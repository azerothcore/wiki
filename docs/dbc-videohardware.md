# VideoHardware.dbc

[`Back-to:DBC`](dbc-index)

**The \`VideoHardware.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                  | Type   | Comment |
| :----: | :--------------------- | :----- | :------ |
| 0      | ID                     | uint32 |         |
| 1      | VendorID               | uint32 |         |
| 2      | DeviceID               | uint32 |         |
| 3      | FarclipIdx             | uint32 |         |
| 4      | TerrainLODDistIdx      | uint32 |         |
| 5      | TerrainShadowLOD       | uint32 |         |
| 6      | DetailDoodadDensityIdx | uint32 |         |
| 7      | DetailDoodadAlpha      | uint32 |         |
| 8      | AnimatingDoodadIdx     | uint32 |         |
| 9      | Trilinear              | uint32 |         |
| 10     | NumLights              | uint32 |         |
| 11     | Specularity            | uint32 |         |
| 12     | WaterLODIdx            | uint32 |         |
| 13     | ParticleDensityIdx     | uint32 |         |
| 14     | UnitDrawDistIdx        | uint32 |         |
| 15     | SmallCullDistIdx       | uint32 |         |
| 16     | ResolutionIdx          | uint32 |         |
| 17     | BaseMipLevel           | uint32 |         |
| 18     | OglOverrides           | string |         |
| 19     | D3dOverrides           | string |         |
| 20     | FixLag                 | uint32 |         |
| 21     | Multisample            | uint32 |         |
| 22     | Atlasdisable           | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/VideoHardware).
