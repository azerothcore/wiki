# Linux Core Installation

| Installation Guide                                                                                                                   |                                               |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 1: Requirements](linux-requirements)                                                                                        | [Step 3: Server Setup >>](linux-server-setup) |

## Installation directories

The following steps will install AzerothCore at `$AC_CODE_DIR`. This will by default be in `$HOME/azerothcore`. This path can be changed to any other location the user has access to if desired.

The user `azerothuser` will be used in some examples as well. Again, this can be changed to whatever is desired.

**Note**: in the following command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root". You can check the state of the environment variable, as follows:

```sh
echo $HOME
```

Configure the install directory as follows:

```sh
export AC_CODE_DIR=$HOME/azerothcore
```

## Required software

See [Requirements](linux-requirements) before you continue.

## Getting the source code

Choose **ONE** of the following method, run one of the below `git ...` commands in your terminal.


1. Clone only the master branch + full history (smaller size - recommended):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR
    ```

1. Clone only the master branch + no previous history (smallest size):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR --depth 1
    ```

    Note: If you want to get the full history back, use `git fetch --unshallow`.

1. Clone all branches and all history:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git $AC_CODE_DIR
    ```

This will create an `azerothcore` directory in your home folder containing the AC source files.

## Compiling the source code

### Creating the build-directory

To avoid issues with updates and colliding source builds, we create a specific build-directory, so we avoid any possible issues due to that (if any might occur)

```sh
cd $AC_CODE_DIR
mkdir build
cd build
```

### Configuring for compiling

Parameter explanation for advanced users [CMake options](cmake-options).

At this point, you must be in your `$AC_CODE_DIR/build` directory.


**Note**: in case you use a non-default package for `clang`, you need to replace it accordingly. For example, if you installed `clang-6.0` then you have to replace `clang` with `clang-6.0` and `clang++` with `clang++-6.0`

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static
```

To know the amount of cores available.
You can use the following command

```sh
nproc --all
```

Set the number of cores to build with, replacing the command with the number of threads you want to execute, if applicable:

```sh
export BUILD_CORES=`nproc | awk '{print $1 - 1}'`
```

Then, type:

```sh
make -j$BUILD_CORES
make install
```

It may be useful to preserve these commands in a script or otherwise keep note of them for later. You will need to re-run all three commands again whenever you update AzerothCore or add new modules. For example:

```sh
#!/bin/bash

BUILD_CORES=`nproc | awk '{print $1 - 1}'`
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static &&
make -j$BUILD_CORES &&
make install
```

## (Optional) Systemd Services

Systemd services can help you with managing your AzerothCore server. The service files shown below must be installed by `root` in most distros. The appropriate location on most distros is `/etc/systemd/system`.

Since these commands won't be run with access to the user's variables, the install directory `$AC_CODE_DIR` must be fully expanded to, for example, `/home/azerothuser/azerothcore`. Run `echo $AC_CODE_DIR` as your user if you're not sure what this should be.

Set the user for the units to run as. The username used here is `azerothuser`, and should be substituted for your username.
```sh
export AC_UNIT_USER=azerothuser
```

### ac-authserver.service

```sh
sudo tee /etc/systemd/system/ac-authserver.service << EOF
[Unit]
Description=AzerothCore Authserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=$AC_CODE_DIR/acore.sh run-authserver

[Install]
WantedBy=multi-user.target
EOF
```

### ac-worldserver.service

```sh
sudo tee /etc/systemd/system/ac-worldserver.service << EOF
[Unit]
Description=AzerothCore Worldserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=/bin/screen -S worldserver -D -m $AC_CODE_DIR/acore.sh run-worldserver

[Install]
WantedBy=multi-user.target
EOF
```

systemd is made aware of these new service files with `systemd daemon-reload`. You can start AzerothCore like this:

```sh
sudo service ac-worldserver start
sudo service ac-authserver start
```

Or stop it:

```sh
sudo service ac-worldserver stop
sudo service ac-authserver stop
```

The servers can be set to automatically start when the system boots with:

```sh
sudo systemctl enable ac-authserver
sudo systemctl enable ac-worldserver
```

You can inspect if the services started properly by inspecting the log entries from the systemd journal like so:

```sh
sudo journalctl authserver.service
sudo journalctl worldserver.service
```

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                               |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 1: Requirements](linux-requirements)                                                                                        | [Step 3: Server Setup >>](linux-server-setup) |
