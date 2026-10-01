# Arch Linux 安装
本页介绍 AzerothCore 在 Arch Linux 上的特定依赖设置。它旨在与 [Linux 经典安装](classic-installation) 指南一起使用。

安装 AzerothCore 有两种方式：手动安装或实验性的 AUR 软件包。

## 手动核心安装

### 开始之前
- 本指南不介绍如何安装 Arch Linux 本身。
- 请确保你的系统已更新到最新，并且你拥有一个具有 `sudo` 权限的普通用户。
- [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) 是了解 Arch 常规安装和软件包管理的最佳来源。

确保你的系统完全更新到最新，如果更新了内核，请在继续之前重启进入新内核。
```sh
sudo pacman -Syu
```

### 必需的软件包
安装构建 AzerothCore 所需的核心开发包：

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

### Arch Linux 上的 MySQL
AzerothCore 需要 Oracle MySQL。Oracle MySQL 无法从 Arch 官方软件源获得，因此本指南从 AUR 安装它。

> {% include warning.html content="信任密钥始终取决于用户自己去验证被信任的密钥是否确实应当被信任。如果你有任何疑问或顾虑，请在此停止并使用其他安装方法。" %}

导入 MySQL 签名密钥：

```sh
gpg --recv-keys B7B3B788A8D3785C
```

构建并安装 MySQL AUR 软件包：

> {% include note.html content="该软件包会从源码构建 MySQL。编译成功很可能至少需要 4 GB 内存。" %}


```sh
mkdir -p ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

安装完成后，启用并启动 MySQL：

```sh
sudo systemctl enable --now mysql.service
```

### 后续步骤
一旦你的数据库服务器安装并运行，请继续参考 [Linux 经典安装](classic-installation) 指南来编译 AzerothCore 并完成配置。

## AUR 安装（实验性）

{% include warning.html content="AUR 中的 AzerothCore 软件包已被重写，正在接受用户测试。请在 Discord 中提供任何反馈。" %}
必须特别小心，以免 Arch 尝试安装 MariaDB 来替代 MySQL。

下面的示例使用 `yay` 安装这些依赖，但你可以使用其他 AUR 助手。这些说明旨在兼容任何一种方式。

请注意，`acore.sh` 不随此安装方式分发，因为它管理的许多内容是以不同方式处理的。

以下安装的可执行文件可以管理安装的各个部分：

* `acore_setup`：初始化 AzerothCore，设置新用户，执行初始数据库填充，并允许从后台服务远程访问 `AC>` 提示符。它默认运行在 localhost 上。
* `acore_mod`：自动编译并部署检出到某个文件夹的模块，如果模块不再存在则将其移除。
* `attach-world`：启动到服务器的远程连接会话，以便你访问 `AC>` 提示符，并且可以在服务器保持运行的同时断开连接。

### MySQL 安装
由于软件包定义的原因，并且为了实现自动依赖解析，我们必须使用名为 MySQL 8.4 的软件包，而不是最新的 9。
```sh
yay -S libmysqlclient84 mysql-clients84 mysql84
```

从这里开始，初始化 MySQL。请根据需要随意更改目录和用户。

请注意，这会输出一个临时密码，你必须记住或抄下来供稍后使用。
```sh
sudo mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

现在我们需要启动 MySQL 服务：
```sh
sudo systemctl enable --now mysqld
```

从这里开始，我们需要通过运行 MySQL 初始化脚本来设置我们的第一个用户：
```sh
sudo mysql_secure_installation
```
在这个脚本中你需要：

1. 更改 root 密码：设为你想要的任何值。初始密码将是上面输出的随机密码。
1. 强制严格密码策略：否（这会干扰 AzerothCore 将创建的默认凭据。）
1. 移除匿名用户：是
1. 禁止远程登录：是（这只会移除远程 root 账号；不会禁用其他用户的远程访问，也不会更改服务器的绑定地址）。默认回答是即可。如果需要远程数据库访问，请另行配置专用的非 root 用户和网络访问。
1. 删除测试数据库：是
1. 重新加载权限表：是

### 安装 AzerothCore
核心被拆分为两个软件包：核心本身和客户端/地图数据。

如果你想自己提取地图数据，则不需要 clientdata 软件包，可以省略它。不过，AzerothCore 期望地图数据位于 `/usr/share/azerothcore/data`。

```sh
yay -S azerothcore-wotlk-git azerothcore-clientdata
```

### 初始化 AzerothCore
有一个随此软件包一起安装的辅助脚本，`acore_setup`。

```sh
sudo acore_setup
```

这会进行一些配置设置，询问你的 mysql 用户，启动服务器以预填充数据库，然后当服务器启动后，系统会要求你创建一个账号：

```sh
AC> account create <username> <password>
```

注意：该账号将被授予游戏管理员（Game Master）权限！

执行完这些步骤后，服务器会自行关闭。你可以通过启用并启动服务来启动一切：

```sh
sudo systemctl enable --now acore-auth-server acore-world-server
```

### 连接到 AzerothCore
你可以通过运行以下命令连接到本地运行的服务器：

```sh
attach-world
```

然后输入你的 AzerothCore 管理员用户名和密码。你可以随时按 `Ctrl+C` 退出。

> {% include note.html content="Ctrl+C _不会_ 关闭你的服务器！" %}

### 模块管理
> {% include warning.html content="此 AUR 软件包不能与 PlayerBots 模块一起使用。该模块有另一个核心分支，且此软件包不提供支持。" %}

要管理模块，请将仓库克隆到 `/usr/src/acore-modules`。

克隆完毕并准备好部署它们之后，运行：
```sh
acore_mod
```

这将：

1. 将模块源码符号链接到 AzerothCore 源码存放的位置
1. 执行增量构建，用这些模块重新构建 AzerothCore
1. 打包 sql 文件，以便随新软件包重新安装并存储在 AzerothCore 安装目录中
1. 安装该软件包
1. 重启服务

> {% include warning.html content="如果你的模块有需要添加到现有配置文件中的配置文件或设置，你必须手动完成！更新后，请重启 world 服务。" %}

### 反馈
这仍在完善中，我尚未用很多模块测试过。如果你遇到问题，请在 Discord 中发布。Beck 是维护此软件包的用户。
