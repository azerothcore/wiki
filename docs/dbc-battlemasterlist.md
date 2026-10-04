# BattlemasterList.dbc

[`Back-to:DBC`](dbc-index)

**The \`BattlemasterList.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [battlemasterlist_dbc](battlemasterlist_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | battlemasterlist\_dbc column                                | Comment |
| :----: | :---------------- | :----- | :---------------------------------------------------------- | :------ |
| 0      | ID                | uint32 | [ID](battlemasterlist_dbc#id)                               |         |
| 1      | MapID_0           | int32  | [MapID_1](battlemasterlist_dbc#mapid)                       |         |
| 2      | MapID_1           | int32  | [MapID_2](battlemasterlist_dbc#mapid)                       |         |
| 3      | MapID_2           | int32  | [MapID_3](battlemasterlist_dbc#mapid)                       |         |
| 4      | MapID_3           | int32  | [MapID_4](battlemasterlist_dbc#mapid)                       |         |
| 5      | MapID_4           | int32  | [MapID_5](battlemasterlist_dbc#mapid)                       |         |
| 6      | MapID_5           | int32  | [MapID_6](battlemasterlist_dbc#mapid)                       |         |
| 7      | MapID_6           | int32  | [MapID_7](battlemasterlist_dbc#mapid)                       |         |
| 8      | MapID_7           | int32  | [MapID_8](battlemasterlist_dbc#mapid)                       |         |
| 9      | InstanceType      | uint32 | [InstanceType](battlemasterlist_dbc#instancetype)           |         |
| 10     | GroupsAllowed     | uint32 | [GroupsAllowed](battlemasterlist_dbc#groupsallowed)         |         |
| 11     | Name_0            | string | [Name_Lang_enUS](battlemasterlist_dbc#namelang)             |         |
| 12     | Name_1            | string | [Name_Lang_enGB](battlemasterlist_dbc#namelang)             |         |
| 13     | Name_2            | string | [Name_Lang_koKR](battlemasterlist_dbc#namelang)             |         |
| 14     | Name_3            | string | [Name_Lang_frFR](battlemasterlist_dbc#namelang)             |         |
| 15     | Name_4            | string | [Name_Lang_deDE](battlemasterlist_dbc#namelang)             |         |
| 16     | Name_5            | string | [Name_Lang_enCN](battlemasterlist_dbc#namelang)             |         |
| 17     | Name_6            | string | [Name_Lang_zhCN](battlemasterlist_dbc#namelang)             |         |
| 18     | Name_7            | string | [Name_Lang_enTW](battlemasterlist_dbc#namelang)             |         |
| 19     | Name_8            | string | [Name_Lang_zhTW](battlemasterlist_dbc#namelang)             |         |
| 20     | Name_9            | string | [Name_Lang_esES](battlemasterlist_dbc#namelang)             |         |
| 21     | Name_10           | string | [Name_Lang_esMX](battlemasterlist_dbc#namelang)             |         |
| 22     | Name_11           | string | [Name_Lang_ruRU](battlemasterlist_dbc#namelang)             |         |
| 23     | Name_12           | string | [Name_Lang_ptPT](battlemasterlist_dbc#namelang)             |         |
| 24     | Name_13           | string | [Name_Lang_ptBR](battlemasterlist_dbc#namelang)             |         |
| 25     | Name_14           | string | [Name_Lang_itIT](battlemasterlist_dbc#namelang)             |         |
| 26     | Name_15           | string | [Name_Lang_Unk](battlemasterlist_dbc#namelang)              |         |
| 27     | Name_lang_mask    | uint32 | [Name_Lang_Mask](battlemasterlist_dbc#namelang)             |         |
| 28     | MaxGroupSize      | uint32 | [MaxGroupSize](battlemasterlist_dbc#maxgroupsize)           |         |
| 29     | HolidayWorldState | uint32 | [HolidayWorldState](battlemasterlist_dbc#holidayworldstate) |         |
| 30     | MinLevel          | uint32 | [Minlevel](battlemasterlist_dbc#minlevel)                   |         |
| 31     | MaxLevel          | uint32 | [Maxlevel](battlemasterlist_dbc#maxlevel)                   |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/BattlemasterList).
