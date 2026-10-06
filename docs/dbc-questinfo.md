# QuestInfo.dbc

[`Back-to:DBC`](dbc-index)

**The \`QuestInfo.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment                                         |
| :----: | :----------------- | :----- | :---------------------------------------------- |
| 0      | ID                 | uint32 |                                                 |
| 1      | InfoName_0         | string | Assumed enUS                                    |
| 2      | InfoName_1         | string | Assumed enGB, not used in 3.3.5a                |
| 3      | InfoName_2         | string | Assumed koKR                                    |
| 4      | InfoName_3         | string | Assumed frFR                                    |
| 5      | InfoName_4         | string | Assumed deDE                                    |
| 6      | InfoName_5         | string | Assumed enCN, not used in 3.3.5a                |
| 7      | InfoName_6         | string | Assumed zhCN                                    |
| 8      | InfoName_7         | string | Assumed enTW, not used in 3.3.5a                |
| 9      | InfoName_8         | string | Assumed zhTW                                    |
| 10     | InfoName_9         | string | Assumed esES                                    |
| 11     | InfoName_10        | string | Assumed esMX                                    |
| 12     | InfoName_11        | string | Assumed ruRU                                    |
| 13     | InfoName_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 14     | InfoName_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 15     | InfoName_14        | string | Assumed itIT, not used in 3.3.5a                |
| 16     | InfoName_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 17     | InfoName_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/QuestInfo).
