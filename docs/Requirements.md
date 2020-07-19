# AzerothCore Requirements

## GNU/Linux

### Debian-based requirements

#### Ubuntu
`sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev`

To configure MySQL in Ubuntu 18.04 and similar (set `root` password and other settings) read [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

--- 


#### Debian 8

`sudo apt-get update && sudo apt-get install git make gcc g++ clang libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev`

#### Install last cmake version on Debian 8

To install last version of cmake use:
```
sudo apt install python3-pip
pip3 install --upgrade cmake
```

Than **reboot** to sync the bash and use cmake from the terminal, than type the followings commands to check the cmake version:
```
cmake --version
```
You should have a version **>= 3.8**.

Continue below the guide to install the other installation requirements.

**Troubleshooting (cmake install)**: if you get any errors like: `No module named 'skbuild'`, you can solve with this:

```
apt install python3-pip
pip3 install scikit-build
pip3 install --upgrade pip
pip3 install cmake
```

#### Debian 9

`sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev`

You might need to add the stretch-backports repositories to APT in order to install clang-6.x+ and cmake v3.8+.
If you do not succeed installing cmake you can use the package manager of python3 (pip3)

#### Debian 10

`sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libace-6.* libace-dev`

--- 


#### Check your clang version

`clang --version`

Your `clang` version **MUST** be `6` or higher ([here](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) you can check the versions that run in our Github Actions pipeline, we recommend to use one of those versions).

For example, if you are using an older version of Ubuntu like 16.04, you need to install clang using:

`sudo apt-get install clang-6.0`

If you use another distro or version, search on google for how to install the right clang version for your system.

#### Check your cmake version

`cmake --version`

Your `cmake` version **MUST** be `3.8` or higher.

On an older version of Ubuntu (example: 16.04), you can follow the instructions here in order to install the latest cmake version. On debian you would need to use the backports sources or build Cmake manually.

#### Ensure that the gcc-7 headers are installed

This is an issue if for example using an older version of Ubuntu like 16.04. There you have to add the PPA "Toolchain test builds":
https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test

After `sudo apt-get update` you can install gcc-7: `sudo apt-get install g++-7 gcc-7`


## Mac OS X

- Install XCode using the App Store, then open the terminal and type:

`xcode-select --install` 

- Install the package manager [Homebrew](http://brew.sh/)

Use brew it to install the required packages:

`brew update`

`brew install openssl readline cmake ace coreutils bash bash-completion coreutils`

Now install mysql:

`brew install mysql`

You will be prompted some instructions to complete the `mysql` installation, for example to properly set a password. Just follow the instructions and properly configure mysql. **This step is important, do not skip it.**

To verify that mysql has been properly installed, try accessing it using either the command line (e.g. `mysql -u root -p`) or using DB client managers with a UI like Sequel Pro.

You can install Sequel Pro with:

`brew cask install sequel-pro`


## Windows

* Install Visual Studio >= 15 ( 2017 Desktop Community, make sure you're using Version 15.9.17+ ) [Microsoft downloads](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)

* Install [CMake](https://cmake.org/) version 2.8 or newer.  

* Install latest version of [Git Extensions](https://git-scm.com/download/win)

* [MySQL Server Community Edition](http://dev.mysql.com/downloads/mysql/5.6.html) (version 5.6 or 5.7, anything later is not supported)

* Install [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) version 1.0.x or 1.1.x (Do not install the Light version) 
  
  Download the 64bit version. Or you can get both if you plan to compile both 32 and 64bit, they can coexist side by side.

1. Find the 64bit version by finding the _latest _ **Win64 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win64 OpenSSL v1.0.1p**

2. Find the 32bit version by finding the _latest _ **Win32 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win32 OpenSSL v1.0.1p**

3. _Note #1: If you get a "Missing Microsoft Visual C++ 2008 Redistributables" error message while installing OpenSSL, download the ** [Microsoft Visual C++ 2008 Redistributable Package (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=29) ** (1.7MB Installer) and install it. If you need 32bit support, download and install the [ **Microsoft Visual C++ 2008 Redistributable Package (x86)** ](http://www.microsoft.com/en-us/download/details.aspx?id=15336)._
4. _Note #2: While installing OpenSSL, choose **The OpenSSL binaries (/bin) directory** (NOT "The Windows system directory") when given the choice on where to copy the OpenSSL DLLs. These DLLs will need to be located easily for Core Installation._

***
