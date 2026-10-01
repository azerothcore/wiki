{% include warning.html content="本指南面向 Debian 9，其安装命令会拉取一些已不再使用或无法获取的软件包（MariaDB、已被移除的 ACE 库 <code>libace</code>、<code>libssl1.0-dev</code>、<code>g++-7</code>），因此下面的构建步骤在当前系统上无法正常工作。请勿遵循这里的安装命令。如需最新的 VPS 安装教程，请参考 [Debian 12 安装指南](debian12-install-guide) 或主 [安装指南](installation)。" %}

## 简介

本教程将带你完成 AzerothCore 服务器安装的整个过程，并帮助你熟悉 Debian 和命令行界面（CLI）的使用。在本教程中，我们将涵盖以下内容：
- 了解各种帮助你搭建并运行服务器的工具，例如 MySQL 客户端、SSH 客户端、SFTP 客户端以及强大的文件编辑器。
- 从零开始配置一个 DigitalOcean Droplet
- 编译 Core
- 导入数据库

还有一个分步的 YouTube 视频，带你走完整个过程。建议你在观看该视频的同时，把本教程作为参考指南。

[![教程视频](https://img.youtube.com/vi/lenMiDtbHhs/0.jpg)](https://www.youtube.com/watch?v=lenMiDtbHhs)

## 你可能需要的 PC 应用程序：
#### MySQL 客户端：
- [HeidiSQL](https://www.heidisql.com/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [SQLYog](https://www.webyog.com/product/sqlyog)（付费）

#### SSH 客户端：
- DigitalOcean 的控制台
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [Termius](https://termius.com/)（付费）

#### FTP 客户端：
- [Filezilla](https://filezilla-project.org/)
- [Terminus](https://termius.com/)（付费）

#### 文件编辑器：
- [Visual Studio Code](https://code.visualstudio.com/)
- [Notepad++](https://notepad-plus-plus.org/)

## 选择我们的 Droplet
#### 新建 Droplet
- 8GB 内存 / 4 核
- Debian 9
- 选择区域
- 启用监控
- 一次性密码
- 给 Droplet 起一个你喜欢的名字，在本教程中我们将其命名为 `AzerothCore`

## Droplet 初始配置
#### 更改你的时区
- 输入命令 `timedatectl` 确认 Droplet 已设置为 UTC（00:00）时间。
- 在设置时区之前，我们首先需要弄清楚你的时区对应的代码。输入命令 `timedatectl list-timezones` 查看所有时区的列表。按 Enter 键直到找到你的时区，并记下它。查看完时区后按 *Control+C* 退出。
- 回到命令行后，输入 `sudo timedatectl set-timezone YOUR_TIME_ZONE`
- 输入 `timedatectl` 验证时区设置是否正确

#### 添加新用户
- 最佳实践是不为应用程序使用 *root* 用户。因此，我们将创建一个负责所有 AzerothCore 相关操作的用户。输入 `adduser azcore` 创建新用户。
- 接下来，确保该用户拥有 sudo 权限。使用以下命令授予这些权限 `usermod -aG sudo azcore`

#### 验证新用户的 sudo 权限
- 让我们以新用户身份登录 `sudo su azcore`
- 输入 `sudo whoami`，然后输入你为该用户设置的密码（可能与你的 root 密码不同）。
- 如果显示 *root*，那么一切就绪！输入命令 `exit` 返回 root 用户以进行后续步骤。

#### 安装关键库和附加应用程序
- 接下来，我们需要安装一批 AzerothCore 所需的重要库、应用程序和工具。运行以下命令：
```
sudo apt-get update && sudo apt-get install git make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev g++-7
```
- 对于任何询问是否为安装预留额外空间的提示，选择 'Y'。
- 在继续之前，让我们再次刷新应用程序列表 `sudo apt-get update`
- 让我们安装 Screen，它允许我们同时打开多个应用程序，并在注销控制台后保持运行 `sudo apt-get install screen`
- 接下来是 curl——我们将用它来获取 VMAP、MMAP 以及服务器所需的其他数据 `sudo apt install curl`
- 让我们安装 unzip 工具，以便解压数据文件 `sudo apt install unzip`
- 最后，用 `sudo apt install` 收尾

#### 安装 CMake
- 让我们先移除之前安装的任何 CMake，确保系统上不存在旧版本的 CMake。`sudo apt remove --purge --auto-remove cmake`
- 接下来，我们将开始安装 CMake。复制这一整块内容并粘贴到你的终端中。如果你想安装不同版本的 CMake，可以将版本号和构建号改为其他 CMake 版本，可在 https://cmake.org/download/ 上找到。
```
version=3.16
build=2
mkdir ~/temp
cd ~/temp
wget https://cmake.org/files/v$version/cmake-$version.$build.tar.gz
tar -xzvf cmake-$version.$build.tar.gz
cd cmake-$version.$build/
```
- 看到大量输出后，在键盘上按一次 'Return' 或 'Enter'。
- 现在安装 CMake。复制这一整块内容并粘贴到你的终端中。
```
./bootstrap
make -j$(nproc)
sudo make install
```
- 构建完成后（并重新回到命令行），在键盘上按一次 'Return' 或 'Enter' 来安装 CMake
- 让我们使用 `cmake --version` 命令验证你运行的是正确的 CMake 版本。注意：如果 CMake 版本命令不起作用，请关闭终端，重新连接，然后再试一次版本命令。
- 输入 `cd` 返回你的主目录。
- 让我们用 `rm -rf temp` 清理 CMake 的安装。现在让我们来看一下如何配置数据库。

#### 完成 MariaDB 安全安装
- 让我们开始这个过程 `sudo mysql_secure_installation`
- 对于以下提示，依次回答 `[no pass]/N/Y/Y/Y/Y`
- 回到命令行后，输入 `sudo mysql` 进入 MariaDB 控制台
- 进入 MariaDB 控制台后，让我们创建我们的用户：
```
GRANT ALL ON *.* TO 'dbadmin'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;
```
- 选择你想要的用户名——可以是任何你喜欢的名字，不一定是 `dbadmin`。另外，请确保选择一个非常安全的密码，`password1` *绝对不要* 使用。
- 让我们刷新 MariaDB 的权限 `Flush Privileges;`
- 返回 Debian 主控制台 `exit`

#### 配置 MariaDB 的远程连接
- 进入存放所需文件的目录 `cd /etc/mysql/mariadb.conf.d`
- 用 nano 文件编辑器打开配置文件 `nano 50-server.cnf`
- 找到 Bind Address，并将其更新为：`0.0.0.0`
- 要保存更改，请按 *Ctrl + X*，然后按 *Y*，接着按 *Ctrl + T*。然后使用方向键选择 `50-server.cnf`
- 既然我们已经更新了关键的 MariaDB 配置文件，我们需要重启 MariaDB 进程。输入 `sudo /etc/init.d/mysql restart`

#### 配置简易防火墙（UFW）
- 让我们刷新应用程序目录 `sudo apt update`
- 让我们安装 UFW `sudo apt install ufw`
- 接下来，我们将默认阻止所有传入连接。这是保护服务器的重要一步。我们将在后续步骤中开放端口 `sudo ufw default deny incoming`
- 接下来，让我们默认允许所有传出连接。这将使你的服务器能够顺利发起外部请求。`sudo ufw default allow outgoing`
- 我们需要确保自己不会被锁在控制台之外，因此需要放行 22 端口，也就是 SSH 使用的端口。为此，输入 `sudo ufw allow ssh`
- 让我们允许 MariaDB 端口接受传入连接 `sudo ufw allow 3306`
- 让我们允许认证服务器接受传入连接 `sudo ufw allow 3724`
- 然后是 Worldserver 端口 `sudo ufw allow 8085`
- 确认你已经放行了上述所有端口，然后用下面的命令开启 UFW：`sudo ufw enable`

## AzerothCore 安装
#### 克隆 AzerothCore 仓库
- 以我们的 sudo 用户身份登录 `sudo su azcore`
- 进入我们的主目录 `cd`
- 让我们下载并克隆最新版本的 AzerothCore `git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore`
- 克隆完成后，让我们进入 git 目录的顶层文件夹 `cd azerothcore`
- 我们需要创建一个名为 *build* 的文件夹 `mkdir build`
- 进入新的 build 文件夹 `cd build`
- 现在我们运行 cmake 命令，这是编译前的准备步骤，用于确保所有 cpp 文件在编译前都被考虑在内，并告诉编译器要编译什么。
```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DTOOLS=0 -DSCRIPTS=static
```
- 现在我们编译 AzerothCore——根据你的 Droplet 拥有的 CPU 核心数量，这可能需要一些时间。本教程基于 4 核 CPU 的 Droplet，编译大约需要 8 分钟。输入以下命令编译核心，并将编译好的文件安装到它们的新位置：
```
MTHREADS=`grep -c ^processor /proc/cpuinfo`; MTHREADS=$(($MTHREADS + 2));
make -j $MTHREADS;
make install -j $MTHREADS;
```
- 编译完成后，终端会显示 `make install -j $MTHREADS`，此时在键盘上按 'Return' 或 'Enter' 进行安装并完成编译过程。

#### 数据文件
- 以 `azcore` 用户身份，让我们返回主目录 `cd`
- 现在我们需要进入编译后的服务器文件夹 `cd azeroth-server`
- 我们需要为数据文件创建一个文件夹并进入其中 `mkdir data;cd data`
- 让我们下载所需的数据文件。`curl https://wow.heyaapl.com/data.zip --output data.zip`
- 让我们解压主数据目录 `unzip data.zip`

#### 设置服务器配置文件
- 使用 SFTP，进入 `/home/azcore/azeroth-server/etc` 并将 authserver.conf.dist 和 worldserver.conf.dist 下载到你的本地机器。
- 在本地机器上重命名它们，去掉文件名中的 .dist。
- 使用你的文件编辑器更新 Authserver 和 Worldserver 配置文件中的数据库信息。使用你之前在步骤中创建的用户名和密码来更新数据库连接信息。
- 在 Worldserver 配置中，将 DataDir 文件夹设置为：`"/home/azcore/azeroth-server/data"`
- 使用你的 SFTP 客户端将 .conf 文件上传回 etc 目录。

#### 初始数据库安装与导入
- 与之前修改 Authserver.conf 和 Worldserver.conf 类似，我们需要更新数据库导入配置文件。使用 SFTP，进入 `/home/azcore/azerothcore/conf/dist/` 找到 `config.sh`。将其下载到你的本地机器。
- 在编辑器中打开 `config.sh`，找到 *DB EXPORTER/IMPORTER CONFIGURATIONS* 部分。
- 从第 153 行开始，将数据库登录信息替换为本教程前面设置的数据库用户名和密码。对 Auth、Character 和 World 数据库配置部分（分别从第 153、158 和 163 行开始）都要进行此操作。
- 保存 `config.sh` 并上传回目录 `/home/azcore/azerothcore/conf/`。
- 我们需要位于 git 目录中才能执行导入脚本，因此输入以下命令 `cd /home/azcore/azerothcore`
- 输入以下命令启动数据库导入脚本 `bash apps/db_assembler/db_assembler.sh`。我们需要配置所有数据库，因此要选择 *Import-all: Assemble & Import All*。输入 `import-all` 并按回车。每次执行后可能会报错，但这没关系——它会成功导入每个数据库。重复整个步骤，直到 World 数据库加载完成。World 数据库导入完成后输入 `quit`。

## 服务器启动
#### 最终配置
- 使用你的 MySQL 客户端连接到数据库。DigitalOcean 服务器的 IP 地址即主机名，用户名是你的数据库用户名，密码是你的数据库密码。端口默认为 3306。连接。
- 进入 `acore_auth` 数据库，打开名为 `realmlist` 的表。查看该表的数据。
- 将 `address` 值更新为你的服务器 IP 地址。如果你愿意，也可以在这里更新你服务器的真实服务器（realm）名称。

#### 启动你的服务器
- 在你的 SSH 终端中，输入以下命令 `cd /home/azcore/azeroth-server/bin`
- 现在，让我们启动 Authserver。我们使用 Screen，以便同时打开 Authserver 和 Worldserver。我们将 Authserver 的 Screen 命名为 'auth'。输入以下命令启动它 `screen -AmdS auth ./authserver`。输入 `screen -r auth` 验证它是否成功启动。按 *Ctrl + A，然后按 D* 退出 auth screen。要完全退出 screen，按 *Ctrl + C*。这会终止进程，所以只在关闭 Authserver 时使用。
- 现在，让我们启动 Worldserver。我们将 Worldserver 的 Screen 命名为 'world'。输入以下命令启动它 `screen -AmdS world ./worldserver`。输入 `screen -r world` 验证它是否成功启动。按 *Ctrl + A，然后按 D* 退出 world screen。要完全退出 screen，按 *Ctrl + C*。这会终止进程，所以只在关闭 Worldserver 时使用。
- 附注：如果你想了解更多关于我们初始化 Screen 时传入 `AmdS` 的原因，或者想看看是否有其他想传入的参数，[这里有一份很好的参考](https://linux.die.net/man/1/screen)，说明了每个字母的含义及其用途。

#### 创建你的游戏内账号
- 输入 `screen -r world` 进入 world screen
- 输入以下命令创建你的新账号 `account create [accountname] [password]`
- 接下来，让我们把你的新账号设为管理员账号 `account set gmlevel [accountname] 3 -1`

#### 更新你的 Realmlist
- 将你的 realmlist.wtf 设置为你的 DigitalOcean IP，该文件位于 `[WoW 目录]/data/enUS`。用你的编辑器修改，然后登录吧！
