# DungeonMap.dbc

[`Back-to:DBC`](dbc-index)

**The \`DungeonMap.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                    |
| :----: | :--------------- | :----- | :----------------------------------------- |
| 0      | ID               | uint32 |                                            |
| 1      | MapID            | uint32 | ID in [Map.dbc](map)                       |
| 2      | FloorIndex       | uint32 |                                            |
| 3      | MinX             | float  |                                            |
| 4      | MaxX             | float  |                                            |
| 5      | MinY             | float  |                                            |
| 6      | MaxY             | float  |                                            |
| 7      | ParentWorldMapID | uint32 | ID in [WorldMapArea.dbc](dbc-worldmaparea) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DungeonMap).
