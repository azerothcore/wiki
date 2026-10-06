# Light.dbc

[`Back-to:DBC`](dbc-index)

**The \`Light.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [light_dbc](light_dbc) table of the world database.

**Structure**

| Column | Field            | Type   | light\_dbc column                          | Comment                                  |
| :----: | :--------------- | :----- | :----------------------------------------- | :--------------------------------------- |
| 0      | ID               | uint32 | [ID](light_dbc#id)                         |                                          |
| 1      | ContinentID      | uint32 | [ContinentID](light_dbc#continentid)       | ID in [Map.dbc](map)                     |
| 2      | GameCoords_X     | float  | [X](light_dbc#x)                           |                                          |
| 3      | GameCoords_Y     | float  | [Y](light_dbc#y)                           |                                          |
| 4      | GameCoords_Z     | float  | [Z](light_dbc#z)                           |                                          |
| 5      | GameFalloffStart | float  | [FalloffStart](light_dbc#falloffstart)     |                                          |
| 6      | GameFalloffEnd   | float  | [FalloffEnd](light_dbc#falloffend)         |                                          |
| 7      | LightParamsID_0  | uint32 | [LightParamsID_1](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 8      | LightParamsID_1  | uint32 | [LightParamsID_2](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 9      | LightParamsID_2  | uint32 | [LightParamsID_3](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 10     | LightParamsID_3  | uint32 | [LightParamsID_4](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 11     | LightParamsID_4  | uint32 | [LightParamsID_5](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 12     | LightParamsID_5  | uint32 | [LightParamsID_6](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |
| 13     | LightParamsID_6  | uint32 | [LightParamsID_7](light_dbc#lightparamsid) |                                          |
| 14     | LightParamsID_7  | uint32 | [LightParamsID_8](light_dbc#lightparamsid) | ID in [LightParams.dbc](dbc-lightparams) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Light).
