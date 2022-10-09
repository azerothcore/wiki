# Instalación del Core en Linux

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 1: Requisitos](requirements.md) | [Paso 3: Instalación del Servidor >>](server-setup.md) |

## Software requerido

Véase [Requisitos](requirements.md) antes de continuar.

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

Esto creará un directorio de `azerothcore-wotlk` que contiene los archivos fuente de AC.

## Compilación del código fuente

### Creación del directorio de la build

To avoid issues with updates and colliding source builds, we create a specific build-directory, so we avoid any possible issues due to that (if any might occur)

```sh
cd azerothcore
mkdir build
cd build
```

### Configuring for compiling

Before running the CMake command, replace `$HOME/azeroth-server/` with the path of the server installation (where you want to place the compiled binaries).

Parameter explanation for advanced users [CMake options](cmake-options.md).

At this point, you must be in your "build/" directory.

**Note**: in the following command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root". You can check the state of the environment variable, as follows:

```sh
echo $HOME
```

**Note**: in case you use a non-default package for `clang`, you need to replace it accordingly. For example, if you installed `clang-6.0` then you have to replace `clang` with `clang-6.0` and `clang++` with `clang++-6.0`

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static
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

<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](requirements.md) | [Step 3: Server Setup >>](server-setup.md) |
