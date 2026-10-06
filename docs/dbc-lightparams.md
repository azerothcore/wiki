# LightParams.dbc

[`Back-to:DBC`](dbc-index)

**The \`LightParams.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field             | Type   | Comment                                  |
| :----: | :---------------- | :----- | :--------------------------------------- |
| 0      | ID                | uint32 |                                          |
| 1      | HighlightSky      | uint32 |                                          |
| 2      | LightSkyboxID     | uint32 | ID in [LightSkybox.dbc](dbc-lightskybox) |
| 3      | Glow              | float  |                                          |
| 4      | WaterShallowAlpha | float  |                                          |
| 5      | WaterDeepAlpha    | float  |                                          |
| 6      | OceanShallowAlpha | float  |                                          |
| 7      | OceanDeepAlpha    | float  |                                          |
| 8      | Flags             | float  |                                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LightParams).
