## 简介

AzerothCore bash 仪表盘（dashboard）是一组用于帮助安装和维护 AzerothCore 服务器的脚本。
它让你只需极少的步骤，就能在你的机器上轻松地安装、更新和运行 AzerothCore。

安装一个用于开发或生产环境的私服从未如此简单。
如果你需要任何帮助，只需[提一个问题](how-to-ask-for-help)。

## 环境要求

你的机器上需要安装有 [git](https://git-scm.com/)、[curl](https://curl.se/)、[unzip](https://github.com/madler/unzip)、[sudo](https://www.sudo.ws/)。
除此之外无需手动安装任何其他软件。

- 基于 debian/ubuntu 的系统：`apt update && apt install git curl unzip sudo`
- macOS：`brew install git`
- Windows：下载并安装 [Git for Windows](https://gitforwindows.org/)

### 注意事项
- 对于 macOS 用户：安装并使用最新版本的 bash 来运行仪表盘的命令（`brew install bash`）
- 对于 Windows 用户：命令需要在 "git bash" shell 或兼容 bash 的 shell（如 WSL、cygwin 等）中执行。
  不过，还是建议使用 git bash，因为它随 Git for Windows 预装（这是我们的环境要求之一）

## 安装设置

### 获取 AC 源码

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk
```

### 配置

有一个 [conf/dist/config.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.sh)
文件包含默认配置。请查看一下它。
大部分默认配置很可能适用于你的情况，
但你也可以把它复制到 `conf/config.sh` 下，并随意修改其中的值。

### 安装所有 AC 依赖

```
./acore.sh install-deps
```

注意：在 Windows 上，需要以管理员身份执行

### 从头开始构建一切

```
./acore.sh compiler all
```

### 设置数据库

- 连接到你的 MySQL 数据库（使用 `sudo mysql -u root`），并通过运行以下命令手动创建 `acore` MySQL 用户：

```
DROP USER IF EXISTS 'acore'@'localhost';
DROP USER IF EXISTS 'acore'@'127.0.0.1';
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore';
CREATE USER 'acore'@'127.0.0.1' IDENTIFIED BY 'acore';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'127.0.0.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit;
```

*注意：尽管 `acore` 用户只能从 localhost 访问，
但将其密码改为更安全的密码仍是一个好习惯。*

### 下载最新的客户端数据

获取最新的客户端数据：

```
./acore.sh client-data
```

### 服务器配置文件

创建以下 2 个文件。它们包含 worldserver 和 authserver 的默认配置，如果你不想修改，直接复制即可。

#### Linux 和 Mac

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

#### Windows 和 Mac

```
cp env/dist/configs/authserver.conf.dist env/dist/configs/authserver.conf
cp env/dist/configs/worldserver.conf.dist env/dist/configs/worldserver.conf
```

### 结果

如果你按照上述步骤操作，你的服务器将位于 `env/dist` 目录内。

`worldserver` 和 `authserver` 二进制文件位于 `azerothcore-wotlk/env/dist/bin`。

你可以直接运行它们，也可以使用重启器（见下文）。
`worldserver` 首次启动时会安装一个完整的 AzerothCore 数据库。此时无需导入任何数据库更新。

另请参阅[网络](networking)和[服务器最终步骤](final-server-steps)。

### 重启器

AzerothCore 仪表盘附带了一套重启器：

```
./acore.sh run-worldserver
```

等待进程运行完成，然后运行：

```
./acore.sh run-authserver
```

对于专用服务器，
你可能希望使用 `tmux`（见下文）等工具在终端复用会话中运行它们。

## 如何更新你的服务器

更新源码：

```
git pull
```

重新编译：
```
./acore.sh compiler build
```

更新数据库：

[database-keeping-the-server-up-to-date](database-keeping-the-server-up-to-date)

就这样。

## 针对专用（生产）服务器的提示

### 通过 Telegram 每日备份数据库

想通过 [Telegram](https://telegram.org/) 消息每天直接把私服数据库的备份发送到你的手机/电脑？

是的，这是可行的。只需使用：[azerothcore/telegram-automated-db-backup](https://github.com/azerothcore/telegram-automated-db-backup)

### Visual Studio Code SSH

你可以在没有任何 GUI 的 Linux 服务器上轻松安装 AzerothCore，
只需通过 [Visual Studio Code](https://code.visualstudio.com/) 使用 SSH 远程连接即可，
配合 [SSH](https://code.visualstudio.com/docs/remote/ssh)
和 [SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) 扩展，
你会感觉就像在自己家里一样。

### 在 Tmux 会话中运行 AzerothCore

你可以使用 [tmux](https://github.com/tmux/tmux) 作为终端复用器，
它可以让你轻松地在没有 GUI 的服务器中管理进程。

你可以创建 2 个会话，并在其中运行 `worldserver` 和 `authserver` 进程：

- `tmux new -s world-session`
- 然后在其中运行 `./acore.sh run-worldserver`，之后从中分离


- `tmux new -s auth-session`
- 然后在其中运行 `./acore.sh run-authserver`，之后从中分离

你可以使用 `CTRL+B+D` 分离，在不终止进程的情况下退出会话。
如果通过 VSCode SSH 连接，你只需关闭终端会话即可。

你可以使用以下命令重新连接到 `world-session` 会话：

- `tmux attach -t world-session`

其他有用的命令：

- 创建新会话：`tmux new -s my_session`
- 列出所有会话：`tmux ls`
- 终止一个会话：`tmux kill my_session`（或连接到它后输入 `exit`）
- 终止所有会话：`tmux kill-server`
- ...更多详情请参见 [tmux wiki](https://github.com/tmux/tmux/wiki)

### 在系统启动时自动启动 tmux 会话

你可以使用这个简单的脚本自动创建 tmux 会话并执行 `authserver` 和 `worldserver`：

```sh
#!/usr/bin/env bash

# ALLOW TMUX TO WAIT FOR MYSQL TO BE READY
# YOU MUST CHANGE THE USER AND PASSWORD TO CORRESPOND WITH YOUR INSTALL
    mysql_ready() {
        mysqladmin ping --host=127.0.0.1 --user=YOURUSER --password=YOURPASSWORD > /dev/null 2>&1
    }

    while !(mysql_ready)
    do
       sleep 3
       echo "waiting for mysql ..."
    done

# CHANGE THESE WITH THE CORRECT PATHS
authserver="/path/to/azerothcore-wotlk/acore.sh run-authserver"
worldserver="/path/to/azerothcore-wotlk/acore.sh run-worldserver"

authserver_session="auth-session"
worldserver_session="world-session"

if tmux new-session -d -s $authserver_session; then
    echo "Created authserver session: $authserver_session"
else
    echo "Error when trying to create authserver session: $authserver_session"
fi

if tmux new-session -d -s $worldserver_session; then
    echo "Created worldserver session: $worldserver_session"
else
    echo "Error when trying to create worldserver session: $worldserver_session"
fi

if tmux send-keys -t $authserver_session "$authserver" C-m; then
    echo "Executed \"$authserver\" inside $authserver_session"
    echo "You can attach to $authserver_session and check the result using \"tmux attach -t $authserver_session\""
else
    echo "Error when executing \"$authserver\" inside $authserver_session"
fi

if tmux send-keys -t $worldserver_session "$worldserver" C-m; then
    echo "Executed \"$worldserver\" inside $worldserver_session"
    echo "You can attach to $worldserver_session and check the result using \"tmux attach -t $worldserver_session\""
else
    echo "Error when executing \"$worldserver\" inside $worldserver_session"
fi
```

在 unix 系统上，你可以使用 [crontab](https://en.wikipedia.org/wiki/Cron)
在系统启动时自动运行该脚本：

```
crontab -e
```

然后添加这一行（将 `/path/to/startup.sh` 替换为你放置上述脚本的路径）：

```
@reboot /bin/bash /path/to/startup.sh
```
