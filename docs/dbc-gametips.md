# GameTips.dbc

[`Back-to:DBC`](dbc-index)

**The \`GameTips.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field          | Type   | Comment                                         |
| :----: | :------------- | :----- | :---------------------------------------------- |
| 0      | ID             | uint32 |                                                 |
| 1      | Text_0         | string | Assumed enUS                                    |
| 2      | Text_1         | string | Assumed enGB, not used in 3.3.5a                |
| 3      | Text_2         | string | Assumed koKR                                    |
| 4      | Text_3         | string | Assumed frFR                                    |
| 5      | Text_4         | string | Assumed deDE                                    |
| 6      | Text_5         | string | Assumed enCN, not used in 3.3.5a                |
| 7      | Text_6         | string | Assumed zhCN                                    |
| 8      | Text_7         | string | Assumed enTW, not used in 3.3.5a                |
| 9      | Text_8         | string | Assumed zhTW                                    |
| 10     | Text_9         | string | Assumed esES                                    |
| 11     | Text_10        | string | Assumed esMX                                    |
| 12     | Text_11        | string | Assumed ruRU                                    |
| 13     | Text_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 14     | Text_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 15     | Text_14        | string | Assumed itIT, not used in 3.3.5a                |
| 16     | Text_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 17     | Text_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GameTips).
