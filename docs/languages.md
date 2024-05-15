---
redirect_from: "/Languages"
---

# Languages

[`Back-to:DBC`](dbc-index.md)

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

**DBC Structure - For Version 3.3.5a**

This DBC contains languages that can be used in texts. The player must have competence in this language to understand what is written.

| Column | Type  | Notes                                   |
|--------|-------|-----------------------------------------|
| 1      | long  | The ID of the language. Must be unique. |
| 2      | str   | The name of the language goes here.     |
| 18     | flags | The purpose of this column is unknown.  |

Any unlisted columns are not used within the DBC file.

**DBC Contents - For Version 3.3.5a**

All of the races, along with their IDs, from the *Languages.dbc* file are as follows.

| ID | Name           |
|----|----------------|
| 1  | Orcish         |
| 2  | Darnassian     |
| 3  | Taurahe        |
| 6  | Dwarvish       |
| 7  | Common         |
| 8  | Demonic        |
| 9  | Titan          |
| 10 | Thalassian     |
| 11 | Draconic       |
| 12 | Kalimag        |
| 13 | Gnomish        |
| 14 | Troll          |
| 33 | Gutterspeak    |
| 35 | Draenei        |
| 36 | Zombie         |
| 37 | Gnomish Binary |
| 38 | Goblin Binary  |
