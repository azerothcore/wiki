# WorldMapTransforms.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldMapTransforms.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field           | Type   | Comment                                |
| :----: | :-------------- | :----- | :------------------------------------- |
| 0      | ID              | uint32 |                                        |
| 1      | MapID           | uint32 | ID in [Map.dbc](map)                   |
| 2      | RegionBottom    | float  |                                        |
| 3      | RegionRight     | float  |                                        |
| 4      | RegionTop       | float  |                                        |
| 5      | RegionLeft      | float  |                                        |
| 6      | NewMapID        | uint32 | ID in [Map.dbc](map)                   |
| 7      | RegionOffset_X  | float  |                                        |
| 8      | RegionOffset_Y  | float  |                                        |
| 9      | NewDungeonMapID | uint32 | ID in [DungeonMap.dbc](dbc-dungeonmap) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldMapTransforms).
