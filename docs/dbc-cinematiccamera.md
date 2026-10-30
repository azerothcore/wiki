# CinematicCamera.dbc

[`Back-to:DBC`](dbc-index)

**The \`CinematicCamera.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [cinematiccamera_dbc](cinematiccamera_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | cinematiccamera\_dbc column                  | Comment                                    |
| :----: | :----------- | :----- | :------------------------------------------- | :----------------------------------------- |
| 0      | ID           | uint32 | [ID](cinematiccamera_dbc#id)                 |                                            |
| 1      | Model        | string | [model](cinematiccamera_dbc#model)           |                                            |
| 2      | SoundID      | uint32 | [soundEntry](cinematiccamera_dbc#soundentry) | ID in [SoundEntries.dbc](dbc-soundentries) |
| 3      | Origin_X     | float  | [locationX](cinematiccamera_dbc#locationx)   |                                            |
| 4      | Origin_Y     | float  | [locationY](cinematiccamera_dbc#locationy)   |                                            |
| 5      | Origin_Z     | float  | [locationZ](cinematiccamera_dbc#locationz)   |                                            |
| 6      | OriginFacing | float  | [rotation](cinematiccamera_dbc#rotation)     |                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CinematicCamera).
