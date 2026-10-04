# LfgDungeons.dbc

[`Back-to:DBC`](dbc-index)

**The \`LfgDungeons.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [lfgdungeons_dbc](lfgdungeons_dbc) table of the world database.

**Structure**

| Column | Field                 | Type   | lfgdungeons\_dbc column                                  | Comment |
| :----: | :-------------------- | :----- | :------------------------------------------------------- | :------ |
| 0      | ID                    | uint32 | [ID](lfgdungeons_dbc#id)                                 |         |
| 1      | Name_0                | string | [Name_Lang_enUS](lfgdungeons_dbc#namelang)               |         |
| 2      | Name_1                | string | [Name_Lang_enGB](lfgdungeons_dbc#namelang)               |         |
| 3      | Name_2                | string | [Name_Lang_koKR](lfgdungeons_dbc#namelang)               |         |
| 4      | Name_3                | string | [Name_Lang_frFR](lfgdungeons_dbc#namelang)               |         |
| 5      | Name_4                | string | [Name_Lang_deDE](lfgdungeons_dbc#namelang)               |         |
| 6      | Name_5                | string | [Name_Lang_enCN](lfgdungeons_dbc#namelang)               |         |
| 7      | Name_6                | string | [Name_Lang_zhCN](lfgdungeons_dbc#namelang)               |         |
| 8      | Name_7                | string | [Name_Lang_enTW](lfgdungeons_dbc#namelang)               |         |
| 9      | Name_8                | string | [Name_Lang_zhTW](lfgdungeons_dbc#namelang)               |         |
| 10     | Name_9                | string | [Name_Lang_esES](lfgdungeons_dbc#namelang)               |         |
| 11     | Name_10               | string | [Name_Lang_esMX](lfgdungeons_dbc#namelang)               |         |
| 12     | Name_11               | string | [Name_Lang_ruRU](lfgdungeons_dbc#namelang)               |         |
| 13     | Name_12               | string | [Name_Lang_ptPT](lfgdungeons_dbc#namelang)               |         |
| 14     | Name_13               | string | [Name_Lang_ptBR](lfgdungeons_dbc#namelang)               |         |
| 15     | Name_14               | string | [Name_Lang_itIT](lfgdungeons_dbc#namelang)               |         |
| 16     | Name_15               | string | [Name_Lang_Unk](lfgdungeons_dbc#namelang)                |         |
| 17     | Name_lang_mask        | uint32 | [Name_Lang_Mask](lfgdungeons_dbc#namelang)               |         |
| 18     | MinLevel              | uint32 | [MinLevel](lfgdungeons_dbc#minlevel)                     |         |
| 19     | MaxLevel              | uint32 | [MaxLevel](lfgdungeons_dbc#maxlevel)                     |         |
| 20     | TargetLevel           | uint32 | [Target_Level](lfgdungeons_dbc#targetlevel)              |         |
| 21     | TargetLevelMin        | uint32 | [Target_Level_Min](lfgdungeons_dbc#targetlevelmin)       |         |
| 22     | TargetLevelMax        | uint32 | [Target_Level_Max](lfgdungeons_dbc#targetlevelmax)       |         |
| 23     | MapID                 | int32  | [MapID](lfgdungeons_dbc#mapid)                           |         |
| 24     | Difficulty            | uint32 | [Difficulty](lfgdungeons_dbc#difficulty)                 |         |
| 25     | Flags                 | uint32 | [Flags](lfgdungeons_dbc#flags)                           |         |
| 26     | TypeID                | uint32 | [TypeID](lfgdungeons_dbc#typeid)                         |         |
| 27     | Faction               | int32  | [Faction](lfgdungeons_dbc#faction)                       |         |
| 28     | TextureFilename       | string | [TextureFilename](lfgdungeons_dbc#texturefilename)       |         |
| 29     | ExpansionLevel        | uint32 | [ExpansionLevel](lfgdungeons_dbc#expansionlevel)         |         |
| 30     | OrderIndex            | uint32 | [Order_Index](lfgdungeons_dbc#orderindex)                |         |
| 31     | GroupID               | uint32 | [Group_Id](lfgdungeons_dbc#groupid)                      |         |
| 32     | Description_0         | string | [Description_Lang_enUS](lfgdungeons_dbc#descriptionlang) |         |
| 33     | Description_1         | string | [Description_Lang_enGB](lfgdungeons_dbc#descriptionlang) |         |
| 34     | Description_2         | string | [Description_Lang_koKR](lfgdungeons_dbc#descriptionlang) |         |
| 35     | Description_3         | string | [Description_Lang_frFR](lfgdungeons_dbc#descriptionlang) |         |
| 36     | Description_4         | string | [Description_Lang_deDE](lfgdungeons_dbc#descriptionlang) |         |
| 37     | Description_5         | string | [Description_Lang_enCN](lfgdungeons_dbc#descriptionlang) |         |
| 38     | Description_6         | string | [Description_Lang_zhCN](lfgdungeons_dbc#descriptionlang) |         |
| 39     | Description_7         | string | [Description_Lang_enTW](lfgdungeons_dbc#descriptionlang) |         |
| 40     | Description_8         | string | [Description_Lang_zhTW](lfgdungeons_dbc#descriptionlang) |         |
| 41     | Description_9         | string | [Description_Lang_esES](lfgdungeons_dbc#descriptionlang) |         |
| 42     | Description_10        | string | [Description_Lang_esMX](lfgdungeons_dbc#descriptionlang) |         |
| 43     | Description_11        | string | [Description_Lang_ruRU](lfgdungeons_dbc#descriptionlang) |         |
| 44     | Description_12        | string | [Description_Lang_ptPT](lfgdungeons_dbc#descriptionlang) |         |
| 45     | Description_13        | string | [Description_Lang_ptBR](lfgdungeons_dbc#descriptionlang) |         |
| 46     | Description_14        | string | [Description_Lang_itIT](lfgdungeons_dbc#descriptionlang) |         |
| 47     | Description_15        | string | [Description_Lang_Unk](lfgdungeons_dbc#descriptionlang)  |         |
| 48     | Description_lang_mask | uint32 | [Description_Lang_Mask](lfgdungeons_dbc#descriptionlang) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LfgDungeons).
