# GroundEffectTexture.dbc

[`Back-to:DBC`](dbc-index)

**The \`GroundEffectTexture.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                                |
| :----: | :--------------- | :----- | :----------------------------------------------------- |
| 0      | ID               | uint32 |                                                        |
| 1      | GroundDoodadID_0 | uint32 | ID in [GroundEffectDoodad.dbc](dbc-groundeffectdoodad) |
| 2      | GroundDoodadID_1 | uint32 | ID in [GroundEffectDoodad.dbc](dbc-groundeffectdoodad) |
| 3      | GroundDoodadID_2 | uint32 | ID in [GroundEffectDoodad.dbc](dbc-groundeffectdoodad) |
| 4      | GroundDoodadID_3 | uint32 | ID in [GroundEffectDoodad.dbc](dbc-groundeffectdoodad) |
| 5      | DoodadWeight_0   | uint32 |                                                        |
| 6      | DoodadWeight_1   | uint32 |                                                        |
| 7      | DoodadWeight_2   | uint32 |                                                        |
| 8      | DoodadWeight_3   | uint32 |                                                        |
| 9      | Density          | uint32 |                                                        |
| 10     | TerrainID        | uint32 | ID in [TerrainType.dbc](dbc-terraintype)               |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GroundEffectTexture).
