# LockType.dbc

[`Back-to:DBC`](dbc-index)

**The \`LockType.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                  | Type   | Comment                                         |
| :----: | :--------------------- | :----- | :---------------------------------------------- |
| 0      | ID                     | uint32 |                                                 |
| 1      | Name_0                 | string | Assumed enUS                                    |
| 2      | Name_1                 | string | Assumed enGB, not used in 3.3.5a                |
| 3      | Name_2                 | string | Assumed koKR                                    |
| 4      | Name_3                 | string | Assumed frFR                                    |
| 5      | Name_4                 | string | Assumed deDE                                    |
| 6      | Name_5                 | string | Assumed enCN, not used in 3.3.5a                |
| 7      | Name_6                 | string | Assumed zhCN                                    |
| 8      | Name_7                 | string | Assumed enTW, not used in 3.3.5a                |
| 9      | Name_8                 | string | Assumed zhTW                                    |
| 10     | Name_9                 | string | Assumed esES                                    |
| 11     | Name_10                | string | Assumed esMX                                    |
| 12     | Name_11                | string | Assumed ruRU                                    |
| 13     | Name_12                | string | Assumed ptPT, not used in 3.3.5a                |
| 14     | Name_13                | string | Assumed ptBR, not used in 3.3.5a                |
| 15     | Name_14                | string | Assumed itIT, not used in 3.3.5a                |
| 16     | Name_15                | string | Unknown language, unsure of the usage in 3.3.5a |
| 17     | Name_lang_mask         | uint32 | Assumed flags of the localized text             |
| 18     | ResourceName_0         | string | Assumed enUS                                    |
| 19     | ResourceName_1         | string | Assumed enGB, not used in 3.3.5a                |
| 20     | ResourceName_2         | string | Assumed koKR                                    |
| 21     | ResourceName_3         | string | Assumed frFR                                    |
| 22     | ResourceName_4         | string | Assumed deDE                                    |
| 23     | ResourceName_5         | string | Assumed enCN, not used in 3.3.5a                |
| 24     | ResourceName_6         | string | Assumed zhCN                                    |
| 25     | ResourceName_7         | string | Assumed enTW, not used in 3.3.5a                |
| 26     | ResourceName_8         | string | Assumed zhTW                                    |
| 27     | ResourceName_9         | string | Assumed esES                                    |
| 28     | ResourceName_10        | string | Assumed esMX                                    |
| 29     | ResourceName_11        | string | Assumed ruRU                                    |
| 30     | ResourceName_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 31     | ResourceName_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 32     | ResourceName_14        | string | Assumed itIT, not used in 3.3.5a                |
| 33     | ResourceName_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 34     | ResourceName_lang_mask | uint32 | Assumed flags of the localized text             |
| 35     | Verb_0                 | string | Assumed enUS                                    |
| 36     | Verb_1                 | string | Assumed enGB, not used in 3.3.5a                |
| 37     | Verb_2                 | string | Assumed koKR                                    |
| 38     | Verb_3                 | string | Assumed frFR                                    |
| 39     | Verb_4                 | string | Assumed deDE                                    |
| 40     | Verb_5                 | string | Assumed enCN, not used in 3.3.5a                |
| 41     | Verb_6                 | string | Assumed zhCN                                    |
| 42     | Verb_7                 | string | Assumed enTW, not used in 3.3.5a                |
| 43     | Verb_8                 | string | Assumed zhTW                                    |
| 44     | Verb_9                 | string | Assumed esES                                    |
| 45     | Verb_10                | string | Assumed esMX                                    |
| 46     | Verb_11                | string | Assumed ruRU                                    |
| 47     | Verb_12                | string | Assumed ptPT, not used in 3.3.5a                |
| 48     | Verb_13                | string | Assumed ptBR, not used in 3.3.5a                |
| 49     | Verb_14                | string | Assumed itIT, not used in 3.3.5a                |
| 50     | Verb_15                | string | Unknown language, unsure of the usage in 3.3.5a |
| 51     | Verb_lang_mask         | uint32 | Assumed flags of the localized text             |
| 52     | CursorName             | string |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LockType).
