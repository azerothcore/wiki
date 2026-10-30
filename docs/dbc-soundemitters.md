# SoundEmitters.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundEmitters.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                  | Type   | Comment              |
| :----: | :--------------------- | :----- | :------------------- |
| 0      | ID                     | uint32 |                      |
| 1      | Position_X             | float  |                      |
| 2      | Position_Y             | float  |                      |
| 3      | Position_Z             | float  |                      |
| 4      | Direction_X            | float  |                      |
| 5      | Direction_Y            | float  |                      |
| 6      | Direction_Z            | float  |                      |
| 7      | SoundEntriesAdvancedID | uint32 |                      |
| 8      | MapID                  | uint32 | ID in [Map.dbc](map) |
| 9      | Name                   | string |                      |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundEmitters).
