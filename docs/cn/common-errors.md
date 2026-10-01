---
tableofcontents: 1
---

# 常见错误（Common Errors）

| 这份 FAQ 没有解决你的问题？请阅读[如何求助](how-to-ask-for-help)，了解以最佳方式提出问题的做法。 |
| --------------------------------------------------------------------------------------------------------------------------------------------- |

## 数据库相关错误

#### ACE00001
我无法启动 Auth/WorldServer，出现以下错误：
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
这只是说明你的数据库没有更新，你需要[更新你的数据库](database-keeping-the-server-up-to-date)。

---------------------------------------------------------

#### ACE00002
我无法启动 Auth/WorldServer，出现以下错误：
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
这可能由很多不同的原因造成，可能是你的数据库没有在线、你输入了错误的凭据，或者数据库结构有问题。

你需要在 Worldserver.conf 中启用 SQLDriverLogFile，以获得关于问题所在的准确报告。

要做到这一点，请取消注释 Logger.sql.driver，然后重新运行 WorldServer。

---------------------------------------------------------

#### ACE00003
我无法启动 Auth/WorldServer，出现以下错误：
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
这是因为你根本没有导入数据库。请按照[数据库安装](database-installation)中的说明操作。

---------------------------------------------------------

#### ACE00004
我无法启动 Auth/WorldServer，出现以下错误：
```
Unknown column 'level' in 'field list'

Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
这可能意味着以下几种情况：

1. 你更新了数据库，但忘了通过重新编译来更新你的二进制文件。
2. 你更新了二进制文件，但忘了更新你的数据库。
3. 你尝试使用自定义补丁或模块，但忘了更新你的数据库。
4. 你尝试使用来自其他项目的 SQL 补丁。

## 核心相关错误

#### ACE00040
核心无法启动，出现以下错误：
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
你需要从与服务器相同且未经修改的客户端版本中提取 DBC 文件，即 3.3.5a。

---------------------------------------------------------

#### ACE00041
核心无法启动，一打开就立即关闭。

请使用命令行启动服务器以获取确切的错误信息。

---------------------------------------------------------

#### ACE00042
核心无法启动，出现这个错误窗口。

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
你没有把必要的 .dll 文件复制到二进制目录中。参见[核心安装](core-installation)。

---------------------------------------------------------

#### ACE00043
核心无法启动，出现以下错误：
```
AzerothCore does not support MySQL versions below 8.0
```
请升级你的 MySQL。

注意：AzerothCore 不支持 MariaDB。

---------------------------------------------------------

#### ACE00044
出现以下错误：
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
你可以忽略它。这是我们无法隐藏的错误。

---------------------------------------------------------

#### ACE00045
当 WorldServer 运行时出现错误：
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
拉取源码，重新编译工具，将提取器复制到你的 WoW 二进制目录，并使用更新后的 mapextractor 重新创建地图。然后用新地图文件替换你的旧地图文件。

---------------------------------------------------------

#### ACE00046
当 WorldServer 启动时出现错误：
```
Used MySQL library version (8.0.19 id 80019) does not match the version id used to compile AzerothCore (id 80024)
```
你需要使用与编译源码时完全相同的 libmysql.dll 版本。你可以从 **C:\Program Files\MySQL\MySQL Server 8.x\lib\** 获取，或按照[安装指南](windows-core-installation#compiling-the-source)操作。

这是因为你更新了 MySQL 服务器，但没有重新编译并添加新的 libmysql.dll 文件。

---------------------------------------------------------

#### ACE00047
当我尝试启动 Worldserver 或 Authserver 时出现错误
```
This application was unable to start correctly (0xc000007b). Click OK to close the application.
```
这通常是由于将 32/64 位 DLL 与你编译的二进制文件混用造成的。你的 DLL 需要与编译的二进制文件保持相同的位数。

---------------------------------------------------------

#### ACE00048
当我尝试启动 Worldserver 或 Authserver 时出现错误
```
{}DatabaseInfo is not specified in configuration file!

{} = World/Character/Auth
```
这意味着 .conf 文件中缺少数据库连接信息。

请转到 .conf 中指定的 DatabaseInfo 并添加连接信息。

---------------------------------------------------------

## 核心编译相关错误

#### ACE00060
我没有得到 AzerothCore 的哈希值

请重新安装 Git for Windows，并在询问是否调整 PATH 时选择 "Git from the command line and also 3rd party software"。

---------------------------------------------------------

#### ACE00061
我无法在 CentOS/Ubuntu/Debian 等系统上安装 AzerothCore。

你的发行版可能太旧，无法提供受支持的编译器。Ubuntu 22.04 及更早版本已不再受支持：请使用 Ubuntu 24.04 或 26.04，或 Debian 12/13。请参阅[受支持的版本](https://github.com/azerothcore/azerothcore-wotlk/security/policy)了解确切的 GCC 和 CLang 要求。

---------------------------------------------------------

#### ACE00062
我无法在 Windows XP/Vista/7 上安装 AzerothCore

AzerothCore 需要 [Visual Studio 2022](https://docs.microsoft.com/en-us/visualstudio/releases/2022/system-requirements)，因此你需要更新到 Windows 10 或更高版本。

---------------------------------------------------------

#### ACE00063
我无法在 Linux 上安装 AzerothCore，出现以下错误：
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
这可能是因为：
1. 启用 SELinux 强化模式的内核，解决方法：改用标准内核，用 clang 代替 gcc 编译，或不用 pch 编译。
2. 内存/交换空间不足，请增加。

---------------------------------------------------------

#### ACE00064
我该如何在我的操作系统上 \<插入问题\>。

请使用谷歌搜索或购买一本书来学习你正在使用的操作系统。

---------------------------------------------------------

#### ACE00065
我无法编译，出现以下错误：
```
fatal error C1060: compiler is out of heap space
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
请阅读[如何：在命令行启用 64 位、x64 托管的 MSVC 工具集。Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160)。

