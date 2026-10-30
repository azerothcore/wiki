# DanceMoves.dbc

[`Back-to:DBC`](dbc-index)

**The \`DanceMoves.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field          | Type   | Comment                                         |
| :----: | :------------- | :----- | :---------------------------------------------- |
| 0      | ID             | uint32 |                                                 |
| 1      | Type           | uint32 |                                                 |
| 2      | Value          | uint32 |                                                 |
| 3      | Fallback       | uint32 |                                                 |
| 4      | Racemask       | uint32 | Race mask. See [ChrRaces.dbc](chrraces#content) |
| 5      | Internal       | string |                                                 |
| 6      | Name_0         | string | Assumed enUS                                    |
| 7      | Name_1         | string | Assumed enGB, not used in 3.3.5a                |
| 8      | Name_2         | string | Assumed koKR                                    |
| 9      | Name_3         | string | Assumed frFR                                    |
| 10     | Name_4         | string | Assumed deDE                                    |
| 11     | Name_5         | string | Assumed enCN, not used in 3.3.5a                |
| 12     | Name_6         | string | Assumed zhCN                                    |
| 13     | Name_7         | string | Assumed enTW, not used in 3.3.5a                |
| 14     | Name_8         | string | Assumed zhTW                                    |
| 15     | Name_9         | string | Assumed esES                                    |
| 16     | Name_10        | string | Assumed esMX                                    |
| 17     | Name_11        | string | Assumed ruRU                                    |
| 18     | Name_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 19     | Name_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 20     | Name_14        | string | Assumed itIT, not used in 3.3.5a                |
| 21     | Name_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 22     | Name_lang_mask | uint32 | Assumed flags of the localized text             |
| 23     | LockID         | uint32 |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DanceMoves).
