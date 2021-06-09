# Common Errors

| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |

## Database-related errors

**ACE00001** I can't start my Auth/WorldServer, I get:
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
You are simply not updated and you need to [Update your database](database-keeping-the-server-up-to-date.md).

**ACE00002** I can't start my Auth/WorldServer, I get:
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
This can mean a lot of different things, either your database might not be online, you have entered the wrong credentials or the database structure is wrong.

You need to enable the SQLDriverLogFile in Worldserver.conf to get an accurate report on what is wrong.

To do this, uncomment Logger.sql.driver and then run the WorldServer again.

**ACE00003** I can't start my Auth/WorldServer, I get:
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
This is because you have not imported the Database at all. Follow the instructions in [Database Installation](database-installation.md)

**ACE00004** I can't start my Auth/WorldServer, I get:
```
Unknown column 'level' in 'field list'

Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
This can mean several things:

1. You have updated your database but forgot to update your binaries by recompiling.
2. You have updated your binaries but have forgot to update your database.
3. You are trying to use a custom patch or module but have forgotten to update your database.
4. You are trying to use an SQL patch from another project.

## Database Update-related errors

**ACE00020** My DB Assambler closes and does not import all updates, I get:
```
ERROR 1054 (42522) at line 14062: Unknown column 'resistance2' in 'field list'
```
This error is because you have manually changed the database structure and is conflicting with updates.

The easiest way to fix it is by dropping your database and importing it again.

**ACE0021** My DB Assambler closes and does not import all updates, I get:

This can be due to several reasons:

1. You have the wrong credentials set up for the DB Assambler.
2. Your Database structure has been modified manually and is conflicting with the updates. Fix this by dropping the database.

**ACE00022** My DB Assambler closes and does not import all updates, I get:
```
ERROR 1067 (42000) at line 181: Invalid default value for 'start_time'.
```
Disable MySQL strict mode, read [How to turn on/off MySQL strict mode in localhost (xampp)? StackOverflow](https://stackoverflow.com/questions/40881773/how-to-turn-on-off-mysql-strict-mode-in-localhost-xampp).

## Core-related Errors

**ACE00040** Core doesn't start, I get:
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
You need to extract the DBC files from the same unmodified client version as your server is. i.e 3.3.5a.

**ACE00041** Core doesn't start, it closes as soon as I open it.

Start the server using command prompt to get the exact error.

**ACE00042** Core doesn't start, I get this error window.

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
You have not copied the necessary .dll files into the binaries directory.

**ACE00043** Core doesn't start, I get:
```
AzerothCore does not support MySQL versions below 5.7
```
Upgrade your MySQL.

**ACE00044** I get:
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
You can ignore it. It's an error we cannot hide.

**ACE00045** I get an error when the WorldServer is running:
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
Pull the source, recompile tools, copy the extractors to your wow binaries and recreate the maps using the updated mapextractor. Then replace your old map files with the new ones.

## Core compilation-related errors

**ACE00060** I don't get a AzerothCore hash

Read how to properly install Git for Windows.

**ACE00061** I cannot install AzerothCore on CentOS/Ubtuntu/Debian etc.

AzerothCore requires GCC 8.0 or higher and CLang 7 or higher.

**ACE00062** I cannot install AzerothCore on Windows XP/Vista

AzerothCore requires [Visual Studio 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/system-requirements), therefore you need to update to Windows 7 or above.

**ACE00063** I cannot install AzerothCore on Linuyx, I get:
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
This can be due to:
1. Selinux stronged kernels, workaround: change to one standard kernel, compile with clang instad of gcc or compile without pch.
2. Low ram/swap memory, increase it.

**ACE00064** How do I \<insert question\> on my operating system.

Use google or buy a book to learn the operating system you are using.

**ACE00065** I can't copmile, I get:
```
fatal error C1060: compiler is out of heap space
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
Read [How to: Enable a 64-Bit, x664 hosted MSVC toolset on the command line. Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160).

**ACE00066** I can't compile, I get:
```
C1001: An internal error has occurred in the compiler.
```
Update your Visual Studio.

## Extractor-related errors

**ACE00080** I am looking for map extractors but they are for wow version 4.

No they are not. The name "vmap4extractor"/"vmap4assambler" reflects the version of the tool. They are all for WoW 3.3.5a.

**ACE00081** Couldn't open RootWmo while running extractor.

Not an error, ignore it.

**ACE00082** I can't use Vmap extractor.

Extract maps first.

**ACE00083** I have maps from ManGOS or TrinityCore, can I use them?

No.
















| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |