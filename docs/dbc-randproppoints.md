# RandPropPoints.dbc

[`Back-to:DBC`](dbc-index)

**The \`RandPropPoints.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [randproppoints_dbc](randproppoints_dbc) table of the world database.

**Structure**

| Column | Field      | Type   | randproppoints\_dbc column                | Comment |
| :----: | :--------- | :----- | :---------------------------------------- | :------ |
| 0      | ID         | uint32 | [ID](randproppoints_dbc#id)               |         |
| 1      | Epic_0     | uint32 | [Epic_1](randproppoints_dbc#epic)         |         |
| 2      | Epic_1     | uint32 | [Epic_2](randproppoints_dbc#epic)         |         |
| 3      | Epic_2     | uint32 | [Epic_3](randproppoints_dbc#epic)         |         |
| 4      | Epic_3     | uint32 | [Epic_4](randproppoints_dbc#epic)         |         |
| 5      | Epic_4     | uint32 | [Epic_5](randproppoints_dbc#epic)         |         |
| 6      | Superior_0 | uint32 | [Superior_1](randproppoints_dbc#superior) |         |
| 7      | Superior_1 | uint32 | [Superior_2](randproppoints_dbc#superior) |         |
| 8      | Superior_2 | uint32 | [Superior_3](randproppoints_dbc#superior) |         |
| 9      | Superior_3 | uint32 | [Superior_4](randproppoints_dbc#superior) |         |
| 10     | Superior_4 | uint32 | [Superior_5](randproppoints_dbc#superior) |         |
| 11     | Good_0     | uint32 | [Good_1](randproppoints_dbc#good)         |         |
| 12     | Good_1     | uint32 | [Good_2](randproppoints_dbc#good)         |         |
| 13     | Good_2     | uint32 | [Good_3](randproppoints_dbc#good)         |         |
| 14     | Good_3     | uint32 | [Good_4](randproppoints_dbc#good)         |         |
| 15     | Good_4     | uint32 | [Good_5](randproppoints_dbc#good)         |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/RandPropPoints).