---------------------------------------------------------

#### ACE00066
我无法编译，出现以下错误：
```
C1001: An internal error has occurred in the compiler.
```
请更新你的 Visual Studio。

---------------------------------------------------------

#### ACE00067
我无法生成 CMake 文件，出现以下错误：
```
Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")
```

请确保你安装的版本受支持。

如果你没有下载预编译的 boost，请找到你的 Boost 文件夹
1. 运行 Bootstrap.bat 文件
1. 运行 b2.exe 文件

---------------------------------------------------------

#### ACE00068
我无法在 Ubuntu 26.04 上生成 CMake 文件，出现以下错误：
```
The C++ compiler "/usr/bin/clang++" is not able to compile a simple test program.
/usr/bin/x86_64-linux-gnu-ld.bfd: cannot find -lstdc++: No such file or directory
```

Clang 链接到 GCC 工具链，而在 Ubuntu 26.04 上，clang 21 会选择 GCC 16，而默认的 `g++` 是 GCC 15，因此它需要的 C++ 开发文件没有安装。请安装它们：

```sh
sudo apt-get install -y libstdc++-16-dev
```

如果 clang 选择了其他版本，请运行 `clang++ -v` 并安装与输出中 `Selected GCC installation` 一行匹配的 `libstdc++-<version>-dev`。

## 提取器相关错误

#### ACE00080
我在寻找地图提取器，但它们是为 wow 4 版本准备的。

不，它们不是。"vmap4extractor"/"vmap4Assembler" 这个名字反映的是工具自身的版本。它们都适用于 WoW 3.3.5a。

---------------------------------------------------------

#### ACE00081
运行提取器时出现 Couldn't open RootWmo。

这不是错误，请忽略它。

---------------------------------------------------------

#### ACE00082
我无法使用 Vmap 提取器。

请先提取地图。

---------------------------------------------------------

#### ACE00083
我有来自 ManGOS 或 TrinityCore 的地图，可以使用它们吗？

不能。

## 核心安装错误

#### ACE00100
如果 CMake 找不到 MySQL，则需要设置

**MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** 以及

**MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**。

- X.X 取决于你使用的 MySQL 版本。
    
- （如果在 CMake 中看不到 MYSQL 字段，请勾选 Advanced 复选框）。

---------------------------------------------------------

#### ACE00101
如果你遇到链接器错误（例如 "error LNK2019: unresolved external symbol mysql_server_init"），请确保 MYSQL_LIBRARY 设置为与你编译模式匹配的 libmysql.lib。

- （如果在 CMake 中看不到 MYSQL 字段，请勾选 Advanced 复选框）。

---------------------------------------------------------

#### ACE00102
如果你遇到 *CMake 找不到 OpenSSL* 的错误

- 勾选 **Advanced** 复选框。

- 在列表中找到两个 OpenSSL 条目并指向正确的目录：

    - OPENSSL_ROOT_DIR 是安装路径（默认情况下，**C:/OpenSSL-Win32** 或 **C:/OpenSSL-Win64**）

    - OPENSSL_INCLUDE_DIR 是安装路径中的 "include" 文件夹（默认情况下，**C:/OpenSSL-Win32/include** 或 **C:/OpenSSL-Win64/include**）

---------------------------------------------------------

#### ACE00103
- 如果你遇到 CMake *找不到 Boost（缺少：system filesystem program_options iostreams regex）（找到合适的版本 "1.74.0"，最低要求 "1.70"）* 的错误

    - 找到你的 Boost 文件夹

        - 运行 Bootstrap.bat 文件

        - 运行 b2.exe 文件

---------------------------------------------------------

#### ACE00104
- 如果你遇到 *系统上未找到 Git* 的错误：

    - 勾选 **Advanced** 复选框。

    - 搜索并找到 **GIT_EXECUTABLE**
    
        - 指定 git.exe 的路径，例如 `C:/Program Files/Git/cmd/git.exe`
        
    - 如果你没有 git.exe，则需要安装 git。参见[要求](requirements)

---------------------------------------------------------

#### ACE00105
- 如果你遇到类似 **fatal: early EOF** 或 **fatal: fetch-pack: invalid index-pack output** 的错误
  - 尝试更新并重启你的 Github Desktop。
  - 考虑使用 Git Bash
    - 运行 Git Bash
    - 运行 `cd "D:/Path/To/Your/Dir/"`
    - 运行 `git clone https://github.com/azerothcore/azerothcore-wotlk.git`
    - 你的仓库现在将位于 `D:/Path/To/Your/Dir/azerothcore-wotlk`

---------------------------------------------------------

| 这份 FAQ 没有解决你的问题？请阅读[如何求助](how-to-ask-for-help)，了解以最佳方式提出问题的做法。 |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
