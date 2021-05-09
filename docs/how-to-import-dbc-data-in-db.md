# How to import DBC data inside the AC database

This guide will show you how to import DBC data inside the AzerothCore database and edit them. For the guide we are going to use the AreaTable.dbc as example
by changing the Hyjal zone from "Normal" to "Sanctuary (with duels allowed)". 
If you do this you will turn that zone into crossfaction and, for example, you can use it for events.

However, the same guide can be used for any kind of DBC ([Spell](importing-spell-dbc), Items etc.) by changing the values of the commands below.

## Requirements

- [Nodejs](https://nodejs.org/en/) for the node-dbc-reader

## Getting started

### 1. install my dbc-reader

Clone or download [this repository](https://github.com/wowgaming/node-dbc-reader) and run `npm install` inside the downloaded folder.

*Read the documentation of that repository if you need to run more complex commands.*

### 2. Search your data

Run this command to check that the zone is correct: `npm run start -- --search="[616].includes({*})" --columns=ID AreaTable`

This command will search into the **ID** column with the following condition: `[616].includes({*})` which means that the program will search for all the IDs that include
the values within the [ ] array. In this case we only need the value 616. 

*Note: the --search option is backed by an eval, which means you can run any javascript method to execute a comparison*

The result of that command will be:
```json
{
    "ID": 616,
    "ContinentID": 1,
    "ParentAreaID": 0,
    "AreaBit": 619,
    "Flags": 64,
    "SoundProviderPref": 0,
    "SoundProviderPrefUnderwater": 11,
    "AmbienceID": 31,
    "ZoneMusic": 0,
    "IntroSound": 0,
    "ExplorationLevel": 0,
    "AreaName_Lang_enUS": "Hyjal",
    "AreaName_Lang_enGB": "",
    "AreaName_Lang_koKR": "",
    "AreaName_Lang_frFR": "",
    "AreaName_Lang_deDE": "",
    "AreaName_Lang_enCN": "",
    "AreaName_Lang_zhCN": "",
    "AreaName_Lang_enTW": "",
    "AreaName_Lang_zhTW": "",
    "AreaName_Lang_esES": "",
    "AreaName_Lang_esMX": "",
    "AreaName_Lang_ruRU": "",
    "AreaName_Lang_ptPT": "",
    "AreaName_Lang_ptBR": "",
    "AreaName_Lang_itIT": "",
    "AreaName_Lang_Unk": "",
    "AreaName_Lang_Mask": 16712190,
    "FactionGroupMask": 0,
    "LiquidTypeID_1": 0,
    "LiquidTypeID_2": 0,
    "LiquidTypeID_3": 0,
    "LiquidTypeID_4": 0,
    "MinElevation": -500,
    "Ambient_Multiplier": 0,
    "Lightid": 0
  }
  ````

The value: `"Flags": 64` means "normal zone", we have to override it with `19456 - Sanctuary (Duels allowed)`.

You can check the list of the flags [here](https://www.azerothcore.org/wiki/AreaTable)

3. Export the SQL

Now run the same command above but with the output type : `npm run start -- -s "[616].includes({*})" -t sql  --columns=ID AreaTable` to extract the INSERT query

Output: 
```sql
INSERT IGNORE INTO areatable_dbc (`ID`,`ContinentID`,`ParentAreaID`,`AreaBit`,`Flags`,`SoundProviderPref`,`SoundProviderPrefUnderwater`,`AmbienceID`,`ZoneMusic`,`IntroSound`,`ExplorationLevel`,`AreaName_Lang_enUS`,`AreaName_Lang_enGB`,`AreaName_Lang_koKR`,`AreaName_Lang_frFR`,`AreaName_Lang_deDE`,`AreaName_Lang_enCN`,`AreaName_Lang_zhCN`,`AreaName_Lang_enTW`,`AreaName_Lang_zhTW`,`AreaName_Lang_esES`,`AreaName_Lang_esMX`,`AreaName_Lang_ruRU`,`AreaName_Lang_ptPT`,`AreaName_Lang_ptBR`,`AreaName_Lang_itIT`,`AreaName_Lang_Unk`,`AreaName_Lang_Mask`,`FactionGroupMask`,`LiquidTypeID_1`,`LiquidTypeID_2`,`LiquidTypeID_3`,`LiquidTypeID_4`,`MinElevation`,`Ambient_Multiplier`,`Lightid`)
 VALUES (616,1,0,619,64,0,11,31,0,0,0,"Hyjal","","","","","","","","","","","","","","","",16712190,0,0,0,0,0,-500,0,0);
````

4. Create the Update Query

Create the update query to set the proper faction :

```sql
UPDATE areatable_dbc SET Flags=19456 WHERE ID=616
```

5. Create your PR

If you are using this guide to fix a bug (not for customization purpose), 
now you can create [your PR](https://www.azerothcore.org/wiki/How-to-create-a-PR) with the 2 queries above 

