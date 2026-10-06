# DungeonMapChunk.dbc

[`Back-to:DBC`](dbc-index)

**The \`DungeonMapChunk.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field        | Type   | Comment                                |
| :----: | :----------- | :----- | :------------------------------------- |
| 0      | ID           | uint32 |                                        |
| 1      | MapID        | uint32 | ID in [Map.dbc](map)                   |
| 2      | WMOGroupID   | uint32 |                                        |
| 3      | DungeonMapID | uint32 | ID in [DungeonMap.dbc](dbc-dungeonmap) |
| 4      | MinZ         | float  |                                        |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DungeonMapChunk).
