# Linux Requirements

| Installation Guide                                                                                                                   |                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](linux-core-installation) |

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
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

Ubuntu 26.04 already provides supported MySQL packages through the default repositories, so the command above is enough.

---

#### Ubuntu 24.04

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

Ubuntu 24.04 does not ship the recommended MySQL release in its default repositories. After installing the base packages above, follow the **Install MySQL** steps below to install MySQL 8.4 LTS.

---

#### Debian 12 & 13

```sh
apt-get update && apt-get install -y git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget screen
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

**Note:** By using the option `-y`, it will start installing without the need for you to confirm.

---

##### Install MySQL

1. Visit the [MySQL APT repository](https://dev.mysql.com/downloads/repo/apt/) page to verify and download the latest script version.
```sh
export MYSQL_APT_CONFIG_VERSION=0.8.36-1
```

1. Download the latest MySQL repository information package.

```sh
wget https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
```

1. (Recommended) Verify config authenticity. If you encounter any issues with this step, please refer to: https://dev.mysql.com/doc/refman/8.4/en/checking-gpg-signature.html
```sh
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
gpg --keyserver pgp.mit.edu --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
```

1. Non-Interactive install using `DEBIAN_FRONTEND="noninteractive"` to install the latest MYSQL-LTS release, e.g. `mysql-8.4-lts` without any user prompts showing up.

```sh
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
unset MYSQL_APT_CONFIG_VERSION
sudo apt-get update
sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y mysql-server libmysqlclient-dev
```

---

#### Check your clang version

```sh
clang --version
```

Your `clang` version **MUST** be equal or higher than the required version listed on the top of this page.

---

#### Check your cmake version

```sh
cmake --version
```

Your `cmake` version **MUST** be equal or higher than the required version listed on the top of this page.

---

#### Check your openssl version

```sh
openssl version
```

Your `openssl` version **MUST** be equal or higher than the required version listed on the top of this page.

--

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](linux-core-installation) |
