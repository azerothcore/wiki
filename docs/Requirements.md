# AzerothCore Requirements

## GNU/Linux

### Debian-based requirements

#### Ubuntu

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

---

## Mac OS X

- Install XCode using the App Store, then open the terminal and type:

```sh
xcode-select --install
```

- Install the package manager [Homebrew](http://brew.sh/)

Use brew it to install the required packages:

```sh
brew update
```

```sh
brew install openssl readline cmake ace coreutils bash bash-completion coreutils
```

This will install bash 5+, you might need to restart your terminal.
Make sure you are using bash 5 or newer by typing `bash --version`.

Now install mysql:

```sh
brew install mysql
```

You will be prompted some instructions to complete the `mysql` installation, for example to properly set a password. Just follow the instructions and properly configure mysql. **This step is important, do not skip it.**

To verify that mysql has been properly installed, try accessing it using either the command line (e.g. `mysql -u root -p`) or using DB client managers with a UI like Sequel Ace.

You can install Sequel Ace with:

```sh
brew cask install sequel-ace
```


## Windows

* Install [Visual Studio](https://visualstudio.microsoft.com/downloads/) VS 2019 Community

* Install [CMake](https://cmake.org/) version 3.16 or higher

* Install latest version of [Git Extensions](https://git-scm.com/download/win)

* [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/) (version 8.0 or 5.7, older versions are not supported)

* Install [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) version 1.0.x or 1.1.x (Do not install the Light version) 
  
  Download the 64bit version. Or you can get both if you plan to compile both 32 and 64bit, they can coexist side by side.

1. Find the 64bit version by finding the _latest _ **Win64 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win64 OpenSSL v1.0.1p**

2. Find the 32bit version by finding the _latest _ **Win32 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win32 OpenSSL v1.0.1p**

3. _Note #1: If you get a "Missing Microsoft Visual C++ 2008 Redistributables" error message while installing OpenSSL, download the ** [Microsoft Visual C++ 2008 Redistributable Package (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=29) ** (1.7MB Installer) and install it. If you need 32bit support, download and install the [ **Microsoft Visual C++ 2008 Redistributable Package (x86)** ](http://www.microsoft.com/en-us/download/details.aspx?id=15336)._
4. _Note #2: While installing OpenSSL, choose **The OpenSSL binaries (/bin) directory** (NOT "The Windows system directory") when given the choice on where to copy the OpenSSL DLLs. These DLLs will need to be located easily for Core Installation._
