# CharTitles.dbc

[`Back-to:DBC`](dbc-index)

**The \`CharTitles.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [chartitles_dbc](chartitles_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | chartitles\_dbc column                      | Comment                                         |
| :----: | :-------------- | :----- | :------------------------------------------ | :---------------------------------------------- |
| 0      | ID              | uint32 | [ID](chartitles_dbc#id)                     |                                                 |
| 1      | ConditionID     | uint32 | [Condition_ID](chartitles_dbc#conditionid)  |                                                 |
| 2      | Name_0          | string | [Name_Lang_enUS](chartitles_dbc#namelang)   | Assumed enUS                                    |
| 3      | Name_1          | string | [Name_Lang_enGB](chartitles_dbc#namelang)   | Assumed enGB, not used in 3.3.5a                |
| 4      | Name_2          | string | [Name_Lang_koKR](chartitles_dbc#namelang)   | Assumed koKR                                    |
| 5      | Name_3          | string | [Name_Lang_frFR](chartitles_dbc#namelang)   | Assumed frFR                                    |
| 6      | Name_4          | string | [Name_Lang_deDE](chartitles_dbc#namelang)   | Assumed deDE                                    |
| 7      | Name_5          | string | [Name_Lang_enCN](chartitles_dbc#namelang)   | Assumed enCN, not used in 3.3.5a                |
| 8      | Name_6          | string | [Name_Lang_zhCN](chartitles_dbc#namelang)   | Assumed zhCN                                    |
| 9      | Name_7          | string | [Name_Lang_enTW](chartitles_dbc#namelang)   | Assumed enTW, not used in 3.3.5a                |
| 10     | Name_8          | string | [Name_Lang_zhTW](chartitles_dbc#namelang)   | Assumed zhTW                                    |
| 11     | Name_9          | string | [Name_Lang_esES](chartitles_dbc#namelang)   | Assumed esES                                    |
| 12     | Name_10         | string | [Name_Lang_esMX](chartitles_dbc#namelang)   | Assumed esMX                                    |
| 13     | Name_11         | string | [Name_Lang_ruRU](chartitles_dbc#namelang)   | Assumed ruRU                                    |
| 14     | Name_12         | string | [Name_Lang_ptPT](chartitles_dbc#namelang)   | Assumed ptPT, not used in 3.3.5a                |
| 15     | Name_13         | string | [Name_Lang_ptBR](chartitles_dbc#namelang)   | Assumed ptBR, not used in 3.3.5a                |
| 16     | Name_14         | string | [Name_Lang_itIT](chartitles_dbc#namelang)   | Assumed itIT, not used in 3.3.5a                |
| 17     | Name_15         | string | [Name_Lang_Unk](chartitles_dbc#namelang)    | Unknown language, unsure of the usage in 3.3.5a |
| 18     | Name_lang_mask  | uint32 | [Name_Lang_Mask](chartitles_dbc#namelang)   | Assumed flags of the localized text             |
| 19     | Name1_0         | string | [Name1_Lang_enUS](chartitles_dbc#name1lang) | Assumed enUS                                    |
| 20     | Name1_1         | string | [Name1_Lang_enGB](chartitles_dbc#name1lang) | Assumed enGB, not used in 3.3.5a                |
| 21     | Name1_2         | string | [Name1_Lang_koKR](chartitles_dbc#name1lang) | Assumed koKR                                    |
| 22     | Name1_3         | string | [Name1_Lang_frFR](chartitles_dbc#name1lang) | Assumed frFR                                    |
| 23     | Name1_4         | string | [Name1_Lang_deDE](chartitles_dbc#name1lang) | Assumed deDE                                    |
| 24     | Name1_5         | string | [Name1_Lang_enCN](chartitles_dbc#name1lang) | Assumed enCN, not used in 3.3.5a                |
| 25     | Name1_6         | string | [Name1_Lang_zhCN](chartitles_dbc#name1lang) | Assumed zhCN                                    |
| 26     | Name1_7         | string | [Name1_Lang_enTW](chartitles_dbc#name1lang) | Assumed enTW, not used in 3.3.5a                |
| 27     | Name1_8         | string | [Name1_Lang_zhTW](chartitles_dbc#name1lang) | Assumed zhTW                                    |
| 28     | Name1_9         | string | [Name1_Lang_esES](chartitles_dbc#name1lang) | Assumed esES                                    |
| 29     | Name1_10        | string | [Name1_Lang_esMX](chartitles_dbc#name1lang) | Assumed esMX                                    |
| 30     | Name1_11        | string | [Name1_Lang_ruRU](chartitles_dbc#name1lang) | Assumed ruRU                                    |
| 31     | Name1_12        | string | [Name1_Lang_ptPT](chartitles_dbc#name1lang) | Assumed ptPT, not used in 3.3.5a                |
| 32     | Name1_13        | string | [Name1_Lang_ptBR](chartitles_dbc#name1lang) | Assumed ptBR, not used in 3.3.5a                |
| 33     | Name1_14        | string | [Name1_Lang_itIT](chartitles_dbc#name1lang) | Assumed itIT, not used in 3.3.5a                |
| 34     | Name1_15        | string | [Name1_Lang_Unk](chartitles_dbc#name1lang)  | Unknown language, unsure of the usage in 3.3.5a |
| 35     | Name1_lang_mask | uint32 | [Name1_Lang_Mask](chartitles_dbc#name1lang) | Assumed flags of the localized text             |
| 36     | MaskID          | uint32 | [Mask_ID](chartitles_dbc#maskid)            |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CharTitles).
