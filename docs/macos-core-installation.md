# macOS Core Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](macos-requirements.md) | [Step 3: Server Setup >>](server-setup.md) |

## Required software

See [Requirements](macos-requirements.md) before you continue.

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

The directories Homebrew uses to install packages differs between Macs that have Apple Silicon CPUs and those that have Intel CPUs. Make sure to run the correct CMake command for your machine. You can view your CPU type in `About This Mac`. The commands below are labeled for the relevant CPU type.

Before running the CMake command, replace `$HOME/azeroth-server/` with the path of the server installation (where you want to place the compiled binaries).

Parameter explanation for advanced users [CMake options](cmake-options.md).

At this point, you must be in your "build/" directory.

**Note**: in the follows command the variable `$HOME` is the path of the **current user**, so if you are logged as root, $HOME will be "/root".

For APPLE SILICON CPUs:
```sh
export OPENSSL_ROOT_DIR=$(brew --prefix openssl@3)
cmake ../ \
-DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/  \
-DTOOLS_BUILD=all \
-DSCRIPTS=static \
-DMYSQL_ADD_INCLUDE_PATH=/opt/homebrew/include/mysql \
-DMYSQL_LIBRARY=/opt/homebrew/lib/libmysqlclient.dylib \
-DREADLINE_INCLUDE_DIR=/opt/homebrew/opt/readline/include \
-DREADLINE_LIBRARY=/opt/homebrew/opt/readline/lib/libreadline.dylib \
-DOPENSSL_INCLUDE_DIR="$OPENSSL_ROOT_DIR/include" \
-DOPENSSL_SSL_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libssl.dylib" \
-DOPENSSL_CRYPTO_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libcrypto.dylib"
```

For INTEL CPUs:
```sh
export OPENSSL_ROOT_DIR=$(brew --prefix openssl@3)
cmake ../ \
-DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/  \
-DTOOLS_BUILD=all \
-DSCRIPTS=static \
-DMYSQL_ADD_INCLUDE_PATH=/usr/local/include/mysql \
-DMYSQL_LIBRARY=/usr/local/opt/mysql/lib/libmysqlclient.dylib \
-DREADLINE_INCLUDE_DIR=/usr/local/opt/readline/include \
-DREADLINE_LIBRARY=/usr/local/opt/readline/lib/libreadline.dylib \
-DOPENSSL_INCLUDE_DIR="$OPENSSL_ROOT_DIR/include" \
-DOPENSSL_SSL_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libssl.dylib" \
-DOPENSSL_CRYPTO_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libcrypto.dylib"
```
Then, to build and install:

```sh
make -j `nproc`
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
| [<< Step 1: Requirements](macos-requirements.md) | [Step 3: Server Setup >>](server-setup.md) |
