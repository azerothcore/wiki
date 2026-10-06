# AreaPOI.dbc

[`Back-to:DBC`](dbc-index)

**The \`AreaPOI.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [areapoi_dbc](areapoi_dbc) table of the world database.

**Structure**

| Column | Field                 | Type   | areapoi\_dbc column                                  | Comment                                         |
| :----: | :-------------------- | :----- | :--------------------------------------------------- | :---------------------------------------------- |
| 0      | ID                    | uint32 | [ID](areapoi_dbc#id)                                 |                                                 |
| 1      | Importance            | uint32 | [Importance](areapoi_dbc#importance)                 |                                                 |
| 2      | Icon_0                | uint32 | [Icon_1](areapoi_dbc#icon)                           |                                                 |
| 3      | Icon_1                | uint32 | [Icon_2](areapoi_dbc#icon)                           |                                                 |
| 4      | Icon_2                | uint32 | [Icon_3](areapoi_dbc#icon)                           |                                                 |
| 5      | Icon_3                | uint32 | [Icon_4](areapoi_dbc#icon)                           |                                                 |
| 6      | Icon_4                | uint32 | [Icon_5](areapoi_dbc#icon)                           |                                                 |
| 7      | Icon_5                | uint32 | [Icon_6](areapoi_dbc#icon)                           |                                                 |
| 8      | Icon_6                | uint32 | [Icon_7](areapoi_dbc#icon)                           |                                                 |
| 9      | Icon_7                | uint32 | [Icon_8](areapoi_dbc#icon)                           |                                                 |
| 10     | Icon_8                | uint32 | [Icon_9](areapoi_dbc#icon)                           |                                                 |
| 11     | FactionID             | uint32 | [FactionID](areapoi_dbc#factionid)                   | ID in [FactionTemplate.dbc](factiontemplate)    |
| 12     | Pos_X                 | float  | [X](areapoi_dbc#x)                                   |                                                 |
| 13     | Pos_Y                 | float  | [Y](areapoi_dbc#y)                                   |                                                 |
| 14     | Pos_Z                 | float  | [Z](areapoi_dbc#z)                                   |                                                 |
| 15     | ContinentID           | uint32 | [ContinentID](areapoi_dbc#continentid)               | ID in [Map.dbc](map)                            |
| 16     | Flags                 | uint32 | [Flags](areapoi_dbc#flags)                           |                                                 |
| 17     | AreaID                | uint32 | [AreaID](areapoi_dbc#areaid)                         | ID in [AreaTable.dbc](areatable)                |
| 18     | Name_0                | string | [Name_Lang_enUS](areapoi_dbc#namelang)               | Assumed enUS                                    |
| 19     | Name_1                | string | [Name_Lang_enGB](areapoi_dbc#namelang)               | Assumed enGB, not used in 3.3.5a                |
| 20     | Name_2                | string | [Name_Lang_koKR](areapoi_dbc#namelang)               | Assumed koKR                                    |
| 21     | Name_3                | string | [Name_Lang_frFR](areapoi_dbc#namelang)               | Assumed frFR                                    |
| 22     | Name_4                | string | [Name_Lang_deDE](areapoi_dbc#namelang)               | Assumed deDE                                    |
| 23     | Name_5                | string | [Name_Lang_enCN](areapoi_dbc#namelang)               | Assumed enCN, not used in 3.3.5a                |
| 24     | Name_6                | string | [Name_Lang_zhCN](areapoi_dbc#namelang)               | Assumed zhCN                                    |
| 25     | Name_7                | string | [Name_Lang_enTW](areapoi_dbc#namelang)               | Assumed enTW, not used in 3.3.5a                |
| 26     | Name_8                | string | [Name_Lang_zhTW](areapoi_dbc#namelang)               | Assumed zhTW                                    |
| 27     | Name_9                | string | [Name_Lang_esES](areapoi_dbc#namelang)               | Assumed esES                                    |
| 28     | Name_10               | string | [Name_Lang_esMX](areapoi_dbc#namelang)               | Assumed esMX                                    |
| 29     | Name_11               | string | [Name_Lang_ruRU](areapoi_dbc#namelang)               | Assumed ruRU                                    |
| 30     | Name_12               | string | [Name_Lang_ptPT](areapoi_dbc#namelang)               | Assumed ptPT, not used in 3.3.5a                |
| 31     | Name_13               | string | [Name_Lang_ptBR](areapoi_dbc#namelang)               | Assumed ptBR, not used in 3.3.5a                |
| 32     | Name_14               | string | [Name_Lang_itIT](areapoi_dbc#namelang)               | Assumed itIT, not used in 3.3.5a                |
| 33     | Name_15               | string | [Name_Lang_Unk](areapoi_dbc#namelang)                | Unknown language, unsure of the usage in 3.3.5a |
| 34     | Name_lang_mask        | uint32 | [Name_Lang_Mask](areapoi_dbc#namelang)               | Assumed flags of the localized text             |
| 35     | Description_0         | string | [Description_Lang_enUS](areapoi_dbc#descriptionlang) | Assumed enUS                                    |
| 36     | Description_1         | string | [Description_Lang_enGB](areapoi_dbc#descriptionlang) | Assumed enGB, not used in 3.3.5a                |
| 37     | Description_2         | string | [Description_Lang_koKR](areapoi_dbc#descriptionlang) | Assumed koKR                                    |
| 38     | Description_3         | string | [Description_Lang_frFR](areapoi_dbc#descriptionlang) | Assumed frFR                                    |
| 39     | Description_4         | string | [Description_Lang_deDE](areapoi_dbc#descriptionlang) | Assumed deDE                                    |
| 40     | Description_5         | string | [Description_Lang_enCN](areapoi_dbc#descriptionlang) | Assumed enCN, not used in 3.3.5a                |
| 41     | Description_6         | string | [Description_Lang_zhCN](areapoi_dbc#descriptionlang) | Assumed zhCN                                    |
| 42     | Description_7         | string | [Description_Lang_enTW](areapoi_dbc#descriptionlang) | Assumed enTW, not used in 3.3.5a                |
| 43     | Description_8         | string | [Description_Lang_zhTW](areapoi_dbc#descriptionlang) | Assumed zhTW                                    |
| 44     | Description_9         | string | [Description_Lang_esES](areapoi_dbc#descriptionlang) | Assumed esES                                    |
| 45     | Description_10        | string | [Description_Lang_esMX](areapoi_dbc#descriptionlang) | Assumed esMX                                    |
| 46     | Description_11        | string | [Description_Lang_ruRU](areapoi_dbc#descriptionlang) | Assumed ruRU                                    |
| 47     | Description_12        | string | [Description_Lang_ptPT](areapoi_dbc#descriptionlang) | Assumed ptPT, not used in 3.3.5a                |
| 48     | Description_13        | string | [Description_Lang_ptBR](areapoi_dbc#descriptionlang) | Assumed ptBR, not used in 3.3.5a                |
| 49     | Description_14        | string | [Description_Lang_itIT](areapoi_dbc#descriptionlang) | Assumed itIT, not used in 3.3.5a                |
| 50     | Description_15        | string | [Description_Lang_Unk](areapoi_dbc#descriptionlang)  | Unknown language, unsure of the usage in 3.3.5a |
| 51     | Description_lang_mask | uint32 | [Description_Lang_Mask](areapoi_dbc#descriptionlang) | Assumed flags of the localized text             |
| 52     | WorldStateID          | uint32 | [WorldStateID](areapoi_dbc#worldstateid)             |                                                 |
| 53     | WorldMapLink          | uint32 | [WorldMapLink](areapoi_dbc#worldmaplink)             |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AreaPOI).
