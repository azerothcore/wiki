# Linux Core Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](linux-requirements) | [Step 3: Server Setup >>](server-setup) |

## Installation directories

The following steps will install AzerothCore at `$HOME/azerothcore`. This will be in the home directory of the current user. This path can be changed to any other location the user has access to if desired.

The user `azerothuser` will be used in some examples as well. Again, this can be changed to whatever is desired.

## Required software

See [Requirements](linux-requirements) before you continue.

## Getting the source code

Choose **ONE** of the following method, run one of the below `git ...` commands in your terminal.


1. Clone only the master branch + full history (smaller size - recommended):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $HOME/azerothcore
    ```

1. Clone only the master branch + no previous history (smallest size):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $HOME/azerothcore --depth 1
    ```

    Note: If you want to get the full history back, use `git fetch --unshallow`.

1. Clone all branches and all history:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git $HOME/azerothcore
    ```

This will create an `azerothcore` directory in your home folder containing the AC source files.

## Compiling the source code

### Creating the build-directory

To avoid issues with updates and colliding source builds, we create a specific build-directory, so we avoid any possible issues due to that (if any might occur)

```sh
cd $HOME/azerothcore
mkdir build
cd build
```

### Configuring for compiling

Parameter explanation for advanced users [CMake options](cmake-options).

At this point, you must be in your `$HOME/azerothcore/build` directory.

**Note**: in the following command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root". You can check the state of the environment variable, as follows:

```sh
echo $HOME
```

**Note**: in case you use a non-default package for `clang`, you need to replace it accordingly. For example, if you installed `clang-6.0` then you have to replace `clang` with `clang-6.0` and `clang++` with `clang++-6.0`

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azerothcore/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static
```

To know the amount of cores available.
You can use the following command

```sh
nproc --all
```

Then, replacing `6` with the number of threads that you want to execute, type:

```sh
make -j 6
make install
```

It may be useful to preserve these commands in a script or otherwise keep note of them for later. You will need to re-run all three commands again whenever you update AzerothCore or add new modules. For example:

```sh
#!/bin/bash

cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azerothcore/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static &&
make -j 6 &&
make install
```

## Services

systemd services can help you with managing your AzerothCore server. The service files shown below must be installed by `root` in most distros. The appropriate location on most distros is `/etc/systemd/system`.

The username used here is `azerothuser`, and should be substituted for your username.

Since these commands won't be run with access to the user's variables, the install directory `$HOME/azerothcore` must be fully expanded to, for example, `/home/azerothuser/azerothcore`. Run `echo $HOME/azerothcore` as your user if you're not sure what this should be.

### authserver.service

```sh
[Unit]
Description=AzerothCore Authserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=azerothcore
WorkingDirectory=/home/azerothuser/azerothcore
ExecStart=/home/azerothuser/azerothcore/acore.sh run-authserver

[Install]
WantedBy=multi-user.target
```

### worldserver.service

```sh
[Unit]
Description=AzerothCore Worldserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=azerothcore
WorkingDirectory=/home/azerothuser/azerothcore
ExecStart=/bin/screen -S worldserver -D -m /home/azerothuser/azerothcore/acore.sh run-worldserver

[Install]
WantedBy=multi-user.target
```

systemd is made aware of these new service files with `systemd daemon-reload`. You can start AzerothCore like this:

```sh
sudo service worldserver start
sudo service authserver start
```

Or stop it:

```sh
sudo service worldserver stop
sudo service authserver stop
```

The servers can be set to automatically start when the system boots with:

```sh
sudo systemctl enable authserver
sudo systemctl enable worldserver
```

## Help

If you are still having problems, check:

* [FAQ](faq)

* [Common Errors](common-errors)

* [How to ask for help](how-to-ask-for-help)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](linux-requirements) | [Step 3: Server Setup >>](server-setup) |
