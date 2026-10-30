# Achievement\_Category.dbc

[`Back-to:DBC`](dbc-index)

**The \`Achievement\_Category.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [achievement_category_dbc](achievement_category_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | achievement\_category\_dbc column                   | Comment                                         |
| :----: | :------------- | :----- | :-------------------------------------------------- | :---------------------------------------------- |
| 0      | ID             | uint32 | [ID](achievement_category_dbc#id)                   |                                                 |
| 1      | ParentID       | uint32 | [Parent](achievement_category_dbc#parent)           |                                                 |
| 2      | Name_0         | string | [Name_Lang_enUS](achievement_category_dbc#namelang) | Assumed enUS                                    |
| 3      | Name_1         | string | [Name_Lang_enGB](achievement_category_dbc#namelang) | Assumed enGB, not used in 3.3.5a                |
| 4      | Name_2         | string | [Name_Lang_koKR](achievement_category_dbc#namelang) | Assumed koKR                                    |
| 5      | Name_3         | string | [Name_Lang_frFR](achievement_category_dbc#namelang) | Assumed frFR                                    |
| 6      | Name_4         | string | [Name_Lang_deDE](achievement_category_dbc#namelang) | Assumed deDE                                    |
| 7      | Name_5         | string | [Name_Lang_enCN](achievement_category_dbc#namelang) | Assumed enCN, not used in 3.3.5a                |
| 8      | Name_6         | string | [Name_Lang_zhCN](achievement_category_dbc#namelang) | Assumed zhCN                                    |
| 9      | Name_7         | string | [Name_Lang_enTW](achievement_category_dbc#namelang) | Assumed enTW, not used in 3.3.5a                |
| 10     | Name_8         | string | [Name_Lang_zhTW](achievement_category_dbc#namelang) | Assumed zhTW                                    |
| 11     | Name_9         | string | [Name_Lang_esES](achievement_category_dbc#namelang) | Assumed esES                                    |
| 12     | Name_10        | string | [Name_Lang_esMX](achievement_category_dbc#namelang) | Assumed esMX                                    |
| 13     | Name_11        | string | [Name_Lang_ruRU](achievement_category_dbc#namelang) | Assumed ruRU                                    |
| 14     | Name_12        | string | [Name_Lang_ptPT](achievement_category_dbc#namelang) | Assumed ptPT, not used in 3.3.5a                |
| 15     | Name_13        | string | [Name_Lang_ptBR](achievement_category_dbc#namelang) | Assumed ptBR, not used in 3.3.5a                |
| 16     | Name_14        | string | [Name_Lang_itIT](achievement_category_dbc#namelang) | Assumed itIT, not used in 3.3.5a                |
| 17     | Name_15        | string | [Name_Lang_Unk](achievement_category_dbc#namelang)  | Unknown language, unsure of the usage in 3.3.5a |
| 18     | Name_lang_mask | uint32 | [Name_Lang_Mask](achievement_category_dbc#namelang) | Assumed flags of the localized text             |
| 19     | UiOrder        | uint32 | [Ui_Order](achievement_category_dbc#uiorder)        |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Achievement_Category).
