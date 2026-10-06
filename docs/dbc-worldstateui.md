# WorldStateUI.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldStateUI.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                     | Type   | Comment                                         |
| :----: | :------------------------ | :----- | :---------------------------------------------- |
| 0      | ID                        | uint32 |                                                 |
| 1      | MapID                     | uint32 | ID in [Map.dbc](map)                            |
| 2      | AreaID                    | uint32 | ID in [AreaTable.dbc](areatable)                |
| 3      | PhaseShift                | uint32 |                                                 |
| 4      | Icon                      | string |                                                 |
| 5      | String_0                  | string | Assumed enUS                                    |
| 6      | String_1                  | string | Assumed enGB, not used in 3.3.5a                |
| 7      | String_2                  | string | Assumed koKR                                    |
| 8      | String_3                  | string | Assumed frFR                                    |
| 9      | String_4                  | string | Assumed deDE                                    |
| 10     | String_5                  | string | Assumed enCN, not used in 3.3.5a                |
| 11     | String_6                  | string | Assumed zhCN                                    |
| 12     | String_7                  | string | Assumed enTW, not used in 3.3.5a                |
| 13     | String_8                  | string | Assumed zhTW                                    |
| 14     | String_9                  | string | Assumed esES                                    |
| 15     | String_10                 | string | Assumed esMX                                    |
| 16     | String_11                 | string | Assumed ruRU                                    |
| 17     | String_12                 | string | Assumed ptPT, not used in 3.3.5a                |
| 18     | String_13                 | string | Assumed ptBR, not used in 3.3.5a                |
| 19     | String_14                 | string | Assumed itIT, not used in 3.3.5a                |
| 20     | String_15                 | string | Unknown language, unsure of the usage in 3.3.5a |
| 21     | String_lang_mask          | uint32 | Assumed flags of the localized text             |
| 22     | Tooltip_0                 | string | Assumed enUS                                    |
| 23     | Tooltip_1                 | string | Assumed enGB, not used in 3.3.5a                |
| 24     | Tooltip_2                 | string | Assumed koKR                                    |
| 25     | Tooltip_3                 | string | Assumed frFR                                    |
| 26     | Tooltip_4                 | string | Assumed deDE                                    |
| 27     | Tooltip_5                 | string | Assumed enCN, not used in 3.3.5a                |
| 28     | Tooltip_6                 | string | Assumed zhCN                                    |
| 29     | Tooltip_7                 | string | Assumed enTW, not used in 3.3.5a                |
| 30     | Tooltip_8                 | string | Assumed zhTW                                    |
| 31     | Tooltip_9                 | string | Assumed esES                                    |
| 32     | Tooltip_10                | string | Assumed esMX                                    |
| 33     | Tooltip_11                | string | Assumed ruRU                                    |
| 34     | Tooltip_12                | string | Assumed ptPT, not used in 3.3.5a                |
| 35     | Tooltip_13                | string | Assumed ptBR, not used in 3.3.5a                |
| 36     | Tooltip_14                | string | Assumed itIT, not used in 3.3.5a                |
| 37     | Tooltip_15                | string | Unknown language, unsure of the usage in 3.3.5a |
| 38     | Tooltip_lang_mask         | uint32 | Assumed flags of the localized text             |
| 39     | StateVariable             | uint32 |                                                 |
| 40     | Type                      | uint32 |                                                 |
| 41     | DynamicIcon               | string |                                                 |
| 42     | DynamicTooltip_0          | string | Assumed enUS                                    |
| 43     | DynamicTooltip_1          | string | Assumed enGB, not used in 3.3.5a                |
| 44     | DynamicTooltip_2          | string | Assumed koKR                                    |
| 45     | DynamicTooltip_3          | string | Assumed frFR                                    |
| 46     | DynamicTooltip_4          | string | Assumed deDE                                    |
| 47     | DynamicTooltip_5          | string | Assumed enCN, not used in 3.3.5a                |
| 48     | DynamicTooltip_6          | string | Assumed zhCN                                    |
| 49     | DynamicTooltip_7          | string | Assumed enTW, not used in 3.3.5a                |
| 50     | DynamicTooltip_8          | string | Assumed zhTW                                    |
| 51     | DynamicTooltip_9          | string | Assumed esES                                    |
| 52     | DynamicTooltip_10         | string | Assumed esMX                                    |
| 53     | DynamicTooltip_11         | string | Assumed ruRU                                    |
| 54     | DynamicTooltip_12         | string | Assumed ptPT, not used in 3.3.5a                |
| 55     | DynamicTooltip_13         | string | Assumed ptBR, not used in 3.3.5a                |
| 56     | DynamicTooltip_14         | string | Assumed itIT, not used in 3.3.5a                |
| 57     | DynamicTooltip_15         | string | Unknown language, unsure of the usage in 3.3.5a |
| 58     | DynamicTooltip_lang_mask  | uint32 | Assumed flags of the localized text             |
| 59     | ExtendedUI                | string |                                                 |
| 60     | ExtendedUIStateVariable_0 | uint32 |                                                 |
| 61     | ExtendedUIStateVariable_1 | uint32 |                                                 |
| 62     | ExtendedUIStateVariable_2 | uint32 |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldStateUI).
