# Linux Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation) | [Step 2: Core Installation >>](linux-core-installation) |

| |
| :- |
| [MySQL](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |
| Boost ≥ 1.74 up to 1.84 |
| OpenSSL ≥ 3.0.x |
| CMake ≥ 3.16 |
| [OS](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |
| [GCC / CLang](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |

#### Ubuntu with MySQL 8.x

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

To configure MySQL in Ubuntu and similar (set `root` password and other settings) read [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

---

#### Debian 12

```sh
apt-get update && apt-get install -y git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

**Note:** By using the option `-y`, it will start installing without the need for you to confirm.

---

#### Install MYSQL

Non-Interactive install using `DEBIAN_FRONTEND="noninteractive"` to install the latest MYSQL-LTS release, e.g. `mysql-8.4-lts` without any user prompts showing up.

```sh
wget https://dev.mysql.com/get/mysql-apt-config_0.8.32-1_all.deb
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_0.8.32-1_all.deb
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

If you are still having problems, check:

* [FAQ](faq)

* [Common Errors](common-errors)

* [How to ask for help](how-to-ask-for-help)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation) | [Step 2: Core Installation >>](linux-core-installation) |
