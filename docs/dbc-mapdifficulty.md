# MapDifficulty.dbc

[`Back-to:DBC`](dbc-index)

**The \`MapDifficulty.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [mapdifficulty_dbc](mapdifficulty_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | mapdifficulty\_dbc column                              | Comment                                                                   |
| :----: | :---------------- | :----- | :----------------------------------------------------- | :------------------------------------------------------------------------ |
| 0      | ID                | uint32 | [ID](mapdifficulty_dbc#id)                             |                                                                           |
| 1      | MapID             | uint32 | [MapID](mapdifficulty_dbc#mapid)                       | ID in [Map.dbc](map) (1 of the 133 values used here are not in that file) |
| 2      | Difficulty        | uint32 | [Difficulty](mapdifficulty_dbc#difficulty)             |                                                                           |
| 3      | Message_0         | string | [Message_Lang_enUS](mapdifficulty_dbc#messagelang)     | Assumed enUS                                                              |
| 4      | Message_1         | string | [Message_Lang_enGB](mapdifficulty_dbc#messagelang)     | Assumed enGB, not used in 3.3.5a                                          |
| 5      | Message_2         | string | [Message_Lang_koKR](mapdifficulty_dbc#messagelang)     | Assumed koKR                                                              |
| 6      | Message_3         | string | [Message_Lang_frFR](mapdifficulty_dbc#messagelang)     | Assumed frFR                                                              |
| 7      | Message_4         | string | [Message_Lang_deDE](mapdifficulty_dbc#messagelang)     | Assumed deDE                                                              |
| 8      | Message_5         | string | [Message_Lang_enCN](mapdifficulty_dbc#messagelang)     | Assumed enCN, not used in 3.3.5a                                          |
| 9      | Message_6         | string | [Message_Lang_zhCN](mapdifficulty_dbc#messagelang)     | Assumed zhCN                                                              |
| 10     | Message_7         | string | [Message_Lang_enTW](mapdifficulty_dbc#messagelang)     | Assumed enTW, not used in 3.3.5a                                          |
| 11     | Message_8         | string | [Message_Lang_zhTW](mapdifficulty_dbc#messagelang)     | Assumed zhTW                                                              |
| 12     | Message_9         | string | [Message_Lang_esES](mapdifficulty_dbc#messagelang)     | Assumed esES                                                              |
| 13     | Message_10        | string | [Message_Lang_esMX](mapdifficulty_dbc#messagelang)     | Assumed esMX                                                              |
| 14     | Message_11        | string | [Message_Lang_ruRU](mapdifficulty_dbc#messagelang)     | Assumed ruRU                                                              |
| 15     | Message_12        | string | [Message_Lang_ptPT](mapdifficulty_dbc#messagelang)     | Assumed ptPT, not used in 3.3.5a                                          |
| 16     | Message_13        | string | [Message_Lang_ptBR](mapdifficulty_dbc#messagelang)     | Assumed ptBR, not used in 3.3.5a                                          |
| 17     | Message_14        | string | [Message_Lang_itIT](mapdifficulty_dbc#messagelang)     | Assumed itIT, not used in 3.3.5a                                          |
| 18     | Message_15        | string | [Message_Lang_Unk](mapdifficulty_dbc#messagelang)      | Unknown language, unsure of the usage in 3.3.5a                           |
| 19     | Message_lang_mask | uint32 | [Message_Lang_Mask](mapdifficulty_dbc#messagelang)     | Assumed flags of the localized text                                       |
| 20     | RaidDuration      | uint32 | [RaidDuration](mapdifficulty_dbc#raidduration)         |                                                                           |
| 21     | MaxPlayers        | uint32 | [MaxPlayers](mapdifficulty_dbc#maxplayers)             |                                                                           |
| 22     | Difficultystring  | string | [Difficultystring](mapdifficulty_dbc#difficultystring) |                                                                           |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/MapDifficulty).
