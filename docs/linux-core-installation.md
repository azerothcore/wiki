# Linux Core Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](requirements.md) | [Step 3: Server Setup >>](server-setup.md) |

## Required software

See [Requirements](requirements.md) before you continue.

## Getting the source code

Choose **ONE** of the following method, run one of the below `git ...` commands in your terminal.


1. Clone only the master branch + full history (smaller size - recommended):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
    ```

1. Clone only the master branch + no previous history (smallest size):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
    ```

    Note: If you want to get the full history back, use `git fetch --unshallow`.

1. Clone all branches and all history:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
    ```

This will create an `azerothcore-wotlk` directory containing the AC source files.

## Compiling the source code

### Creating the build-directory

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

**Note**: in case you use a non-default package for `clang` (such as not from a package manager), you may need to replace the binary name accordingly with the path of where your clang and clang++. This is usually not necessary as long as  you installed from a package manager as they symlink the binary names with the common paths.

```sh
cmake ../ \
-DCMAKE_INSTALL_PREFIX=$(dirname "$(pwd)") \
-DCMAKE_C_COMPILER=$(which clang) \
-DCMAKE_CXX_COMPILER=$(which clang++) \
-DWITH_WARNINGS=1 \
-DTOOLS=1 \
-DSCRIPTS=static
```

To know the amount of cores available.
You can use the following command

```sh
nproc --all
```

Then you can simply run this to compile with all threads available and install the server.

```sh
make -j$(nproc --all)
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
