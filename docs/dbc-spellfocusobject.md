# SpellFocusObject.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellFocusObject.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellfocusobject_dbc](spellfocusobject_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | spellfocusobject\_dbc column                    | Comment |
| :----: | :------------- | :----- | :---------------------------------------------- | :------ |
| 0      | ID             | uint32 | [ID](spellfocusobject_dbc#id)                   |         |
| 1      | Name_0         | string | [Name_Lang_enUS](spellfocusobject_dbc#namelang) |         |
| 2      | Name_1         | string | [Name_Lang_enGB](spellfocusobject_dbc#namelang) |         |
| 3      | Name_2         | string | [Name_Lang_koKR](spellfocusobject_dbc#namelang) |         |
| 4      | Name_3         | string | [Name_Lang_frFR](spellfocusobject_dbc#namelang) |         |
| 5      | Name_4         | string | [Name_Lang_deDE](spellfocusobject_dbc#namelang) |         |
| 6      | Name_5         | string | [Name_Lang_enCN](spellfocusobject_dbc#namelang) |         |
| 7      | Name_6         | string | [Name_Lang_zhCN](spellfocusobject_dbc#namelang) |         |
| 8      | Name_7         | string | [Name_Lang_enTW](spellfocusobject_dbc#namelang) |         |
| 9      | Name_8         | string | [Name_Lang_zhTW](spellfocusobject_dbc#namelang) |         |
| 10     | Name_9         | string | [Name_Lang_esES](spellfocusobject_dbc#namelang) |         |
| 11     | Name_10        | string | [Name_Lang_esMX](spellfocusobject_dbc#namelang) |         |
| 12     | Name_11        | string | [Name_Lang_ruRU](spellfocusobject_dbc#namelang) |         |
| 13     | Name_12        | string | [Name_Lang_ptPT](spellfocusobject_dbc#namelang) |         |
| 14     | Name_13        | string | [Name_Lang_ptBR](spellfocusobject_dbc#namelang) |         |
| 15     | Name_14        | string | [Name_Lang_itIT](spellfocusobject_dbc#namelang) |         |
| 16     | Name_15        | string | [Name_Lang_Unk](spellfocusobject_dbc#namelang)  |         |
| 17     | Name_lang_mask | uint32 | [Name_Lang_Mask](spellfocusobject_dbc#namelang) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellFocusObject).
