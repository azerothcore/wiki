# BattlemasterList.dbc

[`Back-to:DBC`](dbc-index)

**The \`BattlemasterList.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [battlemasterlist_dbc](battlemasterlist_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | battlemasterlist\_dbc column                                | Comment                                         |
| :----: | :---------------- | :----- | :---------------------------------------------------------- | :---------------------------------------------- |
| 0      | ID                | uint32 | [ID](battlemasterlist_dbc#id)                               |                                                 |
| 1      | MapID_0           | int32  | [MapID_1](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 2      | MapID_1           | int32  | [MapID_2](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 3      | MapID_2           | int32  | [MapID_3](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 4      | MapID_3           | int32  | [MapID_4](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 5      | MapID_4           | int32  | [MapID_5](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 6      | MapID_5           | int32  | [MapID_6](battlemasterlist_dbc#mapid)                       | ID in [Map.dbc](map)                            |
| 7      | MapID_6           | int32  | [MapID_7](battlemasterlist_dbc#mapid)                       |                                                 |
| 8      | MapID_7           | int32  | [MapID_8](battlemasterlist_dbc#mapid)                       |                                                 |
| 9      | InstanceType      | uint32 | [InstanceType](battlemasterlist_dbc#instancetype)           |                                                 |
| 10     | GroupsAllowed     | uint32 | [GroupsAllowed](battlemasterlist_dbc#groupsallowed)         |                                                 |
| 11     | Name_0            | string | [Name_Lang_enUS](battlemasterlist_dbc#namelang)             | Assumed enUS                                    |
| 12     | Name_1            | string | [Name_Lang_enGB](battlemasterlist_dbc#namelang)             | Assumed enGB, not used in 3.3.5a                |
| 13     | Name_2            | string | [Name_Lang_koKR](battlemasterlist_dbc#namelang)             | Assumed koKR                                    |
| 14     | Name_3            | string | [Name_Lang_frFR](battlemasterlist_dbc#namelang)             | Assumed frFR                                    |
| 15     | Name_4            | string | [Name_Lang_deDE](battlemasterlist_dbc#namelang)             | Assumed deDE                                    |
| 16     | Name_5            | string | [Name_Lang_enCN](battlemasterlist_dbc#namelang)             | Assumed enCN, not used in 3.3.5a                |
| 17     | Name_6            | string | [Name_Lang_zhCN](battlemasterlist_dbc#namelang)             | Assumed zhCN                                    |
| 18     | Name_7            | string | [Name_Lang_enTW](battlemasterlist_dbc#namelang)             | Assumed enTW, not used in 3.3.5a                |
| 19     | Name_8            | string | [Name_Lang_zhTW](battlemasterlist_dbc#namelang)             | Assumed zhTW                                    |
| 20     | Name_9            | string | [Name_Lang_esES](battlemasterlist_dbc#namelang)             | Assumed esES                                    |
| 21     | Name_10           | string | [Name_Lang_esMX](battlemasterlist_dbc#namelang)             | Assumed esMX                                    |
| 22     | Name_11           | string | [Name_Lang_ruRU](battlemasterlist_dbc#namelang)             | Assumed ruRU                                    |
| 23     | Name_12           | string | [Name_Lang_ptPT](battlemasterlist_dbc#namelang)             | Assumed ptPT, not used in 3.3.5a                |
| 24     | Name_13           | string | [Name_Lang_ptBR](battlemasterlist_dbc#namelang)             | Assumed ptBR, not used in 3.3.5a                |
| 25     | Name_14           | string | [Name_Lang_itIT](battlemasterlist_dbc#namelang)             | Assumed itIT, not used in 3.3.5a                |
| 26     | Name_15           | string | [Name_Lang_Unk](battlemasterlist_dbc#namelang)              | Unknown language, unsure of the usage in 3.3.5a |
| 27     | Name_lang_mask    | uint32 | [Name_Lang_Mask](battlemasterlist_dbc#namelang)             | Assumed flags of the localized text             |
| 28     | MaxGroupSize      | uint32 | [MaxGroupSize](battlemasterlist_dbc#maxgroupsize)           |                                                 |
| 29     | HolidayWorldState | uint32 | [HolidayWorldState](battlemasterlist_dbc#holidayworldstate) |                                                 |
| 30     | MinLevel          | uint32 | [Minlevel](battlemasterlist_dbc#minlevel)                   |                                                 |
| 31     | MaxLevel          | uint32 | [Maxlevel](battlemasterlist_dbc#maxlevel)                   |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/BattlemasterList).
