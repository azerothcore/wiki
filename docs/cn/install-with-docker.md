---
tableofcontents: 1
redirect_from: "/cn/Install-with-Docker"
---

# 使用 Docker 安装

欢迎阅读 AzerothCore 的 Docker 安装指南！

AzerothCore 的示例 docker 配置在某些时候可能看起来不太符合惯例，本文档可以帮助用户开始使用基于容器的环境运行 AzerothCore 服务器。

## 准备工作

### 软件要求

唯一的要求是 [git](https://git-scm.com/download/) 和 Docker。

- 对于 GNU/Linux，安装 [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu)
- 对于 macOS 10.12+ Sierra 及更新版本，安装 [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- 对于 Windows 10，安装 [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

你还需要为 docker 安装 `compose` 插件。安装说明可[在此链接](https://docs.docker.com/compose/install/#scenario-one-install-docker-desktop)找到。如果你使用的是安装了 docker desktop 的机器，则无需执行此步骤。

在继续之前，请在终端中键入以下命令，确保系统中已安装 `docker` 和 `docker compose`：

```
docker --version
```
```
docker compose version
```

你应该会看到类似的输出：

```
Docker version 20.10.5, build 55c4c88
Docker Compose version 2.10.2
```

**Windows 用户须知**：你可以使用 **git-bash**（git 自带的 shell）作为终端。

### 克隆 AzerothCore 仓库

你需要克隆 AzerothCore 仓库（或使用你自己的 fork）：

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --depth 1
```

现在使用 `cd azerothcore-wotlk` 进入主目录。**所有命令都必须在（此文件夹内）运行**。

### 安装 {#installation}

要构建容器，请运行 `docker compose build`。然后要启动容器，请运行 `docker compose up -d`

这些命令可以合并为一条：`docker compose up -d --build`

`ac-client-data` 容器会自动将客户端数据下载到卷（volume）中，dbimport 会执行数据库迁移。在首次运行时，这两个操作可能需要 10 到 15 分钟。

db-import 完成后，authserver 和 worldserver 应该会启动，然后你就可以继续[创建账号](#creating-an-account)。

可以使用 `docker compose down` 关闭容器，或使用 `docker compose restart` 重启容器。

本节中提到的所有命令都支持将容器名称作为参数传入。例如，你只能使用 `docker compose up -d --build ac-worldserver` 重新构建并重启 worldserver。

更多 `docker compose` 命令可在[其文档](https://docs.docker.com/compose/reference/)中找到。

### （备选）使用 Dashboard 安装

在终端中（如果你使用 Windows，请使用 git bash），在 azerothcore-wotlk 文件夹内运行以下命令

下面的流程使用我们的 acore.sh dashboard，不过这些命令只是标准 `docker compose` CLI 的一个薄封装。

#### 1) 编译 AzerothCore
```
./acore.sh docker build
```
它将自动构建 docker 镜像并编译核心！这可能需要一段时间。

**对于 Windows：** 如果构建失败并出现类似下面的消息：
```
unable to start container process: exec: "C:/Program Files/Git/usr/bin/bash": stat C:/Program Files/Git/usr/bin/bash: no such file or directory: unknown
```

你可能会遇到 Unix > Windows 路径转换的问题。设置 `MSYS_NO_PATHCONV=1` 环境变量可能会解决此问题：

```
MSYS_NO_PATHCONV=1 ./acore.sh docker build
```

#### 2) 运行容器

```
./acore.sh docker start:app
```

**恭喜！现在你已经拥有了一个正在运行的 azerothcore 服务器！继续下一步创建账号**

如果你需要在后台运行，可以使用以下命令以 docker compose 分离模式运行：

```
./acore.sh docker start:app:d
```

### 创建账号 {#creating-an-account}

#### 1) 访问 worldserver 控制台

打开一个新终端，运行以下命令以附加到 worldserver：

```
docker attach ac-worldserver
```

要分离，请按 `ctrl+p` 和 `ctrl+q`。**不要**尝试使用 `ctrl+c` 分离，否则会杀掉你的 worldserver 进程！

如果你收到错误消息 `the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'`

此命令会自动将你的终端附加到 worldserver 控制台。
现在你可以运行 `account create <user> <password>` 命令来创建你的第一个游戏内账号。更多信息请参见[创建账号页面](creating-accounts)。

### 访问数据库并更新 realmlist

要访问你的 MySQL 数据库，我们推荐使用 [HeidiSQL](https://www.heidisql.com/)（适用于 Windows/Linux+Wine）或 [DBeaver](https://dbeaver.io/)（跨平台）等客户端。使用 `root` 作为用户，`127.0.0.1` 作为默认主机。
root 数据库用户的默认密码为 `password`。

除非你的服务器安装在与客户端相同的机器上，否则你可能需要使用服务器的公网或内网 IP 地址更新 `acore_auth` 数据库中的 `realmlist` 地址：
```sql
USE acore_auth;
SELECT * FROM realmlist;
UPDATE realmlist SET address='$SERVER PUBLIC IP ADDRESS';
```

## 操作流程

### 备份

当你运行任何依赖它的服务器时，进行备份非常重要。对于 AzerothCore，备份很简单，因为它与标准 MySQL 备份相同。

对于每个数据库（通常是 `acore_auth`、`acore_characters` 和 `acore_world`），你应该运行此命令：

```console
$ mysqldump -h 127.0.0.1 -P3306 -u$DATABASE_USERNAME -p$PASSWORD DATABASE_NAME > ./DATABASE_NAME-$(date +%F).sql
```

使用每个数据库的默认设置，命令应该如下所示：

```console
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_auth > acore_auth-$(date +%F).sql
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_characters > acore_characters-$(date +%F).sql
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_world > acore_world-$(date +%F).sql
```
<!-- TODO Add equivalent command for powershell -->

关于这些命令的几点说明：

- 通常最好使用 cron 作业（Linux/MacOS）或计划任务（Windows）来自动执行此命令。
- 命令 `$(date +%F)` 会以 "yyyy-mm-dd" 格式打印日期。这很有用，因为你可以反复运行此命令。
- 默认设置旨在帮助人们尽快上手。如果你运行的是一个依赖它的系统，**你不应该使用 root 用户**（并且 root 用户的密码应该不同），而应该有一个专门用于备份的用户。
- 更多信息，我们强烈建议阅读 [MySQL 的备份与恢复文档](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html)。

### 在容器中配置 AzerothCore

与大多数在容器中运行的应用程序类似，AzerothCore 可以使用环境变量进行配置。你可以从 [worldserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist) 和 [authserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/authserver/authserver.conf.dist) 的默认配置文件中找到有效的配置参数及其说明。在本地，这些文件在构建后可以在 `env/dist/etc` 目录中找到。

在 Docker 中，为 AzerothCore 设置配置的最佳方式是使用 [`docker-compose.override.yml`](https://docs.docker.com/compose/multiple-compose-files/merge/) 文件。这会创建一个额外的文件，它不会被 git 仓库的更新覆盖，同时仍能正确保留你的所有自定义修改。

在找到要修改的参数后（也许是 `AllowTwoside.Interaction.Calendar`），你可以像这样创建一个覆盖文件：

```yaml
# docker-compose.override.yml
services:
  ac-worldserver:
    environment:
      AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR: "1" # AllowTwoSide.Interaction.Calendar
```

弄清楚某个配置参数对应的环境变量名可能有点困难。一般规则如下：

- 整个参数以 `AC_` 为前缀
- 句点（`.`）变成下划线（`_`）
- 小写字母后紧跟大写字母的序列之间会插入下划线（`_`）
- 整个参数大写（因此 `foo` 变成 `FOO`）

几个示例：

- `foo.bar_baz` => `AC_FOO_BAR_BAZ`
- `MaxPrimaryTradeSkill` => `AC_MAX_PRIMARY_TRADE_SKILL`
- `AllowTwoSide.Interaction.Calendar` => `AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR`

### 如何让 AzerothCore 保持最新

首先，你只需要使用 `git` 工具运行以下命令来更新你的仓库：

`git pull origin master`：这将从 azerothcore 仓库下载最新的提交

然后像往常一样[重新构建并重启](#installation)容器

### 如何使用 gdb 运行 worldserver

使用 GDB 运行服务器可以在服务器崩溃时生成 crashdump 文件。该 crashdump 文件有助于开发者了解哪些行出错，并有可能修复问题。

在 AzerothCore docker 容器的早期版本中，gdb 默认包含在内。为了缩小容器体积，这一点已经改变。对于许多需要 gdb 的问题来说，这往往不是 Docker 特有的问题，可以使用诸如 [devcontainer](#devcontainer-support) 之类的工具来进一步调试问题。

请记住，你应该使用 Debug 或 RelWithDebInfo 编译类型来编译代码，否则 gdb 将无法正常工作。

要在 docker 容器中使用 gdb：

1. 编辑 Dockerfile 的 "runtime" 目标
    1. 要确定哪个部分是 "runtime"，它应该是 "FROM skeleton as runtime" 部分下面的大约 15 行
2. 找到此 runtime 部分中的 "apt-get install" 命令
3. 编辑该命令，使其同时安装 GDB，并复制 `gdb.conf` 文件
    1. 它应该看起来像这样：

    ```
    RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libmysqlclient21 libreadline8 \
      gettext-base default-mysql-client \
      gdb gdbserver && \
    rm -rf /var/lib/apt/lists/*

    COPY apps/startup-scripts/gdb.conf /azerothcore/gdb.conf
    ```
4. 编辑你的 `docker-compose.override.yml`，使 `ac-worldserver` 的 `command` 为 `gdb -x /azerothcore/gdb.conf --batch /azerothcore/env/dist/bin/worldserver`
    1. 它应该看起来像这样：

    ```yaml
    services:
      ac-worldserver:
        command: gdb -x /azerothcore/gdb.conf --batch /azerothcore/env/dist/bin/worldserver
    ```

5. 重启并重新构建你的容器，现在 worldserver 应该会用 gdb 运行

如果服务器崩溃，你可以在 `/azerothcore` 文件夹中找到 crashdump 文件（`gdb.txt`）。可以使用 `docker cp ac-worldserver:/azerothcore/gdb.txt ./gdb.txt` 命令将其复制出来。

### .devcontainer 支持 {#devcontainer-support}

在 `docker-compose.yml` 中，我们定义了 `ac-dev-server` 服务
此服务用于我们的构建和数据库操作，但你也可以使用它通过 [VSCode Remote Docker 扩展](https://code.visualstudio.com/docs/remote/containers)进行开发

开发容器（dev-container）可以让你把 Docker 容器用作功能齐全的开发环境。我们项目中的 **.devcontainer** 文件夹包含一些文件，用于告诉 VS Code 如何访问（或创建）一个包含所有所需工具的开发容器。此容器将以处理我们的代码库和调试服务器所需的所有软件和配置来运行 AzerothCore。

在 azerothcore 仓库中有一个预先配置好的 `devcontainer.json`，可以通过 VSCode 命令面板打开。
要设置开发容器，请遵循以下步骤：

1. [安装并打开 VSCode](https://code.visualstudio.com/)
2. 安装 [remote-container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 扩展
3. 在 VSCode 中打开 azerothcore 文件夹
4. 打开 VSCode [命令面板](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)（Ctrl+Shift+P）并运行：`>Remote-Containers: Reopen in Container`

**重要提示**：开发容器还包含一个预先配置好的调试器操作，允许你使用断点并调试你的 worldserver。

不要忘记在你的 [Visual Studio Code](https://code.visualstudio.com/) IDE 中安装 [Remote Container 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

#### 如何使用开发容器调试代码

注意：**请记住，你应该使用 Debug 模式编译代码，否则调试器将无法正常工作**

一旦进入 VSCode 开发容器，你可以进入调试会话并使用 `Linux/Docker debug` 操作，正如你在下图中看到的那样：

![image](https://user-images.githubusercontent.com/147092/115712693-5a837d80-a375-11eb-98aa-b415e1919125.png)

它将以调试模式运行一个 worldserver，然后你可以在代码中开始放置断点来调试它。

![image](https://user-images.githubusercontent.com/147092/115712867-9cacbf00-a375-11eb-9cab-890e4f68d98b.png)

有关如何在 vscode 中调试的更多信息，请参阅[官方指南](https://code.visualstudio.com/docs/editor/debugging)

### 如何使用 docker compose 创建第二个服务器（realm）

TODO

要点是编辑 `docker-compose.yml`（或创建一个覆盖文件）来添加额外的 `ac-worldserver` 和 `ac-db-import` 服务。它们可以从主要部分复制，但应该重命名以避免冲突。

## 常见问题

### 如何安装模块？

为 docker 安装模块与经典安装完全相同：将模块克隆到 `./modules` 并重新运行构建。区别在于 docker 的命令与经典安装不同。

要添加模块，请将模块目录放在 `/azerothcore-wotlk/modules` 目录内。

添加模块后，你必须[重新构建服务器](#installation)并重启容器。

例如，要安装 `mod-solocraft`：

```console
# Clone the module to `modules` with the name of the repository
$ git clone https://github.com/azerothcore/mod-solocraft.git modules/mod-solocraft
# Install SQL files (OPTIONAL)
$ cp modules/mod-solocraft/data/sql/db-characters/mod_solo_craft.sql data/sql/custom/db_characters
# Re-build Azerothcore
$ docker compose up -d --build
```

通过环境变量进行配置适用于模块，但如果你更喜欢配置文件，则必须将它们放在 `azerothcore-wotlk/env/dist/etc/modules` 目录中。如果此 modules 目录不存在，则必须手动创建。

请注意，SQL 也需要手动安装——可以通过将 SQL 文件移动到 `data/sql/custom` 下的相应目录来实现半自动化，也可以针对正确的数据库执行 SQL 文件。

### 服务器日志在哪里？

使用 docker 时，应用程序通常会将日志输出到控制台。通过将日志输出到控制台，docker 会处理日志轮转和持久化。你可以使用 `docker compose logs` 命令查看这些日志。

此外，它们位于 `env/dist/logs`，不过这个位置将来可能会被移除。

### 如何处理权限问题

#### [Linux] 你必须在不使用 sudo 的情况下运行 docker

不使用 sudo 或 root 用户运行 Docker 非常重要。为此，你必须将当前用户设置为 docker 组的成员。

Docker 的文档中提到了这一点：[Linux 的安装后步骤](https://docs.docker.com/engine/install/linux-postinstall/)

### 如何删除我的数据库文件？

**警告** 一旦你删除了数据库文件，除非你有备份，否则它们将无法恢复。

要删除数据库文件，你首先需要确保容器已被停止并移除，方法是输入：`docker compose down`。

停止并移除容器后，你可以输入 `docker volume rm azerothcore-wotlk_ac-database` 来移除卷。

**注意** 如果你将文件夹名称从默认的 `azerothcore-wotlk` 更改，卷名称会略有不同。要找到新的卷名称，可以使用 `docker volume ls` 命令。卷的标签应该类似于 `xxxx_ac-database`。

### 在禁用 docker 默认网桥的情况下构建容器

如果你的 docker 守护进程配置文件（位于 `/etc/docker/daemon.json`）中有 `{"bridge":"none"}`，那么有 2 种方法可以正确构建容器。

这有时会伴随如下错误消息：

```
WARN[0000] buildx: failed to read current commit information with git rev-parse --is-inside-work-tree
network mode "ac-network" not supported by buildkit - you can define a custom network for your builder using the network driver-opt in
buildx create
```

要修复此构建，可以创建一个将构建网络模式设置为 `host` 的 `docker-compose.override.yml`，以允许容器正确构建：

```yaml
# docker-compose.override.yml
services:
  ac-worldserver:
    build:
      network: host
  ac-authserver:
    build:
      network: host
  ac-db-import:
    build:
      network: host
  ac-client-data-init:
    build:
      network: host
```

请注意，这在 Windows 或 MacOS 上不起作用

将 `network` 设置为网络名称的语法（例如在上面的示例中设置 `ac-network` 而不是 `host`）应该可以正常工作，但不幸的是，这似乎无法被 docker 使用或支持，如 [Github Issue](https://github.com/docker/buildx/issues/175) 所示。

### 性能优化（针对开发服务器）

注意：如果你没有遇到任何 I/O 性能方面的特殊问题，我们建议**不要**使用此配置

众所周知，**osxfs** 和 NTFS 在 docker 绑定卷方面存在[性能限制](https://github.com/docker/for-mac/issues/1592)，我们通过尽可能使用卷和 "delegated/cached" 策略优化了 docker compose，但对于某些配置来说这还不够。

* **Windows 用户：** 我们建议使用 [WSL2](https://docs.docker.com/desktop/windows/wsl/) 来克隆我们的仓库并使用 docker 工作。它的性能与原生 linux 环境类似

* **Mac 用户：** 遗憾的是，Mac 上没有类似 WSL2 的东西，不过只有 `ac-dev-server` 使用可能导致这种缓慢的绑定源卷。
  如果你仍然想在 Mac 上使用 `ac-dev-server`，可以考虑尝试 [acore-docker](https://www.azerothcore.org/acore-docker/#dev-server)。它使用命名卷，
  命名卷比绑定卷快得多。

### Docker 参考与支持请求

对于服务器管理员，我们建议阅读 [Docker 文档](https://docs.docker.com/)以及 [Docker Compose 参考](https://docs.docker.com/compose/reference/overview/)。

如果你想成为 AzerothCore 生产服务器的管理员，熟悉并掌握 Docker 和命令行使用会很有帮助。

欢迎在 [StackOverflow](https://stackoverflow.com/) 上提问，并在我们 [Discord 聊天](https://stackoverflow.com/questions/tagged/azerothcore) 的 **#support-docker** 频道中链接它们。我们将很乐意帮助你！
