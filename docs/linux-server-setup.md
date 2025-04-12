# Linux Server Setup

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](linux-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |

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

2. Create a new folder within the build folder called **Data**. i.e **$HOME/azerothcore/data/**

3. Extract the files from the zip file and place them within the **Data** folder.

4. Edit your the [DataDir](#updating-datadir) config option to the location of your folder.

## Extractors

**(Not needed if you downloaded the files above)**

Go to your AzerothCore build directory (e.g. $AC_CODE_DIR/env/dist/) and copy the following files to your World of Warcraft binaries directory.

* **map_extractor**
* **mmaps_generator**
* **vmap4_assembler**
* **vmap4_extractor**

**DBC and Maps files**

```
cd <your WoW client directory>
./map_extractor
```

**Visual Maps (aka vmaps) Note: If you stop vmap4_extractor before finish you will need to delete the Buildings directory before start again.**

You can also extract vmaps which will take quite a while depending on your machine (up to hours on ancient hardware).

```
cd <your WoW client directory>
./vmap4_extractor
mkdir vmaps;
./vmap4_assembler Buildings vmaps
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

## Config Files: Worldserver and Authserver

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

The following steps must be verified:

- The hostname (127.0.0.1) can stay the same if AzerothCore is being installed on the same computer that you run WoW on.
  If not, follow the instruction in [Realmlist Table](realmlist).

- The port (3306) is the standard configured value. If you changed the default port in your MySQL settings, you must change it accordingly.
  The username and password can be variable. You can choose to either: 

    - use default acore / acore username and password pair.

    - create a unique login within a User Manager within your preferred database management tool (commonly identified by an icon that looks like a person or people) and give it the necessary permissions (SELECT, INSERT, UPDATE, DELETE permissions are sufficient, and is much safer).

### Updating DataDir

1. In your worldserver.conf file locate the **DataDir** option.

1. Edit it to the path of your folder. i.e **$HOME/azerothcore/data/**

{% include tip.html content="For most worldserver.conf setting changes, you can simply type .reload config in-game to see changes instantly without restarting the server." %}

{% include warning.html content="The AzerothCore Team and Owners DO NOT in any case sponsor nor support illegal public servers. If you use these projects to run an illegal public server and not for testing and learning it is your own personal choice." %}

### (Optional) Config options by environment variable

It is possible to load config options via environment variables, which you can read about [here](config-overrides-with-env-var).

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](linux-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |
