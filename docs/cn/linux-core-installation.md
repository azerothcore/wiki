# Linux 核心安装

| 安装指南                                                                                                                             |                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 1 步：环境要求](linux-requirements)                                                                                           | [第 3 步：服务器设置 >>](linux-server-setup)                                |

## 安装目录

以下步骤会将 AzerothCore 安装到 `$AC_CODE_DIR`。默认情况下，该路径为 `$HOME/azerothcore`。如果需要，此路径可以更改为用户有权访问的任何其他位置。

某些示例中还会使用 `azerothuser` 用户。同样，你也可以根据需要将其更改为任意用户。

**注意**：在以下命令中，变量 `$HOME` 是**当前用户**的路径，因此如果你以 root 身份登录，则 $HOME 将为 "/root"。你可以如下所示检查环境变量的状态：

```sh
echo $HOME
```

按如下方式配置安装目录：

```sh
export AC_CODE_DIR=$HOME/azerothcore
```

## 所需软件

继续之前请先查看[环境要求](linux-requirements)。

## 获取源代码

选择以下方法中的**一种**，在终端中运行下面其中一个 `git ...` 命令。

1. 仅克隆 master 分支 + 完整历史记录（体积较小 - 推荐）：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR
    ```

1. 仅克隆 master 分支 + 无历史记录（体积最小）：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR --depth 1
    ```

    注意：如果你想恢复完整的历史记录，请使用 `git fetch --unshallow`。

1. 克隆所有分支和所有历史记录：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git $AC_CODE_DIR
    ```

这会在你的主目录中创建一个包含 AC 源文件的 `azerothcore` 目录。

## 编译源代码

> [!WARNING]
> 使用较新版本的 Debian 或 Ubuntu 时，存在自动更新检查和安装机制，这可能会破坏服务器的正常运行！
> 事实上，例如 MySQL 可能会被自动更新（甚至是在服务器运行时！），导致 `authserver` 和 `worldserver` 立即崩溃，这种情况可能会造成游戏时间的损失。
>
> 因此，为避免这种情况，只需这样做：
> 1. 编辑文件 `sudo nano /etc/apt/apt.conf.d/20auto-upgrades`
> 2. 注释掉所有行
> 3. 重启
>
> 这将防止系统更新某些有用的程序，从而避免你的游戏服务器崩溃。
> 
> 链接：  
> https://discord.com/channels/217589275766685707/1255602330431127753/1369358673465442405
> https://discord.com/channels/217589275766685707/555424966137479180/1445387284768620554

### 创建构建目录

为避免更新和源构建冲突带来的问题，我们创建一个专用的构建目录，从而避免任何可能因此产生的问题（如果确实会发生的话）。

```sh
cd $AC_CODE_DIR
mkdir build
cd build
```

### 配置编译 {#configuring-for-compiling}

高级用户的参数说明请参阅 [CMake 选项](cmake-options)。

此时，你必须位于 `$AC_CODE_DIR/build` 目录中。

**注意**：如果你使用了非默认的 `clang` 包，则需要相应地替换。例如，如果你安装了 `clang-6.0`，则必须将 `clang` 替换为 `clang-6.0`，并将 `clang++` 替换为 `clang++-6.0`。

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static
```

要了解可用的核心数，可以使用以下命令：

```sh
nproc --all
```

设置用于构建的核心数，如有必要，请将命令中的数字替换为你想要执行的线程数：

```sh
export BUILD_CORES=`nproc | awk '{print $1 - 1}'`
```

然后输入：

```sh
make -j$BUILD_CORES
make install
```

将这些命令保存在脚本中或以其他方式记下来可能会很有用。每当你更新 AzerothCore 或添加新模块时，都需要重新运行这三条命令。例如：

```sh
#!/bin/bash

BUILD_CORES=`nproc | awk '{print $1 - 1}'`
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static &&
make -j$BUILD_CORES &&
make install
```

## （可选）Systemd 服务 {#optional-systemd-services}

Systemd 服务可以帮助你管理 AzerothCore 服务器。下面显示的服务文件在大多数发行版中必须由 `root` 用户安装。在大多数发行版中，合适的位置是 `/etc/systemd/system`。

由于这些命令在运行时无法访问用户的环境变量，因此安装目录 `$AC_CODE_DIR` 必须完全展开，例如 `/home/azerothuser/azerothcore`。如果不确定该值，请以你的用户身份运行 `echo $AC_CODE_DIR`。

设置运行这些单元的用户。此处使用的用户名为 `azerothuser`，应替换为你的用户名。
```sh
export AC_UNIT_USER=azerothuser
```

### ac-authserver.service

```sh
sudo tee /etc/systemd/system/ac-authserver.service << EOF
[Unit]
Description=AzerothCore Authserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=$AC_CODE_DIR/acore.sh run-authserver

[Install]
WantedBy=multi-user.target
EOF
```

### ac-worldserver.service

```sh
sudo tee /etc/systemd/system/ac-worldserver.service << EOF
[Unit]
Description=AzerothCore Worldserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=/bin/screen -S worldserver -D -m $AC_CODE_DIR/acore.sh run-worldserver

[Install]
WantedBy=multi-user.target
EOF
```

使用 `systemctl daemon-reload` 让 systemd 识别这些新的服务文件。你可以像这样启动 AzerothCore：

```sh
sudo service ac-worldserver start
sudo service ac-authserver start
```

或者停止它：

```sh
sudo service ac-worldserver stop
sudo service ac-authserver stop
```

可以通过以下方式设置服务器在系统启动时自动启动：

```sh
sudo systemctl enable ac-authserver
sudo systemctl enable ac-worldserver
```

你可以通过查看 systemd 日志中的日志条目来检查服务是否正确启动，如下所示：

```sh
sudo journalctl ac-authserver.service
sudo journalctl ac-worldserver.service
```

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 1 步：环境要求](linux-requirements)                                                                                           | [第 3 步：服务器设置 >>](linux-server-setup)                                |
