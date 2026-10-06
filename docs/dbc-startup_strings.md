# Startup\_Strings.dbc

[`Back-to:DBC`](dbc-index)

**The \`Startup\_Strings.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field             | Type   | Comment                                         |
| :----: | :---------------- | :----- | :---------------------------------------------- |
| 0      | ID                | uint32 |                                                 |
| 1      | Name              | string |                                                 |
| 2      | Message_0         | string | Assumed enUS                                    |
| 3      | Message_1         | string | Assumed enGB, not used in 3.3.5a                |
| 4      | Message_2         | string | Assumed koKR                                    |
| 5      | Message_3         | string | Assumed frFR                                    |
| 6      | Message_4         | string | Assumed deDE                                    |
| 7      | Message_5         | string | Assumed enCN, not used in 3.3.5a                |
| 8      | Message_6         | string | Assumed zhCN                                    |
| 9      | Message_7         | string | Assumed enTW, not used in 3.3.5a                |
| 10     | Message_8         | string | Assumed zhTW                                    |
| 11     | Message_9         | string | Assumed esES                                    |
| 12     | Message_10        | string | Assumed esMX                                    |
| 13     | Message_11        | string | Assumed ruRU                                    |
| 14     | Message_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 15     | Message_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 16     | Message_14        | string | Assumed itIT, not used in 3.3.5a                |
| 17     | Message_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 18     | Message_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Startup_Strings).
