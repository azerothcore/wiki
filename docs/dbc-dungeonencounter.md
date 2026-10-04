# DungeonEncounter.dbc

[`Back-to:DBC`](dbc-index)

**The \`DungeonEncounter.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [dungeonencounter_dbc](dungeonencounter_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | dungeonencounter\_dbc column                    | Comment |
| :----: | :------------- | :----- | :---------------------------------------------- | :------ |
| 0      | ID             | uint32 | [ID](dungeonencounter_dbc#id)                   |         |
| 1      | MapID          | uint32 | [MapID](dungeonencounter_dbc#mapid)             |         |
| 2      | Difficulty     | uint32 | [Difficulty](dungeonencounter_dbc#difficulty)   |         |
| 3      | OrderIndex     | int32  | [OrderIndex](dungeonencounter_dbc#orderindex)   |         |
| 4      | Bit            | uint32 | [Bit](dungeonencounter_dbc#bit)                 |         |
| 5      | Name_0         | string | [Name_Lang_enUS](dungeonencounter_dbc#namelang) |         |
| 6      | Name_1         | string | [Name_Lang_enGB](dungeonencounter_dbc#namelang) |         |
| 7      | Name_2         | string | [Name_Lang_koKR](dungeonencounter_dbc#namelang) |         |
| 8      | Name_3         | string | [Name_Lang_frFR](dungeonencounter_dbc#namelang) |         |
| 9      | Name_4         | string | [Name_Lang_deDE](dungeonencounter_dbc#namelang) |         |
| 10     | Name_5         | string | [Name_Lang_enCN](dungeonencounter_dbc#namelang) |         |
| 11     | Name_6         | string | [Name_Lang_zhCN](dungeonencounter_dbc#namelang) |         |
| 12     | Name_7         | string | [Name_Lang_enTW](dungeonencounter_dbc#namelang) |         |
| 13     | Name_8         | string | [Name_Lang_zhTW](dungeonencounter_dbc#namelang) |         |
| 14     | Name_9         | string | [Name_Lang_esES](dungeonencounter_dbc#namelang) |         |
| 15     | Name_10        | string | [Name_Lang_esMX](dungeonencounter_dbc#namelang) |         |
| 16     | Name_11        | string | [Name_Lang_ruRU](dungeonencounter_dbc#namelang) |         |
| 17     | Name_12        | string | [Name_Lang_ptPT](dungeonencounter_dbc#namelang) |         |
| 18     | Name_13        | string | [Name_Lang_ptBR](dungeonencounter_dbc#namelang) |         |
| 19     | Name_14        | string | [Name_Lang_itIT](dungeonencounter_dbc#namelang) |         |
| 20     | Name_15        | string | [Name_Lang_Unk](dungeonencounter_dbc#namelang)  |         |
| 21     | Name_lang_mask | uint32 | [Name_Lang_Mask](dungeonencounter_dbc#namelang) |         |
| 22     | SpellIconID    | uint32 | [SpellIconID](dungeonencounter_dbc#spelliconid) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DungeonEncounter).
