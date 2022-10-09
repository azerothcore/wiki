# Windows Core Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 1: Requirements](requirements.md) | [Step 3: Server Setup >>](server-setup.md) |

## Required software

See [Requirements](requirements.md) before you continue.

## Pulling & Compiling the source

### Pulling the code

1. Create the directory where the source files will be located. In this guide we will use **C:\Azerothcore**.

1. Right-click on the folder and select **GitExt Clone...**

1. Fill in the data as follow:

```
Repository to clone: https://github.com/azerothcore/azerothcore-wotlk
Destination: C:\Azerothcore
Subdirectory to create: <none>*
Branch: master
Repository type: Personal repository
```

Click **Clone**. Within a few minutes Azerothcore's sourcefiles will be cloned into **C:\Azerothcore**.

### Configuring and generating Visual C++ solution with CMake

Before you begin, create a new directory called **Build**. In this guide we will use **C:\Build**.

1. Open CMake

1. Click **Browse Source...** → Select the source directory (**C:\Azerothcore**)

1. Click **Browse Build...** → Select the build directory (**C:\Build**)

1. Click **Configure**.

1. In the dropdown menu, choose the version of the compiler you downloaded in [Requirements](windows-requirements.md) section. Be sure to choose **Win64** version if you work on a 64-bit compilation.

1. Make sure that **Use default native compilers** is checked.

1. Click **Finish**.

1. Make sure **TOOLS** is checked. This will compile the extractors needed later in the setup.

1. Click **Configure** again. As long as you have error(s) typed in red in the log window you will need to check your parameters and re-run it.

1. Click **Generate**. This will install the selected build files into your **C:\Build** folder.

#### Some error fixes

- If MySQL is not found by CMake it is required to set **MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** and **MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**.

    - XX depends on which MySQL version you use.
    
    - (If you do not see the MYSQL fields in CMake, tick the Advanced box).
    
- If you get linker errors (e.g "error LNK2019: unresolved external symbol mysql_server_init"), make sure MYSQL_LIBRARY is set to the libmysql.lib that matches your compile mode (x64 vs 32 bits).

    - (If you do not see the MYSQL fields in CMake, tick the Advanced box).

- If you get an error that *CMake could NOT find OpenSSL*:
    
    - Check the **Advanced** checkbox.
    
    - Find the two OPENSSL entries in the list and point to the correct directories:

        - OPENSSL_ROOT_DIR is the installation path (by default, **C:/OpenSSL-Win32** or **C:/OpenSSL-Win64**)
        
        - OPENSSL_INCLUDE_DIR is the "include" folder in installation path (by default, **C:/OpenSSL-Win32/include** or **C:/OpenSSL-Win64/include**)

- If you get an error that CMake *Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")

    - Locate your Boost folder

        - Run the Bootstrap.bat file

        - Run the b2.exe file 

### Compiling the Source

1. In CMake press **Open Project** to open the **AzerothCore.sln** file directly with Visual Studio.

1. In the menu at the top, click **Build** and select **Configuration Manager**.

1. Set **Active Solution Configuration** to **RelWithDebInfo**.

1. In the list menus below "Help", set **Active Solution Platform** to **x64** and then click Close (settings automatically save).

    1. If you set 32-bit compilation during CMake configuration, select **x86**.

1. Right-click **ALL_BUILD** in the Solution Explorer on the right sidebar and select **Clean**.
 
1. Right-click **ALL_BUILD** and select **Build**. (Ctrl + Shift + B)

    1. If your GUI does not show Solution Explorer, click the Build menu and select **Clean Solution** then **Build**.

Build time differs from machine to machine, but you can expect it to take between 5 and 30 minutes.

If you are asked to "Reload build files" during or after the compile, do so.

When the build is complete you will find a message in the output that looks similar to this:

```
========== Build: 22 succeeded, 0 failed, 0 up-to-date, 1 skipped ==========
```

You will find your freshly compiled binaries in the **C:\Build\bin\RelWithDebInfo** or **C:\Build\bin\Debug** folder. These are all used to run your server at the end of this instruction.

You will need the following files in order for the core to function properly:

```
\configs\
authserver.exe
authserver.pbd
worldserver.exe
worldserver.pdb
libmysql.dll
libeay32.dll / libcrypto-1_1.dll / libcrypto-1_1-x64.dll
ssleay32.dll / libssl-1_1.dll / libssl-1_1-x64.dll
legacy.dll
```

In the **configs** folder you should find:

```
authserver.conf.dist
worldserver.conf.dist
```

There are three DLL files that need to be manually added to this folder, and you need to copy them from the following installation/bin directories:

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*Note: You need the exact version of libmysql to correspond to the MySQL you have downloaded. Due to this you cannot download the DLL from the web and need to take it out of the folder.*

OpenSSL _before_ version 1.1.0:

**libeay32.dll** and
**ssleay32.dll** → C:\OpenSSL-Win64\ or C:\OpenSSL-Win32\ *(depends on if your core is 64-bit or 32-bit)*.

OpenSSL 1.1.0 and more recent installed, names have changed:

For 32-bit version:
**libssl-1_1.dll** and
**libcrypto-1_1.dll** → C:\OpenSSL-Win32\bin

For 64-bit version:
**libssl-1_1-x64.dll** and
**libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### About compilation log and report

pdb files only exist if you compile on Debug or RelWithDebInfo modes, it's not mandatory but it's recommended to compile core on at least RelWithDebInfo mode to get proper crashlogs. If you compile on Release mode the pdb files aren't needed.

To report crash logs it's MANDATORY to compile on Debug or RelWithDebInfo mode.

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
