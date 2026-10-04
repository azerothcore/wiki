# Achievement\_Category.dbc

[`Back-to:DBC`](dbc-index)

**The \`Achievement\_Category.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [achievement_category_dbc](achievement_category_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | achievement\_category\_dbc column                   | Comment |
| :----: | :------------- | :----- | :-------------------------------------------------- | :------ |
| 0      | ID             | uint32 | [ID](achievement_category_dbc#id)                   |         |
| 1      | ParentID       | uint32 | [Parent](achievement_category_dbc#parent)           |         |
| 2      | Name_0         | string | [Name_Lang_enUS](achievement_category_dbc#namelang) |         |
| 3      | Name_1         | string | [Name_Lang_enGB](achievement_category_dbc#namelang) |         |
| 4      | Name_2         | string | [Name_Lang_koKR](achievement_category_dbc#namelang) |         |
| 5      | Name_3         | string | [Name_Lang_frFR](achievement_category_dbc#namelang) |         |
| 6      | Name_4         | string | [Name_Lang_deDE](achievement_category_dbc#namelang) |         |
| 7      | Name_5         | string | [Name_Lang_enCN](achievement_category_dbc#namelang) |         |
| 8      | Name_6         | string | [Name_Lang_zhCN](achievement_category_dbc#namelang) |         |
| 9      | Name_7         | string | [Name_Lang_enTW](achievement_category_dbc#namelang) |         |
| 10     | Name_8         | string | [Name_Lang_zhTW](achievement_category_dbc#namelang) |         |
| 11     | Name_9         | string | [Name_Lang_esES](achievement_category_dbc#namelang) |         |
| 12     | Name_10        | string | [Name_Lang_esMX](achievement_category_dbc#namelang) |         |
| 13     | Name_11        | string | [Name_Lang_ruRU](achievement_category_dbc#namelang) |         |
| 14     | Name_12        | string | [Name_Lang_ptPT](achievement_category_dbc#namelang) |         |
| 15     | Name_13        | string | [Name_Lang_ptBR](achievement_category_dbc#namelang) |         |
| 16     | Name_14        | string | [Name_Lang_itIT](achievement_category_dbc#namelang) |         |
| 17     | Name_15        | string | [Name_Lang_Unk](achievement_category_dbc#namelang)  |         |
| 18     | Name_lang_mask | uint32 | [Name_Lang_Mask](achievement_category_dbc#namelang) |         |
| 19     | UiOrder        | uint32 | [Ui_Order](achievement_category_dbc#uiorder)        |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Achievement_Category).
