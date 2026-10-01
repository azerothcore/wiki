# macOS 核心安装

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 1 步：环境要求](macos-requirements)                                                                                           | [第 3 步：服务器设置 >>](macos-server-setup)                 |

## 所需软件

继续之前请先阅读[环境要求](macos-requirements)。

## 获取源代码

选择以下方法中的**一种**，在你的终端中运行下面的其中一个 `git ...` 命令。

1. 仅克隆 master 分支 + 完整历史（体积较小 - 推荐）：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
    ```

1. 仅克隆 master 分支 + 无历史记录（体积最小）：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
    ```

    注意：如果你想要恢复完整历史，请使用 `git fetch --unshallow`。

1. 克隆所有分支和所有历史：

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
    ```

这将创建一个包含 AC 源文件的 `azerothcore-wotlk` 目录。

## 编译源代码

### 创建构建目录

为了避免更新和源码构建冲突带来的问题，我们创建一个专用的构建目录，以规避可能出现的任何问题（如果会发生的话）。

```sh
cd azerothcore
mkdir build
cd build
```

### 配置编译 {#configuring-for-compiling}

Homebrew 用于安装软件包的目录在搭载 Apple Silicon CPU 的 Mac 和搭载 Intel CPU 的 Mac 上有所不同。请确保为你的机器运行正确的 CMake 命令。你可以在「关于本机」中查看你的 CPU 类型。下面的命令已针对相应的 CPU 类型做了标注。

在运行 CMake 命令之前，请将 `$HOME/azeroth-server/` 替换为服务器安装路径（即你想要放置编译后二进制文件的位置）。

高级用户的参数说明请参考 [CMake 选项](cmake-options)。

此时，你必须位于你的 "build/" 目录中。

**注意**：在下面的命令中，变量 `$HOME` 是**当前用户**的路径，因此如果你以 root 身份登录，$HOME 将是 "/root"。

针对 APPLE SILICON CPU：
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

针对 INTEL CPU：
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
然后，进行构建和安装：

```sh
make -j `nproc`
make install
```

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 1 步：环境要求](macos-requirements)                                                                                           | [第 3 步：服务器设置 >>](macos-server-setup)                 |
