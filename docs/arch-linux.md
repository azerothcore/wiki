# Arch Linux Install
This page covers Arch Linux-specific dependency setup for AzerothCore. It is intended to be used together with the [Linux Classic Installation](classic-installation) guide.

There are two ways to install AzerothCore: manual installation or the experimental AUR package.

## Manual Core Installation

### Before you begin
- This guide does not explain how to install Arch Linux itself.
- Make sure your system is up to date and you have a normal user with `sudo` privileges.
- The [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) is the best source for general Arch installation and package management.

Make sure your system is fully up to date, and if you update the kernel, please reboot into the new kernel before continuing.
```sh
sudo pacman -Syu
```

### Required packages
Install the core development packages needed to build AzerothCore:

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

### MySQL on Arch Linux
AzerothCore requires Oracle MySQL. Oracle MySQL is not available from the official Arch repositories, so this guide installs it from the AUR.

> {% include warning.html content="Trusting keys is always up to the user to verify that the key being trusted should be. If you have any doubts or concerns, stop here and use a different installation method." %}

Import the MySQL signing key:

```sh
gpg --recv-keys B7B3B788A8D3785C
```

Build and install the MySQL AUR package:

> {% include note.html content="This package builds MySQL from source. You will likely need at least 4 gigabytes of memory for the compile to succeed." %}


```sh
mkdir -p ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

After installation, enable and start MySQL:

```sh
sudo systemctl enable --now mysql.service
```

### Next steps
Once your database server is installed and running, continue with the [Linux Classic Installation](classic-installation) guide to compile AzerothCore and finish configuration.

## AUR Install (Experimental)

{% include warning.html content="The AzerothCore package in the AUR has been re-written and is undergoing testing by users. Please offer any feedback in Discord." %}
Special care must be taken so that Arch does not try to install MariaDB as a substitute for MySQL.

The examples below use `yay` to install these dependencies, but you can use another AUR helper. These instructions are intended to work with either approach.

Please note that `acore.sh` is not distributed with this installation method since many of the things it manages are handled differently.

The following executables are installed that can manage parts of the install:

* `acore_setup`: Initializes AzerothCore, sets up a new user, performs the initial database population, and enables remote access to the `AC>` prompt from the background service. It runs on localhost by default.
* `acore_mod`: Automatically compiles and deploys modules checked out to a folder or removes them if they no longer exist.
* `attach-world`: Starts a remote connection session to the server so you can access the `AC>` prompt and disconnect while the server stays running.

### MySQL installation
Due to package definitions and to allow automatic dependency resolution, we must use the named MySQL 8.4 package instead of the newest 9.
```sh
yay -S libmysqlclient84 mysql-clients84 mysql84
```

From here, initialize MySQL. Feel free to change directories and users as needed.

Please note that this will output a temporary password you must remember or copy down for later.
```sh
sudo mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Now we need to start the MySQL service:
```sh
sudo systemctl enable --now mysqld
```

From here, we need to setup our first user by running the MySQL initialization scripts:
```sh
sudo mysql_secure_installation
```
In this script you want to:

1. Change the root password: Set it to whatever you want. The initial password will be the random password output above.
1. Enforce strict password policy: No (this will interfere with the default credentials AzerothCore will create.)
1. Remove anonymous users: Yes
1. Disallow remote login: Yes (this removes remote root accounts only; it does not disable remote access for other users or change the server bind address). Answer Yes by default. If remote database access is needed, configure dedicated non-root users and network access separately.
1. Remove test database: Yes
1. Reload privilege table: Yes

### Install AzerothCore
The core is split into two packages: the core and the client/map data.

If you want to extract the map data yourself, the clientdata package is not required and you can omit it. However, AzerothCore expects the map data to be in `/usr/share/azerothcore/data`.

```sh
yay -S azerothcore-wotlk-git azerothcore-clientdata
```

### Initialize AzerothCore
There is a helper script that is installed as part of this package, `acore_setup`.

```sh
sudo acore_setup
```

This will do some configuration setup, ask you for the mysql user, start the server to pre-populate the database, and then you will be asked to make an account once the server is up with:

```sh
AC> account create <username> <password>
```

Note: This account will be given Game Master privileges!

After performing these steps, the server will shut itself down. You can start everything by enabling and starting the services:

```sh
sudo systemctl enable --now acore-auth-server acore-world-server
```

### Connecting to the AzerothCore
You can connect to the locally running server by running:

```sh
attach-world
```

Then enter your AzerothCore administrator username and password. You can exit at any time by pressing `Ctrl+C`.

> {% include note.html content="Ctrl+C will _not_ shut your server down!" %}

### Module management
> {% include warning.html content="This AUR package is not to be used with PlayerBots module. There is another fork of the core for that module and it is unsupported by this package." %}

To manage modules, clone the repositories to `/usr/src/acore-modules`.

After they have been cloned and you are ready to deploy them, run:
```sh
acore_mod
```

This will:

1. Symbolically link the module source to the place where the AzerothCore source is stored
1. Perform an incremental build to rebuild AzerothCore with the modules
1. Package the sql files to be reinstalled with the new package and stored in the AzerothCore installation directory
1. Install the package
1. Restart the services

> {% include warning.html content="If your module has a config file or settings that need to be added to existing configuration files, you must do this manually! Once updated, restart the world service." %}

### Feedback
This is a work in progress and I have not tested many modules with this. If you run into issues, please post them in Discord. Beck is the user maintaining this package.
