# Windows Server Setup

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |

## Extracting DBC, Maps, VMaps & MMaps

1. Browse into your build directory (**C:\Build\bin\RelWithDebInfo\\**) and copy the following files into your World of Warcraft folder (where the wow.exe is located).
```
mapextractor.exe
mmaps_generator.exe
vmap4extractor.exe
vmap4assembler.exe
```

2. Browse into **C:\Azerothcore\apps\extractor** and copy "**extractor.bat**" into your World of Warcraft folder with the previous files.

3. Create **mmaps** and **vmaps** folders in your World of Warcraft directory.

4. Launch extractor.bat and select your extractor options.

{{site.data.alerts.important}}
</br>

   - <b>dbc</b>, <b>maps</b> AND <b>vmaps</b> are needed to make server work properly!

   - Do not attempt to stop <b>vmaps</b> exctraction process. It is finished when it prints "Press any key...". It will create two new folders: <b>buildings</b> and <b>vmaps</b> The <b>buildings</b> folder is completely useless post-running and can be safely deleted.
    
   - Don't run another task before the first is finished or you will have errors.

   - If you stop vmap4extractor before finish you will need to delete the Buildings directory before start again.

   - <b>Optional but extremely recommended: Extract mmaps.</b> Do not attempt to stop this process while it is exctracting.
{{site.data.alerts.end}}

5. Create a new folder in <b>C:\Build\bin\RelWithDebInfo</b> called <b>Data</b>

6. Move the vmaps, maps, dbc, cameras into the <b>Data</b> folder.

## Setting up the configuration files

First of all you need to find the two default config files (named worldserver.conf.dist and authserver.conf.dist) and copy them. Then rename the copies their namesakes without the .dist extension. You can find them within /build/bin/configs/ (may vary).

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

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |
