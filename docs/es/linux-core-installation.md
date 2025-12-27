# Instalación del Core en Linux

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 1: Requisitos](linux-requirements) | [Paso 3: Instalación del Servidor >>](server-setup) |

## Software requerido

Véase [Requisitos](linux-requirements) antes de continuar.

## Obtener el código fuente

Elija **UNO** de los siguientes metodos, ejecute uno de los siguientes comandos `git ...` en su terminal.


1. Clonar solo la rama master + el historial completo (Menor tamaño - recomendado):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
    ```

1. Clonar solo la rama master sin historial previo (el menor tamaño):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
    ```

    Nota: si usted quiere obtener el historial completo, use `git fetch --unshallow`.

1. Clonar todas las ramas y todo el historial:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
    ```

Esto creará un directorio de `azerothcore` que contiene los archivos fuente de AC.

## Compilación del código fuente

### Creación del directorio de la build

**Note**: in the following command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root". You can check the state of the environment variable, as follows:

```sh
echo $HOME
```

Configure the install directory as follows:

```sh
export AC_CODE_DIR=$HOME/azerothcore
```

To avoid issues with updates and colliding source builds, we create a specific build-directory, so we avoid any possible issues due to that (if any might occur)

```sh
cd $AC_CODE_DIR
mkdir build
cd build
```

### Configuring for compiling

Parameter explanation for advanced users [CMake options](cmake-options).

At this point, you must be in your "build/" directory.

**Note**: in the following command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root". You can check the state of the environment variable, as follows:

```sh
echo $HOME
```

**Note**: in case you use a non-default package for `clang`, you need to replace it accordingly. For example, if you installed `clang-6.0` then you have to replace `clang` with `clang-6.0` and `clang++` with `clang++-6.0`

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static
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
sudo journalctl ac-authserver.service
sudo journalctl ac-worldserver.service
```

## Help

If you are still having problems, check:

* [FAQ](faq)

* [Common Errors](common-errors)

* [How to ask for help](how-to-ask-for-help)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 1: Requirements](linux-requirements) | [Step 3: Server Setup >>](server-setup) |
