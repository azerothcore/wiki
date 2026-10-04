# MapDifficulty.dbc

[`Back-to:DBC`](dbc-index)

**The \`MapDifficulty.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [mapdifficulty_dbc](mapdifficulty_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | mapdifficulty\_dbc column                              | Comment |
| :----: | :---------------- | :----- | :----------------------------------------------------- | :------ |
| 0      | ID                | uint32 | [ID](mapdifficulty_dbc#id)                             |         |
| 1      | MapID             | uint32 | [MapID](mapdifficulty_dbc#mapid)                       |         |
| 2      | Difficulty        | uint32 | [Difficulty](mapdifficulty_dbc#difficulty)             |         |
| 3      | Message_0         | string | [Message_Lang_enUS](mapdifficulty_dbc#messagelang)     |         |
| 4      | Message_1         | string | [Message_Lang_enGB](mapdifficulty_dbc#messagelang)     |         |
| 5      | Message_2         | string | [Message_Lang_koKR](mapdifficulty_dbc#messagelang)     |         |
| 6      | Message_3         | string | [Message_Lang_frFR](mapdifficulty_dbc#messagelang)     |         |
| 7      | Message_4         | string | [Message_Lang_deDE](mapdifficulty_dbc#messagelang)     |         |
| 8      | Message_5         | string | [Message_Lang_enCN](mapdifficulty_dbc#messagelang)     |         |
| 9      | Message_6         | string | [Message_Lang_zhCN](mapdifficulty_dbc#messagelang)     |         |
| 10     | Message_7         | string | [Message_Lang_enTW](mapdifficulty_dbc#messagelang)     |         |
| 11     | Message_8         | string | [Message_Lang_zhTW](mapdifficulty_dbc#messagelang)     |         |
| 12     | Message_9         | string | [Message_Lang_esES](mapdifficulty_dbc#messagelang)     |         |
| 13     | Message_10        | string | [Message_Lang_esMX](mapdifficulty_dbc#messagelang)     |         |
| 14     | Message_11        | string | [Message_Lang_ruRU](mapdifficulty_dbc#messagelang)     |         |
| 15     | Message_12        | string | [Message_Lang_ptPT](mapdifficulty_dbc#messagelang)     |         |
| 16     | Message_13        | string | [Message_Lang_ptBR](mapdifficulty_dbc#messagelang)     |         |
| 17     | Message_14        | string | [Message_Lang_itIT](mapdifficulty_dbc#messagelang)     |         |
| 18     | Message_15        | string | [Message_Lang_Unk](mapdifficulty_dbc#messagelang)      |         |
| 19     | Message_lang_mask | uint32 | [Message_Lang_Mask](mapdifficulty_dbc#messagelang)     |         |
| 20     | RaidDuration      | uint32 | [RaidDuration](mapdifficulty_dbc#raidduration)         |         |
| 21     | MaxPlayers        | uint32 | [MaxPlayers](mapdifficulty_dbc#maxplayers)             |         |
| 22     | Difficultystring  | string | [Difficultystring](mapdifficulty_dbc#difficultystring) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/MapDifficulty).
