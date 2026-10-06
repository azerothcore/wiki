# GameObjectDisplayInfo.dbc

[`Back-to:DBC`](dbc-index)

**The \`GameObjectDisplayInfo.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [gameobjectdisplayinfo_dbc](gameobjectdisplayinfo_dbc) table of the world database.

**Structure**

| Column | Field                 | Type   | gameobjectdisplayinfo\_dbc column                                        | Comment                                                                                        |
| :----: | :-------------------- | :----- | :----------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| 0      | ID                    | uint32 | [ID](gameobjectdisplayinfo_dbc#id)                                       |                                                                                                |
| 1      | ModelName             | string | [ModelName](gameobjectdisplayinfo_dbc#modelname)                         |                                                                                                |
| 2      | Sound_0               | uint32 | [Sound_1](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 58 values used here are not in that file) |
| 3      | Sound_1               | uint32 | [Sound_2](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 4      | Sound_2               | uint32 | [Sound_3](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 56 values used here are not in that file) |
| 5      | Sound_3               | uint32 | [Sound_4](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 6      | Sound_4               | uint32 | [Sound_5](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 7      | Sound_5               | uint32 | [Sound_6](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 8      | Sound_6               | uint32 | [Sound_7](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 78 values used here are not in that file) |
| 9      | Sound_7               | uint32 | [Sound_8](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 10     | Sound_8               | uint32 | [Sound_9](gameobjectdisplayinfo_dbc#sound)                               | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 11     | Sound_9               | uint32 | [Sound_10](gameobjectdisplayinfo_dbc#sound)                              | ID in [SoundEntries.dbc](dbc-soundentries)                                                     |
| 12     | GeoBoxMin_X           | float  | [GeoBoxMinX](gameobjectdisplayinfo_dbc#geoboxminx)                       |                                                                                                |
| 13     | GeoBoxMin_Y           | float  | [GeoBoxMinY](gameobjectdisplayinfo_dbc#geoboxminy)                       |                                                                                                |
| 14     | GeoBoxMin_Z           | float  | [GeoBoxMinZ](gameobjectdisplayinfo_dbc#geoboxminz)                       |                                                                                                |
| 15     | GeoBoxMax_X           | float  | [GeoBoxMaxX](gameobjectdisplayinfo_dbc#geoboxmaxx)                       |                                                                                                |
| 16     | GeoBoxMax_Y           | float  | [GeoBoxMaxY](gameobjectdisplayinfo_dbc#geoboxmaxy)                       |                                                                                                |
| 17     | GeoBoxMax_Z           | float  | [GeoBoxMaxZ](gameobjectdisplayinfo_dbc#geoboxmaxz)                       |                                                                                                |
| 18     | ObjectEffectPackageID | uint32 | [ObjectEffectPackageID](gameobjectdisplayinfo_dbc#objecteffectpackageid) | ID in [ObjectEffectPackage.dbc](dbc-objecteffectpackage)                                       |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GameObjectDisplayInfo).
