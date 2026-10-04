# QuestXP.dbc

[`Back-to:DBC`](dbc-index)

**The \`QuestXP.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [questxp_dbc](questxp_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | questxp\_dbc column                     | Comment |
| :----: | :----------- | :----- | :-------------------------------------- | :------ |
| 0      | ID           | uint32 | [ID](questxp_dbc#id)                    |         |
| 1      | Difficulty_0 | uint32 | [Difficulty_1](questxp_dbc#difficulty)  |         |
| 2      | Difficulty_1 | uint32 | [Difficulty_2](questxp_dbc#difficulty)  |         |
| 3      | Difficulty_2 | uint32 | [Difficulty_3](questxp_dbc#difficulty)  |         |
| 4      | Difficulty_3 | uint32 | [Difficulty_4](questxp_dbc#difficulty)  |         |
| 5      | Difficulty_4 | uint32 | [Difficulty_5](questxp_dbc#difficulty)  |         |
| 6      | Difficulty_5 | uint32 | [Difficulty_6](questxp_dbc#difficulty)  |         |
| 7      | Difficulty_6 | uint32 | [Difficulty_7](questxp_dbc#difficulty)  |         |
| 8      | Difficulty_7 | uint32 | [Difficulty_8](questxp_dbc#difficulty)  |         |
| 9      | Difficulty_8 | uint32 | [Difficulty_9](questxp_dbc#difficulty)  |         |
| 10     | Difficulty_9 | uint32 | [Difficulty_10](questxp_dbc#difficulty) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/QuestXP).
