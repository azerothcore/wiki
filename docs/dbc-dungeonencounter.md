# DungeonEncounter.dbc

[`Back-to:DBC`](dbc-index)

**The \`DungeonEncounter.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [dungeonencounter_dbc](dungeonencounter_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | dungeonencounter\_dbc column                    | Comment                                         |
| :----: | :------------- | :----- | :---------------------------------------------- | :---------------------------------------------- |
| 0      | ID             | uint32 | [ID](dungeonencounter_dbc#id)                   |                                                 |
| 1      | MapID          | uint32 | [MapID](dungeonencounter_dbc#mapid)             | ID in [Map.dbc](map)                            |
| 2      | Difficulty     | uint32 | [Difficulty](dungeonencounter_dbc#difficulty)   | ID in [MapDifficulty.dbc](dbc-mapdifficulty)    |
| 3      | OrderIndex     | int32  | [OrderIndex](dungeonencounter_dbc#orderindex)   |                                                 |
| 4      | Bit            | uint32 | [Bit](dungeonencounter_dbc#bit)                 |                                                 |
| 5      | Name_0         | string | [Name_Lang_enUS](dungeonencounter_dbc#namelang) | Assumed enUS                                    |
| 6      | Name_1         | string | [Name_Lang_enGB](dungeonencounter_dbc#namelang) | Assumed enGB, not used in 3.3.5a                |
| 7      | Name_2         | string | [Name_Lang_koKR](dungeonencounter_dbc#namelang) | Assumed koKR                                    |
| 8      | Name_3         | string | [Name_Lang_frFR](dungeonencounter_dbc#namelang) | Assumed frFR                                    |
| 9      | Name_4         | string | [Name_Lang_deDE](dungeonencounter_dbc#namelang) | Assumed deDE                                    |
| 10     | Name_5         | string | [Name_Lang_enCN](dungeonencounter_dbc#namelang) | Assumed enCN, not used in 3.3.5a                |
| 11     | Name_6         | string | [Name_Lang_zhCN](dungeonencounter_dbc#namelang) | Assumed zhCN                                    |
| 12     | Name_7         | string | [Name_Lang_enTW](dungeonencounter_dbc#namelang) | Assumed enTW, not used in 3.3.5a                |
| 13     | Name_8         | string | [Name_Lang_zhTW](dungeonencounter_dbc#namelang) | Assumed zhTW                                    |
| 14     | Name_9         | string | [Name_Lang_esES](dungeonencounter_dbc#namelang) | Assumed esES                                    |
| 15     | Name_10        | string | [Name_Lang_esMX](dungeonencounter_dbc#namelang) | Assumed esMX                                    |
| 16     | Name_11        | string | [Name_Lang_ruRU](dungeonencounter_dbc#namelang) | Assumed ruRU                                    |
| 17     | Name_12        | string | [Name_Lang_ptPT](dungeonencounter_dbc#namelang) | Assumed ptPT, not used in 3.3.5a                |
| 18     | Name_13        | string | [Name_Lang_ptBR](dungeonencounter_dbc#namelang) | Assumed ptBR, not used in 3.3.5a                |
| 19     | Name_14        | string | [Name_Lang_itIT](dungeonencounter_dbc#namelang) | Assumed itIT, not used in 3.3.5a                |
| 20     | Name_15        | string | [Name_Lang_Unk](dungeonencounter_dbc#namelang)  | Unknown language, unsure of the usage in 3.3.5a |
| 21     | Name_lang_mask | uint32 | [Name_Lang_Mask](dungeonencounter_dbc#namelang) | Assumed flags of the localized text             |
| 22     | SpellIconID    | uint32 | [SpellIconID](dungeonencounter_dbc#spelliconid) |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DungeonEncounter).
