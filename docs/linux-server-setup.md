# Linux Server Setup

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |

## Extracting DBC, Maps, VMaps & MMaps

Go to your AzerothCore build directory (e.g. $HOME/build/bin/) and copy the following files to your World of Warcraft binaries directory.

* **mapextractor**
* **mmaps_generator**
* **vmap4assembler**
* **vmap4extractor**

**DBC and Maps files**

```
cd <your WoW client directory>
./mapextractor
```

**Visual Maps (aka vmaps) Note: If you stop vmap4extractor before finish you will need to delete the Buildings directory before start again.**

You can also extract vmaps which will take quite a while depending on your machine (up to hours on ancient hardware).

```
cd <your WoW client directory>
./vmap4extractor
mkdir vmaps;
./vmap4assembler Buildings vmaps
```

When this is complete you will receive the following message which can be safely ignored.

```
Processing Map 724
[################################################################]
Extracting GameObject models...Extracting World\Wmo\Band\Final_Stage.wmo
No such file.
Couldn't open RootWmo!!!
Done!
  
Extract V4.00 2012_02. Work complete. No errors.
```

**Movement Maps  (aka mmaps - optional RECOMMENDED)**

Extracting mmaps will take quite a while depending on your machine (up to hours).

```
cd <your WoW client directory>
mkdir mmaps;
./mmaps_generator
```

Now that everything is completed, you need to copy **dbc**, **maps**, **vmaps** and **mmaps** folders to your AzerothCore build directory (e.g. *$HOME/build/data/*).

## Setting up the configuration files

First of all you need to find the two default config files (named worldserver.conf.dist and authserver.conf.dist) and copy them. Then rename the copies their namesakes without the .dist extension. You can find them within /build/configs/ (may vary).

Open the .conf files and scroll down to LoginDatabaseInfo, WorldDatabaseInfo, and CharacterDatabaseInfo and enter MySQL login information for the server to be able to access your database.

On a newly compiled configuration, you will have the following values by default
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

They follow this structure:

```
Variablename = "MySQLIP;Port;Username;Password;database"  
``` 

<br>

## Help

If you are still having problems, check:

* [How to ask for help](How-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |