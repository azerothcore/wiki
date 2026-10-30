# TerrainType.dbc

[`Back-to:DBC`](dbc-index)

**The \`TerrainType.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field             | Type   | Comment                                              |
| :----: | :---------------- | :----- | :--------------------------------------------------- |
| 0      | ID                | uint32 |                                                      |
| 1      | Description       | string |                                                      |
| 2      | FootstepSprayRun  | uint32 |                                                      |
| 3      | FootstepSprayWalk | uint32 |                                                      |
| 4      | TerrainSoundID    | uint32 | ID in [TerrainTypeSounds.dbc](dbc-terraintypesounds) |
| 5      | Flags             | uint32 |                                                      |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TerrainType).
