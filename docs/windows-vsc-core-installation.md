# Windows VSC Core Installation

| Installation Guide | |
| :- | :- |
| [<< Step 1: VSC Requirements](vsc-requirements) | [Step 3: Server Setup >>](server-setup) |

## Required software

See [Requirements](requirements) before you continue.

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

1. In the dropdown menu, choose the version of the compiler you downloaded in [Requirements](windows-requirements) section. Be sure to choose **Win64** version if you work on a 64-bit compilation.

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

### Compiling the Source

1. In Visual Studio Code open directory with AC source.
1. In the menu at the bottom, click **all** (wait a few seconds) and select **ALL_BUILD** on the top dialog.
1. click **BUILD** 

Build time differs from machine to machine, but you can expect it to take between 5 and 30 minutes.

When the build is complete you will find a message in the output that looks similar to this:

```
Build finished with exit code 0
```

You will find your freshly compiled binaries in the **C:\Build\bin\Release** or **C:\Build\bin\Debug** folder. These are all used to run your server at the end of this instruction.

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
```

In the **configs** folder you should find:

```
authserver.conf.dist
worldserver.conf.dist
```

There are three DLL files that need to be manually added to this folder, and you need to copy them from the following installation/bin directories:

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*Note: You need the exact version of libmysql to correspond to the MySQL you have downloaded. Due to this you cannot download the DLL from the web and need to take it out of the folder.*

OpenSLL _before_ version 1.1.0:

**libeay32.dll**
**ssleay32.dll** → C:\OpenSSL-Win64\ or C:\OpenSSL-Win32\ *(depends on if your core is 64-bit or 32-bit)*.

OpenSSL 1.1.0 and more recent installed, names have changed:

**libssl-1_1.dll**
**libcrypto-1_1.dll** → C:\OpenSSL-Win32\bin

**libssl-1_1-x64.dll**
**libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### About compilation log and report

pdb files only exist if you compile on Debug or RelWithDebInfo modes, it's not mandatory but it's recommended to compile core on at least RelWithDebInfo mode to get proper crashlogs. If you compile on Release mode the pdb files aren't needed.

To report crash logs it's MANDATORY to compile on Debug or RelWithDebInfo mode.

| Installation Guide | |
| :- | :- |
| [<< Step 1: VSC Requirements](vsc-requirements) | [Step 3: Server Setup >>](server-setup) |
