# Common Errors

| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |

## Database-related errors

#### [ACE00001](#ace00001)
I can't start my Auth/WorldServer, I get:
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
You are simply not updated and you need to [Update your database](database-keeping-the-server-up-to-date.md).

---------------------------------------------------------

#### [ACE00002](#ace00002)
I can't start my Auth/WorldServer, I get:
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
This can mean a lot of different things, either your database might not be online, you have entered the wrong credentials or the database structure is wrong.

You need to enable the SQLDriverLogFile in Worldserver.conf to get an accurate report on what is wrong.

To do this, uncomment Logger.sql.driver and then run the WorldServer again.

---------------------------------------------------------

#### [ACE00003](#ace00003)
I can't start my Auth/WorldServer, I get:
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
This is because you have not imported the Database at all. Follow the instructions in [Database Installation](database-installation.md)

---------------------------------------------------------

#### [ACE00004](#ace00004)
I can't start my Auth/WorldServer, I get:
```
Unknown column 'level' in 'field list'

Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
This can mean several things:

1. You have updated your database but forgot to update your binaries by recompiling.
2. You have updated your binaries but have forgot to update your database.
3. You are trying to use a custom patch or module but have forgotten to update your database.
4. You are trying to use an SQL patch from another project.

---------------------------------------------------------

## Database Update-related errors

#### [ACE00020](#ace00020)
My DB Assembler closes and does not import all updates, I get:
```
ERROR 1054 (42522) at line 14062: Unknown column 'resistance2' in 'field list'
```
This error is because you have manually changed the database structure and is conflicting with updates.

The easiest way to fix it is by dropping your database and importing it again.

---------------------------------------------------------

#### [ACE0021](#ace0021)
My DB Assembler closes and does not import all updates, I get:

This can be due to several reasons:

1. You have the wrong credentials set up for the DB Assembler.
2. Your Database structure has been modified manually and is conflicting with the updates. Fix this by dropping the database.

---------------------------------------------------------

#### [ACE00022](#ace00022)
 My DB Assembler closes and does not import all updates, I get:
```
ERROR 1067 (42000) at line 181: Invalid default value for 'start_time'.
```
Disable MySQL strict mode, read [How to turn on/off MySQL strict mode in localhost (xampp)? StackOverflow](https://stackoverflow.com/questions/40881773/how-to-turn-on-off-mysql-strict-mode-in-localhost-xampp).

------------------------------------------------------------------------------------------------------------------

#### [ACE00023](#ace00023)
My Worldserver closes when autoupdater, I get:
```
ERROR 2013 (HY000) at line 4: Lost connection to MySQL server during query
```
This is most likely due to your MySQL server's max_allowed_packet setting is too low. See [this](https://docs.oracle.com/cd/E19509-01/820-6323/gicxk/index.html) or run the command `SET GLOBAL max_allowed_packet=1073741824;` in your SQL client (HeidiSQL, SQLyog, etc.) to update your max_allowed_packet.

**This value will reset the next time your SQL server restarts and it may be necessary to run this query again in the future.** 

## Core-related Errors

#### [ACE00040](#ace00040)
Core doesn't start, I get:
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
You need to extract the DBC files from the same unmodified client version as your server is. i.e 3.3.5a.

---------------------------------------------------------

#### [ACE00041](#ace00041)
Core doesn't start, it closes as soon as I open it.

Start the server using command prompt to get the exact error.

---------------------------------------------------------

#### [ACE00042](#ace00042)
Core doesn't start, I get this error window.

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
You have not copied the necessary .dll files into the binaries directory.

---------------------------------------------------------

#### [ACE00043](#ace00043)
Core doesn't start, I get:
```
AzerothCore does not support MySQL versions below 5.7 and MariaDB versions below 10.5
```
Upgrade your MySQL/MariaDB.

---------------------------------------------------------

#### [ACE00044](#ace00044)
I get:
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
You can ignore it. It's an error we cannot hide.

---------------------------------------------------------

#### [ACE00045](#ace00045)
I get an error when the WorldServer is running:
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
Pull the source, recompile tools, copy the extractors to your wow binaries and recreate the maps using the updated mapextractor. Then repl#ace your old map files with the new ones.

---------------------------------------------------------

#### [ACE00046](#ace00046)
I get an error when WorldServer is starting:
```
Used MySQL library version (8.0.19 id 80019) does not match the version id used to compile AzerothCore (id 80024)
```` 
You need to use the exact version of libmysql.dll as the version you used to compile your source with. You get it from **C:\Program Files\MySQL\MySQL Server 8.x\lib\\** or by following the [installation guide](https://www.azerothcore.org/wiki/windows-core-installation#compiling-the-source).

This is due to that you have updated your MySQL server but have not recompiled and added the new libmysql.dll file.

---------------------------------------------------------

#### [ACE00047](#ace00047)
I get an error when I am trying to start Worldserver or Authserver
```
This application was unable to start correctly (0xc000007b). Click OK to close the application.
```
This is usually due to mixing 32/64bit DLLs with your compiled binaries. Your DLLs needs to be the same bit version as your compiled binaries.

---------------------------------------------------------

## Core compilation-related errors

#### [ACE00060](#ace00060)
I don't get an AzerothCore hash

Reinstall Git for Windows and select "Git from the command line and also 3rd party software" when asked about adjusting your PATH.

---------------------------------------------------------

#### [ACE00061](#ace00061)
I cannot install AzerothCore on CentOS/Ubuntu/Debian etc.

AzerothCore requires GCC 8.0 or higher and CLang 7 or higher.

---------------------------------------------------------

#### [ACE00062](#ace00062)
I cannot install AzerothCore on Windows XP/Vista

AzerothCore requires [Visual Studio 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/system-requirements), therefore you need to update to Windows 7 or above.

---------------------------------------------------------

#### [ACE00063](#ace00063)
I cannot install AzerothCore on Linuyx, I get:
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
This can be due to:
1. SELinux stronged kernels, workaround: change to one standard kernel, compile with clang instead of gcc or compile without pch.
2. Low ram/swap memory, increase it.

---------------------------------------------------------

#### [ACE00064](#ace00064)
How do I \<insert question\> on my operating system.

Use google or buy a book to learn the operating system you are using.

---------------------------------------------------------

#### [ACE00065](#ace00065)
I can't compile, I get:
```
fatal error C1060: compiler is out of heap sp#ace
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
Read [How to: Enable a 64-Bit, x64 hosted MSVC toolset on the command line. Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160).

---------------------------------------------------------

#### [ACE00066](#ace00066)
I can't compile, I get:
```
C1001: An internal error has occurred in the compiler.
```
Update your Visual Studio.

---------------------------------------------------------

#### [ACE00067](#ace00067)
I can't generate my CMake files, I get:
```
Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")
```
Locate your Boost folder
1. Run the Bootstrap.bat file
1. Run the b2.exe file 

## Extractor-related errors

#### [ACE00080](#ace00080)
I am looking for map extractors but they are for wow version 4.

No they are not. The name "vmap4extractor"/"vmap4Assembler" reflects the version of the tool. They are all for WoW 3.3.5a.

---------------------------------------------------------

#### [ACE00081](#ace00081)
Couldn't open RootWmo while running extractor.

Not an error, ignore it.

---------------------------------------------------------

#### [ACE00082](#ace00082)
I can't use Vmap extractor.

Extract maps first.

---------------------------------------------------------

#### [ACE00083](#ace00083)
I have maps from ManGOS or TrinityCore, can I use them?

No.

| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |
