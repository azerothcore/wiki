# Package.dbc

[`Back-to:DBC`](dbc-index)

**The \`Package.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                 | Type   | Comment                                         |
| :----: | :-------------------- | :----- | :---------------------------------------------- |
| 0      | ID                    | uint32 |                                                 |
| 1      | Icon                  | string |                                                 |
| 2      | Cost                  | uint32 |                                                 |
| 3      | Description_0         | string | Assumed enUS                                    |
| 4      | Description_1         | string | Assumed enGB, not used in 3.3.5a                |
| 5      | Description_2         | string | Assumed koKR                                    |
| 6      | Description_3         | string | Assumed frFR                                    |
| 7      | Description_4         | string | Assumed deDE                                    |
| 8      | Description_5         | string | Assumed enCN, not used in 3.3.5a                |
| 9      | Description_6         | string | Assumed zhCN                                    |
| 10     | Description_7         | string | Assumed enTW, not used in 3.3.5a                |
| 11     | Description_8         | string | Assumed zhTW                                    |
| 12     | Description_9         | string | Assumed esES                                    |
| 13     | Description_10        | string | Assumed esMX                                    |
| 14     | Description_11        | string | Assumed ruRU                                    |
| 15     | Description_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 16     | Description_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 17     | Description_14        | string | Assumed itIT, not used in 3.3.5a                |
| 18     | Description_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 19     | Description_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Package).
