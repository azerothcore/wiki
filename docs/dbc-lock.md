# Lock.dbc

[`Back-to:DBC`](dbc-index)

**The \`Lock.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [lock_dbc](lock_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | lock\_dbc column            | Comment |
| :----: | :------- | :----- | :-------------------------- | :------ |
| 0      | ID       | uint32 | [ID](lock_dbc#id)           |         |
| 1      | Type_0   | uint32 | [Type_1](lock_dbc#type)     |         |
| 2      | Type_1   | uint32 | [Type_2](lock_dbc#type)     |         |
| 3      | Type_2   | uint32 | [Type_3](lock_dbc#type)     |         |
| 4      | Type_3   | uint32 | [Type_4](lock_dbc#type)     |         |
| 5      | Type_4   | uint32 | [Type_5](lock_dbc#type)     |         |
| 6      | Type_5   | uint32 | [Type_6](lock_dbc#type)     |         |
| 7      | Type_6   | uint32 | [Type_7](lock_dbc#type)     |         |
| 8      | Type_7   | uint32 | [Type_8](lock_dbc#type)     |         |
| 9      | Index_0  | uint32 | [Index_1](lock_dbc#index)   |         |
| 10     | Index_1  | uint32 | [Index_2](lock_dbc#index)   |         |
| 11     | Index_2  | uint32 | [Index_3](lock_dbc#index)   |         |
| 12     | Index_3  | uint32 | [Index_4](lock_dbc#index)   |         |
| 13     | Index_4  | uint32 | [Index_5](lock_dbc#index)   |         |
| 14     | Index_5  | uint32 | [Index_6](lock_dbc#index)   |         |
| 15     | Index_6  | uint32 | [Index_7](lock_dbc#index)   |         |
| 16     | Index_7  | uint32 | [Index_8](lock_dbc#index)   |         |
| 17     | Skill_0  | uint32 | [Skill_1](lock_dbc#skill)   |         |
| 18     | Skill_1  | uint32 | [Skill_2](lock_dbc#skill)   |         |
| 19     | Skill_2  | uint32 | [Skill_3](lock_dbc#skill)   |         |
| 20     | Skill_3  | uint32 | [Skill_4](lock_dbc#skill)   |         |
| 21     | Skill_4  | uint32 | [Skill_5](lock_dbc#skill)   |         |
| 22     | Skill_5  | uint32 | [Skill_6](lock_dbc#skill)   |         |
| 23     | Skill_6  | uint32 | [Skill_7](lock_dbc#skill)   |         |
| 24     | Skill_7  | uint32 | [Skill_8](lock_dbc#skill)   |         |
| 25     | Action_0 | uint32 | [Action_1](lock_dbc#action) |         |
| 26     | Action_1 | uint32 | [Action_2](lock_dbc#action) |         |
| 27     | Action_2 | uint32 | [Action_3](lock_dbc#action) |         |
| 28     | Action_3 | uint32 | [Action_4](lock_dbc#action) |         |
| 29     | Action_4 | uint32 | [Action_5](lock_dbc#action) |         |
| 30     | Action_5 | uint32 | [Action_6](lock_dbc#action) |         |
| 31     | Action_6 | uint32 | [Action_7](lock_dbc#action) |         |
| 32     | Action_7 | uint32 | [Action_8](lock_dbc#action) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Lock).
