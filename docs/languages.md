---
redirect_from: "/Languages"
---

# Languages

[`Back-to:DBC`](dbc-index)

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**DBC Structure - For Version 3.3.5a**

This DBC contains languages that can be used in texts. The player must have competence in this language to understand what is written.

| Column | Field          | Type   | Comment                                                                    |
| :----: | :------------- | :----- | :------------------------------------------------------------------------- |
| 0      | ID             | uint32 | The ID of the language. Must be unique.                                    |
| 1      | Name_0         | string | The name of the language goes here. Assumed enUS                           |
| 2      | Name_1         | string | Assumed enGB, not used in 3.3.5a                                           |
| 3      | Name_2         | string | Assumed koKR                                                               |
| 4      | Name_3         | string | Assumed frFR                                                               |
| 5      | Name_4         | string | Assumed deDE                                                               |
| 6      | Name_5         | string | Assumed enCN, not used in 3.3.5a                                           |
| 7      | Name_6         | string | Assumed zhCN                                                               |
| 8      | Name_7         | string | Assumed enTW, not used in 3.3.5a                                           |
| 9      | Name_8         | string | Assumed zhTW                                                               |
| 10     | Name_9         | string | Assumed esES                                                               |
| 11     | Name_10        | string | Assumed esMX                                                               |
| 12     | Name_11        | string | Assumed ruRU                                                               |
| 13     | Name_12        | string | Assumed ptPT, not used in 3.3.5a                                           |
| 14     | Name_13        | string | Assumed ptBR, not used in 3.3.5a                                           |
| 15     | Name_14        | string | Assumed itIT, not used in 3.3.5a                                           |
| 16     | Name_15        | string | Unknown language, unsure of the usage in 3.3.5a                            |
| 17     | Name_lang_mask | uint32 | The purpose of this column is unknown. Assumed flags of the localized text |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

Any unlisted columns are not used within the DBC file.

**DBC Contents - For Version 3.3.5a**

All of the races, along with their IDs, from the *Languages.dbc* file are as follows.

<details>
<summary>Show the content of Languages.dbc</summary>

| ID  | Name           |
| --- | -------------- |
| 1   | Orcish         |
| 2   | Darnassian     |
| 3   | Taurahe        |
| 6   | Dwarvish       |
| 7   | Common         |
| 8   | Demonic        |
| 9   | Titan          |
| 10  | Thalassian     |
| 11  | Draconic       |
| 12  | Kalimag        |
| 13  | Gnomish        |
| 14  | Troll          |
| 33  | Gutterspeak    |
| 35  | Draenei        |
| 36  | Zombie         |
| 37  | Gnomish Binary |
| 38  | Goblin Binary  |

</details>
