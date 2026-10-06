# WorldSafeLocs.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldSafeLocs.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment                                         |
| :----: | :----------------- | :----- | :---------------------------------------------- |
| 0      | ID                 | uint32 |                                                 |
| 1      | Continent          | uint32 | ID in [Map.dbc](map)                            |
| 2      | Loc_X              | float  |                                                 |
| 3      | Loc_Y              | float  |                                                 |
| 4      | Loc_Z              | float  |                                                 |
| 5      | AreaName_0         | string | Assumed enUS                                    |
| 6      | AreaName_1         | string | Assumed enGB, not used in 3.3.5a                |
| 7      | AreaName_2         | string | Assumed koKR                                    |
| 8      | AreaName_3         | string | Assumed frFR                                    |
| 9      | AreaName_4         | string | Assumed deDE                                    |
| 10     | AreaName_5         | string | Assumed enCN, not used in 3.3.5a                |
| 11     | AreaName_6         | string | Assumed zhCN                                    |
| 12     | AreaName_7         | string | Assumed enTW, not used in 3.3.5a                |
| 13     | AreaName_8         | string | Assumed zhTW                                    |
| 14     | AreaName_9         | string | Assumed esES                                    |
| 15     | AreaName_10        | string | Assumed esMX                                    |
| 16     | AreaName_11        | string | Assumed ruRU                                    |
| 17     | AreaName_12        | string | Assumed ptPT, not used in 3.3.5a                |
| 18     | AreaName_13        | string | Assumed ptBR, not used in 3.3.5a                |
| 19     | AreaName_14        | string | Assumed itIT, not used in 3.3.5a                |
| 20     | AreaName_15        | string | Unknown language, unsure of the usage in 3.3.5a |
| 21     | AreaName_lang_mask | uint32 | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldSafeLocs).
