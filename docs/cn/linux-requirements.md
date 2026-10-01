# Linux 环境要求

{% include important.html content="<b>MySQL 26.x.x</b> 不受支持。请改用 <b>MySQL 8.4 LTS</b>。" %}

| 安装指南                                                                                                                             |                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 开始：安装指南](classic-installation)                                                                                            | [第 2 步：核心安装 >>](linux-core-installation)                             |

|                                                                                 |
| :------------------------------------------------------------------------------ |
| [MySQL](https://github.com/azerothcore/azerothcore-wotlk/security/policy)       |
| Boost ≥ 1.74                                                                    |
| OpenSSL ≥ 3.0.x                                                                 |
| CMake ≥ 3.16                                                                    |
| [OS](https://github.com/azerothcore/azerothcore-wotlk/security/policy)          |
| [GCC / CLang](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |

#### Ubuntu 26.04

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libstdc++-16-dev default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev
```

请记住，如果你使用 `root` 用户，则无需使用 `sudo`。

Ubuntu 26.04 已通过默认软件源提供受支持的 MySQL 包，因此上面的命令就足够了。

需要 `libstdc++-16-dev`，因为 clang 21（26.04 上的默认版本）会链接 GCC 16 工具链，而默认的 `g++` 是 GCC 15，只附带 GCC 15 的 C++ 开发文件。缺少它时，CMake 会报 `cannot find -lstdc++` 错误（[ACE00068](common-errors#ace00068)）。如果未来 Ubuntu 更新改变了 clang 选择的 GCC 版本，请运行 `clang++ -v`，并安装与 `Selected GCC installation` 行匹配的 `libstdc++-<版本>-dev`。

---

#### Ubuntu 24.04

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget
```

请记住，如果你使用 `root` 用户，则无需使用 `sudo`。

Ubuntu 24.04 的默认软件源中没有提供推荐的 MySQL 版本。安装完上面的基础包后，请按照下面的**安装 MySQL**步骤安装 MySQL 8.4 LTS。

---

#### Debian 12 和 13

```sh
apt-get update && apt-get install -y git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget screen
```

请记住，如果你使用 `root` 用户，则无需使用 `sudo`。

**注意：** 使用 `-y` 选项后，将无需你确认即可开始安装。

---

##### 安装 MySQL

1. 访问 [MySQL APT 软件源](https://dev.mysql.com/downloads/repo/apt/)页面，以验证并下载最新的脚本版本。
```sh
export MYSQL_APT_CONFIG_VERSION=0.8.36-1
```

1. 下载最新的 MySQL 软件源信息包。

```sh
wget https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
```

1. （推荐）验证配置的真实性。如果此步骤遇到任何问题，请参阅：https://dev.mysql.com/doc/refman/8.4/en/checking-gpg-signature.html
```sh
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
gpg --keyserver pgp.mit.edu --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
```

1. 使用 `DEBIAN_FRONTEND="noninteractive"` 进行非交互式安装，以安装最新的 MYSQL-LTS 版本，例如 `mysql-8.4-lts`，全程不会出现任何用户提示。

```sh
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
unset MYSQL_APT_CONFIG_VERSION
sudo apt-get update
sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y mysql-server libmysqlclient-dev
```

---

#### 检查你的 clang 版本

```sh
clang --version
```

你的 `clang` 版本**必须**等于或高于本页顶部所列的所需版本。

---

#### 检查你的 cmake 版本

```sh
cmake --version
```

你的 `cmake` 版本**必须**等于或高于本页顶部所列的所需版本。

---

#### 检查你的 openssl 版本

```sh
openssl version
```

你的 `openssl` 版本**必须**等于或高于本页顶部所列的所需版本。

--

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 开始：安装指南](classic-installation)                                                                                            | [第 2 步：核心安装 >>](linux-core-installation)                             |
