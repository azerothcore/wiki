# Server Setup

| Installation Guide                                                                                                                      |                                                              |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps.    |
| [<< Step 2: Core Installation](core-installation)                                                                                       | [Step 4: Database Installation >>](database-installation)    |

**Table of contents**
- [Data files](#data-files) - Required/Optional (Not needed if you extract the files.)
- [Extractors](#extractors) - Required/Optional (Not needed if you download the files.)
- [Config Files: Worldserver and Authserver](#config-files-worldserver-and-authserver) - Required

Now that you have the source compiled, you need to add some necessary files, by either downloading or extracting them.

Some files are optional but highly recommended:

| Directory |                    |
| :-------- | :----------------- |
| dbc       | Mandatory          |
| maps      | Mandatory          |
| vmaps     | HIGHLY RECOMMENDED |
| mmaps     | HIGHLY RECOMMENDED |
| cameras   | Recommended        |

## Data files

If you intend to use an enUS client you can download the data files below. If you intend to use any other language client you will need to [extract](#extractors) the data yourself.

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> Data files enUS (AC Data v16)</a>

1. Download the files above.

2. Create a new folder within the build folder called **Data**. i.e windows: **C:\Build\bin\RelWithDebInfo\Data** or Linux: **$HOME/azerothcore/data/**

3. Extract the files from the zip file and place them within the **Data** folder.

4. Edit your the [DataDir](#updating-datadir) config option to the location of your folder.

## Extractors

**(Not needed if you downloaded the files above)**

If you downloaded the files above you can skip this step and jump forward to [worldserver.conf and authserver.conf](#config-files-worldserver-and-authserver).

This part is just a general summary of the overall process - please read it in more detail for the OS you are working with.

[Linux Server Setup](linux-server-setup)

[macOS Server Setup](macos-server-setup)

[Windows Server Setup](windows-server-setup)

AzerothCore needs certain files extracted from the World of Warcraft client. You need to extract them from a 3.3.5a client.

By default, you will compile your core with tools and you will get the following executable files: **mapextractor**, **vmap4extractor**, **vmap4assembler**, **mmaps_generator** (.exe on Windows).

Place the files with your World of Warcraft binary (wow.exe on Windows) and run them.

After extracting all necessary files, create a folder called **Data** within the **RelWithDebInfo** or **Debug** directory and place the files in there. Alternatively, you can specify a different directory where you want to keep them by changing the DataDir value in the worldserver.conf file.

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

### Trouble Shooting

"**Unable to open wmo_list.txt! Nothing extracted.**"

You need to run Mapextractor.exe before the makevmaps_simple.bat.

## Config Files: Worldserver and Authserver

Every time the core is recompiled a distributed, .dist, conf file will be made where all the default options are stored. This file serves no real purpose except for distributing all the options from the core.

### Creating the config files

1. Go to your configs folder i.e. D:\build\bin\RelWithDebInfo\configs

1. Remove the **.dist** part from **worldserver.conf.dist** and **authserver.conf.dist**.

    - You should be left with **worldserver.conf** and **authserver.conf**.

Open the .conf files and scroll down to LoginDatabaseInfo, WorldDatabaseInfo, and CharacterDatabaseInfo and enter MySQL login information for the server to be able to access your database.

On a newly compiled configuration, you will have the following values by default

```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth"         -> worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world"        -> worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters"   -> worldserver.conf
```

That part of the configuration follows this specific format or structure:

```
Variablename = "MySQLIP;Port;Username;Password;database"  
``` 

The following steps must be verified:

- The hostname (127.0.0.1) can stay the same if AzerothCore is being installed on the same computer that you run WoW on.
  If not, follow the instruction in [Realmlist Table](realmlist).

- The port (3306) is the standard configured value. If you changed the default port in your MySQL settings, you must change it accordingly.
  The username and password can be variable. You can choose to either: 

    - use default acore / acore username and password pair.

    - create a unique login within a User Manager within your preferred database management tool (commonly identified by an icon that looks like a person or people) and give it the necessary permissions (SELECT, INSERT, UPDATE, DELETE permissions are sufficient, and is much safer).

### Updating DataDir

1. In your worldserver.conf file locate the **DataDir** option.

1. Edit it to the path of your folder. i.e **C:\Build\bin\RelWithDebInfo\Data**

{% include tip.html content="For most worldserver.conf setting changes, you can simply type .reload config in-game to see changes instantly without restarting the server." %}

{% include warning.html content="The AzerothCore Team and Owners DO NOT in any case sponsor nor support illegal public servers. If you use these projects to run an illegal public server and not for testing and learning it is your own personal choice." %}

### (Optional) Config options by environment variable

It is possible to load config options via environment variables, which you can read about [here](config-overrides-with-env-var).

## Help

If you are still having problems, check:

* [FAQ](faq)

* [Common Errors](common-errors)

* [How to ask for help](how-to-ask-for-help)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide                                                                                                                   |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation)    |
