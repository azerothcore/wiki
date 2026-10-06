# ItemPurchaseGroup.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemPurchaseGroup.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field          | Type   | Comment                                         |
| :----: | :------------- | :----- | :---------------------------------------------- |
| 0      | ID             | uint32 |                                                 |
| 1      | ItemID_0       | uint32 | ID in [Item.dbc](dbc-item)                      |
| 2      | ItemID_1       | uint32 | ID in [Item.dbc](dbc-item)                      |
| 3      | ItemID_2       | uint32 | ID in [Item.dbc](dbc-item)                      |
| 4      | ItemID_3       | uint32 |                                                 |
| 5      | ItemID_4       | uint32 |                                                 |
| 6      | ItemID_5       | uint32 |                                                 |
| 7      | ItemID_6       | uint32 |                                                 |
| 8      | ItemID_7       | uint32 |                                                 |
| 9      | Name_0         | string | Assumed enUS                                    |
| 10     | Name_1         | string | Assumed enGB, not used in 3.3.5a                |
| 11     | Name_2         | string | Assumed koKR                                    |
| 12     | Name_3         | string | Assumed frFR                                    |
| 13     | Name_4         | string | Assumed deDE                                    |
| 14     | Name_5         | string | Assumed enCN, not used in 3.3.5a                |
| 15     | Name_6         | string | Assumed zhCN                                    |
| 16     | Name_7         | string | Assumed enTW, not used in 3.3.5a                |
| 17     | Name_8         | string | Assumed zhTW                                    |
| 18     | Name_9         | string | Assumed esES                                    |
| 19     | Name_10        | string | Assumed esMX                                    |
| 20     | Name_11        | string | Assumed ruRU                                    |
| 21     | Name_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 22     | Name_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 23     | Name_14        | string | Assumed itIT, not used in 3.3.5a                |
| 24     | Name_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 25     | Name_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemPurchaseGroup).
