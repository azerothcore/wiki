# Windows Server Setup

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](windows-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |

**Table of contents**
- [Client Data Files (Download Pre-Extracted)](#option-1-download-pre-extracted-files)
- [Client Data Extractors (Extract Files Yourself)](#option-2-extract-files-yourself)
- [Config Files: Worldserver and Authserver](#config-files-worldserver-and-authserver)

Now that you have the source compiled, you need to add the necessary client data. You can either download pre-extracted files or use the compiled extractors to extract the files yourself. Once the data is ready, you must update the **DataDir** option in your **worldserver.conf** file to point to the directory containing the data.

Some files are optional but highly recommended:

| Directory |                    |
| :-------- | :----------------- |
| dbc       | Mandatory          |
| maps      | Mandatory          |
| vmaps     | HIGHLY RECOMMENDED |
| mmaps     | HIGHLY RECOMMENDED |
| Cameras   | Recommended        |

## Option 1: Download Pre-Extracted Files

If you intend to use an english (`enUS` or `enGB`) client you can download the data files below. If you intend to use any other language client you will need to [extract](#option-2-extract-files-yourself) the data yourself.

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> Data files enUS (AC Data v16)</a>

1. Download the files above.

2. Create a new folder within the build folder called **Data**. i.e **C:\Build\bin\RelWithDebInfo\Data**

3. Extract the files from the zip file and place them within the **Data** folder.

4. Edit your the [DataDir](#updating-datadir) config option to the location of your folder.

## Option 2: Extract Files Yourself

**(Not needed if you downloaded the files above)**

1. Browse into your build directory (**C:\Build\bin\RelWithDebInfo\\**) and copy the following files into your World of Warcraft folder (where the wow.exe is located).
```
map_extractor.exe
mmaps_generator.exe
vmap4_extractor.exe
vmap4_assembler.exe
```

2. Browse into **C:\Azerothcore\apps\extractor** and copy "**extractor.bat**" into your World of Warcraft folder with the previous files.

3. Create **mmaps** and **vmaps** folders in your World of Warcraft directory.

Note: To be able to generate your mmaps you will have to have present the `mmaps-config.yaml` in the same place as your `mmaps_generator.exe`, you can find the YAML file in `C:\Azerothcore\src\tools\mmaps_generator`.

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

## Config Files: Worldserver and Authserver

First of all you need to find the two default config files (named **worldserver.conf.dist** and **authserver.conf.dist**) and copy them. Then rename the copies their namesakes without the .dist extension. You can find them within C:\Build\bin\RelWithDebInfo\configs\ (may vary).

You will need to go in the `Build` folder you created, under `\bin\RelWithDebInfo\configs` and make a copy and rename the copies to the following:
`worldserver.conf.dist - Copy` to `worldserver.conf`
`authserver.conf.dist - Copy` to `authserver.conf`

{% include tip.html content="In the case you made the copies and it still giving you errors because it doesnt find either config, make sure you've -Hide extensions for known file types- unchecked in your windows folder options, and you can validate if the file names are correct." %}


## Updating DataDir / Data Directory

1. In your `worldserver.conf` file locate the `DataDir` option.

2. Edit it to the path of your folder the following examples below:
  - Current folder, if the `Data` folder is in the same place as your `authserver` and `worldserver` setting `DataDir = "./Data"`. 


  - To relative / full path path: `DataDir = "C:\Build\bin\RelWithDebInfo\Data"`.


For most `worldserver.conf` setting changes, you can simply type `.reload config` in-game to see changes instantly without restarting the server.


{% include warning.html content="The AzerothCore Team and Owners DO NOT in any case sponsor nor support illegal public servers. If you use these projects to run an illegal public server and not for testing and learning it is your own personal choice." %}

## (Optional) Config options by environment variable

It is possible to load config options via environment variables, which you can read about [here](config-overrides-with-env-var).

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 2: Core Installation](windows-core-installation)                                                                                    | [Step 4: Database Installation >>](database-installation) |
