# CharTitles.dbc

[`Back-to:DBC`](dbc-index)

**The \`CharTitles.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [chartitles_dbc](chartitles_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | chartitles\_dbc column                      | Comment |
| :----: | :-------------- | :----- | :------------------------------------------ | :------ |
| 0      | ID              | uint32 | [ID](chartitles_dbc#id)                     |         |
| 1      | ConditionID     | uint32 | [Condition_ID](chartitles_dbc#conditionid)  |         |
| 2      | Name_0          | string | [Name_Lang_enUS](chartitles_dbc#namelang)   |         |
| 3      | Name_1          | string | [Name_Lang_enGB](chartitles_dbc#namelang)   |         |
| 4      | Name_2          | string | [Name_Lang_koKR](chartitles_dbc#namelang)   |         |
| 5      | Name_3          | string | [Name_Lang_frFR](chartitles_dbc#namelang)   |         |
| 6      | Name_4          | string | [Name_Lang_deDE](chartitles_dbc#namelang)   |         |
| 7      | Name_5          | string | [Name_Lang_enCN](chartitles_dbc#namelang)   |         |
| 8      | Name_6          | string | [Name_Lang_zhCN](chartitles_dbc#namelang)   |         |
| 9      | Name_7          | string | [Name_Lang_enTW](chartitles_dbc#namelang)   |         |
| 10     | Name_8          | string | [Name_Lang_zhTW](chartitles_dbc#namelang)   |         |
| 11     | Name_9          | string | [Name_Lang_esES](chartitles_dbc#namelang)   |         |
| 12     | Name_10         | string | [Name_Lang_esMX](chartitles_dbc#namelang)   |         |
| 13     | Name_11         | string | [Name_Lang_ruRU](chartitles_dbc#namelang)   |         |
| 14     | Name_12         | string | [Name_Lang_ptPT](chartitles_dbc#namelang)   |         |
| 15     | Name_13         | string | [Name_Lang_ptBR](chartitles_dbc#namelang)   |         |
| 16     | Name_14         | string | [Name_Lang_itIT](chartitles_dbc#namelang)   |         |
| 17     | Name_15         | string | [Name_Lang_Unk](chartitles_dbc#namelang)    |         |
| 18     | Name_lang_mask  | uint32 | [Name_Lang_Mask](chartitles_dbc#namelang)   |         |
| 19     | Name1_0         | string | [Name1_Lang_enUS](chartitles_dbc#name1lang) |         |
| 20     | Name1_1         | string | [Name1_Lang_enGB](chartitles_dbc#name1lang) |         |
| 21     | Name1_2         | string | [Name1_Lang_koKR](chartitles_dbc#name1lang) |         |
| 22     | Name1_3         | string | [Name1_Lang_frFR](chartitles_dbc#name1lang) |         |
| 23     | Name1_4         | string | [Name1_Lang_deDE](chartitles_dbc#name1lang) |         |
| 24     | Name1_5         | string | [Name1_Lang_enCN](chartitles_dbc#name1lang) |         |
| 25     | Name1_6         | string | [Name1_Lang_zhCN](chartitles_dbc#name1lang) |         |
| 26     | Name1_7         | string | [Name1_Lang_enTW](chartitles_dbc#name1lang) |         |
| 27     | Name1_8         | string | [Name1_Lang_zhTW](chartitles_dbc#name1lang) |         |
| 28     | Name1_9         | string | [Name1_Lang_esES](chartitles_dbc#name1lang) |         |
| 29     | Name1_10        | string | [Name1_Lang_esMX](chartitles_dbc#name1lang) |         |
| 30     | Name1_11        | string | [Name1_Lang_ruRU](chartitles_dbc#name1lang) |         |
| 31     | Name1_12        | string | [Name1_Lang_ptPT](chartitles_dbc#name1lang) |         |
| 32     | Name1_13        | string | [Name1_Lang_ptBR](chartitles_dbc#name1lang) |         |
| 33     | Name1_14        | string | [Name1_Lang_itIT](chartitles_dbc#name1lang) |         |
| 34     | Name1_15        | string | [Name1_Lang_Unk](chartitles_dbc#name1lang)  |         |
| 35     | Name1_lang_mask | uint32 | [Name1_Lang_Mask](chartitles_dbc#name1lang) |         |
| 36     | MaskID          | uint32 | [Mask_ID](chartitles_dbc#maskid)            |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CharTitles).
