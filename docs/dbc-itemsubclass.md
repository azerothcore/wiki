# ItemSubClass.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemSubClass.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                    | Type   | Comment                                                  |
| :----: | :----------------------- | :----- | :------------------------------------------------------- |
| 0      | ClassID                  | uint32 |                                                          |
| 1      | SubClassID               | uint32 | ID in [SheatheSoundLookups.dbc](dbc-sheathesoundlookups) |
| 2      | PrerequisiteProficiency  | int32  |                                                          |
| 3      | PostrequisiteProficiency | int32  |                                                          |
| 4      | Flags                    | uint32 |                                                          |
| 5      | DisplayFlags             | uint32 |                                                          |
| 6      | WeaponParrySeq           | uint32 |                                                          |
| 7      | WeaponReadySeq           | uint32 |                                                          |
| 8      | WeaponAttackSeq          | uint32 |                                                          |
| 9      | WeaponSwingSize          | uint32 | ID in [WeaponSwingSounds2.dbc](dbc-weaponswingsounds2)   |
| 10     | DisplayName_0            | string | Assumed enUS                                             |
| 11     | DisplayName_1            | string | Assumed enGB, not used in 3.3.5a                         |
| 12     | DisplayName_2            | string | Assumed koKR                                             |
| 13     | DisplayName_3            | string | Assumed frFR                                             |
| 14     | DisplayName_4            | string | Assumed deDE                                             |
| 15     | DisplayName_5            | string | Assumed enCN, not used in 3.3.5a                         |
| 16     | DisplayName_6            | string | Assumed zhCN                                             |
| 17     | DisplayName_7            | string | Assumed enTW, not used in 3.3.5a                         |
| 18     | DisplayName_8            | string | Assumed zhTW                                             |
| 19     | DisplayName_9            | string | Assumed esES                                             |
| 20     | DisplayName_10           | string | Assumed esMX                                             |
| 21     | DisplayName_11           | string | Assumed ruRU                                             |
| 22     | DisplayName_12           | string | Assumed ptPT, not used in 3.3.5a                         |
| 23     | DisplayName_13           | string | Assumed ptBR, not used in 3.3.5a                         |
| 24     | DisplayName_14           | string | Assumed itIT, not used in 3.3.5a                         |
| 25     | DisplayName_15           | string | Unknown language, unsure of the usage in 3.3.5a          |
| 26     | DisplayName_lang_mask    | uint32 | Assumed flags of the localized text                      |
| 27     | VerboseName_0            | string | Assumed enUS                                             |
| 28     | VerboseName_1            | string | Assumed enGB, not used in 3.3.5a                         |
| 29     | VerboseName_2            | string | Assumed koKR                                             |
| 30     | VerboseName_3            | string | Assumed frFR                                             |
| 31     | VerboseName_4            | string | Assumed deDE                                             |
| 32     | VerboseName_5            | string | Assumed enCN, not used in 3.3.5a                         |
| 33     | VerboseName_6            | string | Assumed zhCN                                             |
| 34     | VerboseName_7            | string | Assumed enTW, not used in 3.3.5a                         |
| 35     | VerboseName_8            | string | Assumed zhTW                                             |
| 36     | VerboseName_9            | string | Assumed esES                                             |
| 37     | VerboseName_10           | string | Assumed esMX                                             |
| 38     | VerboseName_11           | string | Assumed ruRU                                             |
| 39     | VerboseName_12           | string | Assumed ptPT, not used in 3.3.5a                         |
| 40     | VerboseName_13           | string | Assumed ptBR, not used in 3.3.5a                         |
| 41     | VerboseName_14           | string | Assumed itIT, not used in 3.3.5a                         |
| 42     | VerboseName_15           | string | Unknown language, unsure of the usage in 3.3.5a          |
| 43     | VerboseName_lang_mask    | uint32 | Assumed flags of the localized text                      |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemSubClass).
