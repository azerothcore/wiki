# TaxiNodes.dbc

[`Back-to:DBC`](dbc-index)

**The \`TaxiNodes.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [taxinodes_dbc](taxinodes_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | Comment |
| :----: | :---------------- | :----- | :------ |
| 0      | ID                | uint32 |         |
| 1      | ContinentID       | uint32 |         |
| 2      | Pos_X             | float  |         |
| 3      | Pos_Y             | float  |         |
| 4      | Pos_Z             | float  |         |
| 5      | Name_0            | string |         |
| 6      | Name_1            | string |         |
| 7      | Name_2            | string |         |
| 8      | Name_3            | string |         |
| 9      | Name_4            | string |         |
| 10     | Name_5            | string |         |
| 11     | Name_6            | string |         |
| 12     | Name_7            | string |         |
| 13     | Name_8            | string |         |
| 14     | Name_9            | string |         |
| 15     | Name_10           | string |         |
| 16     | Name_11           | string |         |
| 17     | Name_12           | string |         |
| 18     | Name_13           | string |         |
| 19     | Name_14           | string |         |
| 20     | Name_15           | string |         |
| 21     | Name_16           | string |         |
| 22     | Name_lang_mask    | uint32 |         |
| 23     | MountCreatureID_0 | uint32 |         |
| 24     | MountCreatureID_1 | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TaxiNodes).
