# ItemLimitCategory.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemLimitCategory.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemlimitcategory_dbc](itemlimitcategory_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | itemlimitcategory\_dbc column                    | Comment                                         |
| :----: | :------------- | :----- | :----------------------------------------------- | :---------------------------------------------- |
| 0      | ID             | uint32 | [ID](itemlimitcategory_dbc#id)                   |                                                 |
| 1      | Name_0         | string | [Name_Lang_enUS](itemlimitcategory_dbc#namelang) | Assumed enUS                                    |
| 2      | Name_1         | string | [Name_Lang_enGB](itemlimitcategory_dbc#namelang) | Assumed enGB, not used in 3.3.5a                |
| 3      | Name_2         | string | [Name_Lang_koKR](itemlimitcategory_dbc#namelang) | Assumed koKR                                    |
| 4      | Name_3         | string | [Name_Lang_frFR](itemlimitcategory_dbc#namelang) | Assumed frFR                                    |
| 5      | Name_4         | string | [Name_Lang_deDE](itemlimitcategory_dbc#namelang) | Assumed deDE                                    |
| 6      | Name_5         | string | [Name_Lang_enCN](itemlimitcategory_dbc#namelang) | Assumed enCN, not used in 3.3.5a                |
| 7      | Name_6         | string | [Name_Lang_zhCN](itemlimitcategory_dbc#namelang) | Assumed zhCN                                    |
| 8      | Name_7         | string | [Name_Lang_enTW](itemlimitcategory_dbc#namelang) | Assumed enTW, not used in 3.3.5a                |
| 9      | Name_8         | string | [Name_Lang_zhTW](itemlimitcategory_dbc#namelang) | Assumed zhTW                                    |
| 10     | Name_9         | string | [Name_Lang_esES](itemlimitcategory_dbc#namelang) | Assumed esES                                    |
| 11     | Name_10        | string | [Name_Lang_esMX](itemlimitcategory_dbc#namelang) | Assumed esMX                                    |
| 12     | Name_11        | string | [Name_Lang_ruRU](itemlimitcategory_dbc#namelang) | Assumed ruRU                                    |
| 13     | Name_12        | string | [Name_Lang_ptPT](itemlimitcategory_dbc#namelang) | Assumed ptPT, not used in 3.3.5a                |
| 14     | Name_13        | string | [Name_Lang_ptBR](itemlimitcategory_dbc#namelang) | Assumed ptBR, not used in 3.3.5a                |
| 15     | Name_14        | string | [Name_Lang_itIT](itemlimitcategory_dbc#namelang) | Assumed itIT, not used in 3.3.5a                |
| 16     | Name_15        | string | [Name_Lang_Unk](itemlimitcategory_dbc#namelang)  | Unknown language, unsure of the usage in 3.3.5a |
| 17     | Name_lang_mask | uint32 | [Name_Lang_Mask](itemlimitcategory_dbc#namelang) | Assumed flags of the localized text             |
| 18     | Quantity       | uint32 | [Quantity](itemlimitcategory_dbc#quantity)       |                                                 |
| 19     | Flags          | uint32 | [Flags](itemlimitcategory_dbc#flags)             |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemLimitCategory).
