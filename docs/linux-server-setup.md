# Linux Server Setup

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](linux-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |

**Table of contents**
- [Client Data Files (Download Pre-Extracted)](#option-1-download-pre-extracted-files)
- [Client Data Extractors (Extract Files Yourself)](#option-2-extract-files-yourself)
- [Config Files: Worldserver and Authserver](#config-files-worldserver-and-authserver)

Now that you have the source compiled, you need to add the necessary client data. You can either download pre-extracted files or use the compiled extractors to extract the files yourself. Once the data is ready, you must verify the **DataDir** option in your **worldserver.conf** file to point to the directory containing the data.

Some files are optional but highly recommended:

| Directory |                    |
| :-------- | :----------------- |
| dbc       | Mandatory          |
| maps      | Mandatory          |
| vmaps     | HIGHLY RECOMMENDED |
| mmaps     | HIGHLY RECOMMENDED |
| cameras   | Recommended        |

## Option 1: Download Pre-Extracted Files


If you intend to use an enUS client you can download the data files below. If you intend to use any other language client you will need to [extract](#option-2-extract-files-yourself) the data yourself.

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> Data files enUS (AC Data v16)</a>

1. Download archive `data.zip`.

2. Extract the archive directly into the default **$AC_CODE_DIR/env/dist/bin/** directory as specified by DataDir option in **wordserver.conf**. You may choose another folder, but you'll need edit your the [DataDir](#updating-datadir) config option to the location of your folder.

Default folder structure of **$AC_CODE_DIR/env/dist/bin** (as displayed by `tree -L 1`):
```
.
├── authserver
├── Cameras
├── data-version
├── dbc
├── maps
├── mmaps
├── vmaps
└── worldserver
```

## Option 2: Extract Files Yourself

**(Not needed if you downloaded the files above)**

1. Browse into your install directory (e.g. **$AC_CODE_DIR/env/dist/bin/**) and copy the following files into your World of Warcraft folder (where the Wow.exe is located).
```
map_extractor
mmaps_generator
vmap4_assembler
vmap4_extractor
```

2. Browse into **$AC_CODE_DIR/apps/extractor/** and copy "**extractor.sh**" into your World of Warcraft folder with the previous files.

3. Create (`mkdir`) **mmaps** and **vmaps** folders in your World of Warcraft directory.

4. Launch extractor.sh and select your extractor options.

{{site.data.alerts.important}}
</br>

   - <b>dbc</b>, <b>maps</b> AND <b>vmaps</b> are needed to make server work properly!

   - Do not attempt to stop <b>vmaps</b> extraction process. It is finished when it prints "Press any key...". It will create two new folders: <b>buildings</b> and <b>vmaps</b> The <b>buildings</b> folder is completely useless post-running and can be safely deleted.

   - Don't run another task before the first is finished or you will have errors.

   - If you stop vmap4extractor before finish you will need to delete the Buildings directory before start again.

   - <b>Optional but extremely recommended: Extract mmaps.</b> Do not attempt to stop this process while it is extracting.
{{site.data.alerts.end}}


5. Move the extracted files <b>vmaps</b>, <b>maps</b>, <b>dbc</b> and <b>Cameras</b> into the <b>$AC_CODE_DIR/env/dist/bin/</b> folder or a directory of your choice (remember to update your the [DataDir](#updating-datadir))

When this is complete you will receive the following message which can be safely ignored.

## Config Files: Worldserver and Authserver

First of all you need to find the two default config files (named **worldserver.conf.dist** and **authserver.conf.dist**) and copy them. Then rename the copies their namesakes without the .dist extension. You can find them within the install directory **$AC_CODE_DIR/env/dist/etc/**.

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

> **Note:** The default value for DataDir is `"."`. This means if your client files (dbc, maps, mmaps,...) are located in the same directory as the worldserver binary, there's no need to update this option.

1. In your **worldserver.conf** file locate the **DataDir** option.

1. Edit DataDir to the absolute or relative path of your folder. e.g, **/home/acore/azerothcore/data/** or **./data**

{% include tip.html content="For most **worldserver.conf** setting changes, you can simply type .reload config in-game to see changes instantly without restarting the server." %}

{% include warning.html content="The AzerothCore Team and Owners DO NOT in any case sponsor nor support illegal public servers. If you use these projects to run an illegal public server and not for testing and learning it is your own personal choice." %}

### (Optional) Config options by environment variable

It is possible to load config options via environment variables, which you can read about [here](config-overrides-with-env-var).

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](linux-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |
