# Linux Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md) | [Step 2: Core Installation >>](core-installation.md) |

| |
| :- |
| MySQL ≥ 5.7.0 |
| Boost ≥ 1.67 |
| CMake ≥ 3.16 |
| Clang ≥ [7](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) |

#### Ubuntu with MariaDB 10.x

```sh
sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libace-6.* libace-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadbclient-dev libmariadb-dev-compat
```

#### Ubuntu with MySQL 8.x

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libboost-all-dev libace-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

To configure MySQL in Ubuntu 18.04 and similar (set `root` password and other settings) read [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

**Note**: in older versions of Ubuntu like **18.04** you need to install `gcc-10` and `libboost1.74-dev`:

```
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo add-apt-repository -y ppa:mhier/libboost-latest
sudo apt-get update
sudo apt install -y gcc-10 g++-10
sudo apt install -y install libboost1.74-dev
```

--- 

#### Debian 10

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libace-6.* libace-dev libboost-all-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

**Note:** If you add the option `-y` and at the end of the list, it will start installing them without the need for you to confirm.

**Example:**

```sh
apt-get update && apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libace-6.* libace-dev -y
```

--- 

#### Check your clang version

```sh
clang --version
```

Your `clang` version **MUST** be `7` or higher ([here](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) you can check the versions that run in our Github Actions pipeline, we recommend to use one of those versions).

For example, if you are using an older version of Ubuntu like 18.04, you need to install clang using:

```sh
sudo apt-get install clang-7.0
```

If you use another distro or version, search on google for how to install the right clang version for your system.

#### Check your cmake version

```sh
cmake --version
```

Your `cmake` version **MUST** be `3.16` or higher.

On an older version of Ubuntu (example: 16.04), you can follow the instructions here in order to install the latest cmake version. On debian you would need to use the backports sources or build Cmake manually.

#### Ensure that the gcc-8 headers are installed

This is an issue if for example using an older version of Ubuntu like 16.04. There you have to add the PPA "Toolchain test builds":
https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test

After

```sh
sudo apt-get update
```

you can install gcc-8: 

```sh
sudo apt-get install g++-8 gcc-8
```

---

## Help

If you are still having problems, check:

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md) | [Step 2: Core Installation >>](core-installation.md) |
