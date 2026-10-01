# Windows VSC 核心安装

{% include note.html content="本指南由社区制作。它可能不是最新的，也不受官方支持。" %}

| 安装指南 | |
| :- | :- |
| [<< 第 1 步：VSC 环境要求](vsc-requirements) | [第 3 步：服务器设置 >>](server-setup) |

## 所需软件

在继续之前请先阅读 [环境要求](requirements)。

## 拉取并编译源代码

### 拉取代码

1. 创建用于存放源文件的目录。在本指南中，我们将使用 **C:\Azerothcore**。

1. 右键点击该文件夹，选择 **GitExt Clone...**

1. 按如下方式填写数据：

```
Repository to clone: https://github.com/azerothcore/azerothcore-wotlk
Destination: C:\Azerothcore
Subdirectory to create: <none>*
Branch: master
Repository type: Personal repository
```

点击 **Clone**。几分钟内，Azerothcore 的源文件将被克隆到 **C:\Azerothcore**。

### 使用 CMake 配置并生成 Visual C++ 解决方案

在开始之前，创建一个名为 **Build** 的新目录。在本指南中，我们将使用 **C:\Build**。

1. 打开 CMake

1. 点击 **Browse Source...** → 选择源目录（**C:\Azerothcore**）

1. 点击 **Browse Build...** → 选择构建目录（**C:\Build**）

1. 点击 **Configure**。

1. 在下拉菜单中选择你在 [环境要求](windows-requirements) 部分下载的编译器版本。如果你进行的是 64 位编译，请务必选择 **Win64** 版本。

1. 确保 **Use default native compilers** 已勾选。

1. 点击 **Finish**。

1. 确保 **TOOLS** 已勾选。这将编译后续设置中所需的提取器（extractor）。

1. 再次点击 **Configure**。只要日志窗口中还有红色字体的错误，你就需要检查参数并重新运行。

1. 点击 **Generate**。这会将所选构建文件安装到你的 **C:\Build** 文件夹中。

#### 一些错误修复

- 如果 CMake 找不到 MySQL，则需要设置 **MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** 和 **MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**。

    - XX 取决于你使用的 MySQL 版本。

    - （如果你在 CMake 中看不到 MYSQL 字段，请勾选 Advanced 复选框）。

- 如果遇到链接器错误（例如"error LNK2019: unresolved external symbol mysql_server_init"），请确保 MYSQL_LIBRARY 设置为与你编译模式（x64 与 32 位）匹配的 libmysql.lib。

    - （如果你在 CMake 中看不到 MYSQL 字段，请勾选 Advanced 复选框）。

- 如果遇到 *CMake could NOT find OpenSSL* 的错误：

    - 勾选 **Advanced** 复选框。

    - 在列表中找到两个 OPENSSL 条目，并指向正确的目录：

        - OPENSSL_ROOT_DIR 是安装路径（默认为 **C:/OpenSSL-Win32** 或 **C:/OpenSSL-Win64**）

        - OPENSSL_INCLUDE_DIR 是安装路径中的"include"文件夹（默认为 **C:/OpenSSL-Win32/include** 或 **C:/OpenSSL-Win64/include**）

### 编译源代码

1. 在 Visual Studio Code 中打开包含 AC 源代码的目录。
1. 在底部菜单中点击 **all**（等待几秒），然后在顶部对话框中选择 **ALL_BUILD**。
1. 点击 **BUILD**

编译时间因机器而异，但预计需要 5 到 30 分钟。

构建完成后，你会在输出中看到类似这样的消息：

```
Build finished with exit code 0
```

你会在 **C:\Build\bin\Release** 或 **C:\Build\bin\Debug** 文件夹中找到刚编译好的二进制文件。在本教程的最后，它们都将用于运行你的服务器。

核心要正常运行，你需要以下文件：

```
\configs\
authserver.exe
authserver.pdb
worldserver.exe
worldserver.pdb
libmysql.dll
libeay32.dll / libcrypto-1_1.dll / libcrypto-1_1-x64.dll
ssleay32.dll / libssl-1_1.dll / libssl-1_1-x64.dll
```

在 **configs** 文件夹中，你应该找到：

```
authserver.conf.dist
worldserver.conf.dist
```

有三个 DLL 文件需要手动添加到该文件夹中，你需要从以下安装/bin 目录中复制它们：

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*注意：你需要与你下载的 MySQL 版本相对应的精确 libmysql 版本。因此，你不能从网上下载该 DLL，而必须从该文件夹中取出。*

OpenSSL 版本 _低于_ 1.1.0：

**libeay32.dll**
**ssleay32.dll** → C:\OpenSSL-Win64\ 或 C:\OpenSSL-Win32\ *（取决于你的核心是 64 位还是 32 位）*。

安装了 OpenSSL 1.1.0 及更新版本，名称已更改：

**libssl-1_1.dll**
**libcrypto-1_1.dll** → C:\OpenSSL-Win32\bin

**libssl-1_1-x64.dll**
**libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### 关于编译日志和报告

pdb 文件只有在你使用 Debug 或 RelWithDebInfo 模式编译时才会存在，这不是强制要求，但建议至少使用 RelWithDebInfo 模式编译核心，以获得正常的崩溃日志。如果你在 Release 模式下编译，则不需要 pdb 文件。

要报告崩溃日志，必须使用 Debug 或 RelWithDebInfo 模式编译。

| 安装指南 | |
| :- | :- |
| [<< 第 1 步：VSC 环境要求](vsc-requirements) | [第 3 步：服务器设置 >>](server-setup) |
