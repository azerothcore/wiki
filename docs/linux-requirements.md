# Linux Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md) | [Step 2: Core Installation >>](core-installation.md) |

| |
| :- |
| MySQL ≥ 5.7.0 |
| CMake ≥ 3.16 |
| Clang ≥ [6](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) |

#### Ubuntu with MariaDB 10.x

```sh
sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libace-6.* libace-dev mariadb-server mariadb-client libmariadb-dev libmariadbclient-dev libmariadb-dev-compat
```

#### Ubuntu with MySQL 8.x

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

To configure MySQL in Ubuntu 18.04 and similar (set `root` password and other settings) read [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

**Note**: in older versions of Ubuntu like **18.04** you need to install gcc 10:

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt install gcc-10 g++-10
```


--- 

#### Debian 8

```sh
sudo apt-get update && sudo apt-get install git make gcc g++ clang libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

#### Install last cmake version on Debian 8

To install last version of cmake use:

```sh
sudo apt install python3-pip
pip3 install --upgrade cmake
```

If you are using the `root` user

```sh
apt install python3-pip
pip3 install --upgrade cmake
```

Than **reboot** to sync the bash and use cmake from the terminal, than type the followings commands to check the cmake version:

```sh
cmake --version
```

You should have a version **>= 3.16**.

Continue below the guide to install the other installation requirements.

**Troubleshooting (cmake install)**: if you get any errors like: `No module named 'skbuild'`, you can solve with this:

```sh
apt install python3-pip
pip3 install scikit-build
pip3 install --upgrade pip
pip3 install cmake
```

---

#### Debian 9

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev
```

Remember that if you are using the `root` user, it is not necessary to use `sudo`.

You might need to add the stretch-backports repositories to APT in order to install clang-6.x+ and cmake v3.8+.
If you do not succeed installing cmake you can use the package manager of python3 (pip3)

---

#### Debian 10

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libace-6.* libace-dev
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

Your `clang` version **MUST** be `6` or higher ([here](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) you can check the versions that run in our Github Actions pipeline, we recommend to use one of those versions).

For example, if you are using an older version of Ubuntu like 16.04, you need to install clang using:

```sh
sudo apt-get install clang-6.0
```

If you use another distro or version, search on google for how to install the right clang version for your system.

#### Check your cmake version

```sh
cmake --version
```

Your `cmake` version **MUST** be `3.16` or higher.

On an older version of Ubuntu (example: 16.04), you can follow the instructions here in order to install the latest cmake version. On debian you would need to use the backports sources or build Cmake manually.

#### Ensure that the gcc-7 headers are installed

This is an issue if for example using an older version of Ubuntu like 16.04. There you have to add the PPA "Toolchain test builds":
https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test

After

```sh
sudo apt-get update
```

you can install gcc-7: 

```sh
sudo apt-get install g++-7 gcc-7
```

<br>

## Help

If you are still having problems, check:

* [How to ask for help](How-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md) | [Step 2: Core Installation >>](core-installation.md) |
