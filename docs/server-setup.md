# Server Setup

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |

Now that you have the source compiled, you need to add some neccessary files, by either downloading or extracting them.

Some files are optional but highly recommended:

| Directory | |
| :- | :- |
| dbc | Mandatory |
| maps | Mandatory |
| vmaps | HIGHLY RECOMMENDED |
| mmaps | HIGHLY RECOMMENDED |
| cameras | Recommended |

If you do not want to extract these files using the extractors you can find download links here:

Github link:

[Full data (v10) - from 05/04/2021 to now](https://github.com/wowgaming/client-data/releases/download/v10/data.zip) (Used in the automatic downloader script in `/apps/`)

Mega link:

[DBC & maps for all versions](https://mega.nz/#F!pyYlkK6b!pNz-zhThXQIg0_rO5L_RsQ)

## Extractors

If you downloaded the files above you can skip this step and jump forward to [worldserver.conf / authserver.conf](#worldserverconf--authserverconf).

This part is just a general summary of the overall process - please read it more detaild for the OS you are working with.

[Linux Server Setup](linux-server-setup.md)

[macOS Server Setup](macos-server-setup.md)

[Windows Server Setup](windows-server-setup.md)

AzerothCore needs certain files extracted from the World of Warcraft client. You need to extract them from a 3.3.5a client.

By default you will compile your core with tools and you will get the following executable files: **mapextractor**, **vmap4extractor**, **vmap4assembler**, **mmaps_generator** (.exe on windows).

Place the files with your World of Warcraft binary (wow.exe on windows) and run them.

After extracting all neccessary files, create a folder called **Data** within the **RelWithDebInfo** or **Debug** directory and place the files in there. Alternatively you can specify directory where you want to keep them changing DataDir value in worldserver.conf file.

If you use extractors from other projects or branches it is almost certain that your AzerothCore will not recognize the extracted data or even work!

When this is complete you may receive the following message which can be safely ignored:

```
Processing Map 724
[################################################################]
Extracting GameObject models...Extracting World\Wmo\Band\Final_Stage.wmo
No such file.
Couldn't open RootWmo!!!
Done!
  
Extract V4.00 2012_02. Work complete. No errors.
```

## worldserver.conf / authserver.conf

1. Make copies of both .dist files.

1. From each copy, remove the .dist part.

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

The following steps must be verified:

- The hostname (127.0.0.1) can stay the same if AzerothCore is being installed on the same computer that you run WoW on.
  Otherwise, follow the instruction in [Realmlist Table](realmlist.md) if this is not the case. 

- The port (3306) is the standard configured value. If you changed the default port in your mysql settings, you must change it accordingly.
  The username and password can be variable. You can choose to either: 

    - use default acore / acore username and password pair.

    - create an unique login within a User Manager within your preferred database management tool (commonly identified by an icon that looks like a person or people) and give it necessary permissions (SELECT, INSERT, UPDATE, DELETE permissions are sufficient, and is much safer).


*Pro Tip: For most worldserver.conf setting changes, you can simply type .reload config in-game to see changes instantly without restarting the server.*

*NOTE: The AzerothCore Team and Owners DO NOT in any case sponsor nor support illegal public servers. If you use these projects to run an illegal public server and not for testing and learning it is your own personal choice.*

## Trouble Shooting

"**Unable to open wmo_list.txt! Nothing extracted.**"

You need to run Mapextractor.exe before the makevmaps_simple.bat.

<br>

## Help

If you are still having problems, check:

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation.md) | [Step 4: Database Installation >>](database-installation.md) |
