# CinematicSequences.dbc

[`Back-to:DBC`](dbc-index)

**The \`CinematicSequences.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [cinematicsequences_dbc](cinematicsequences_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | cinematicsequences\_dbc column            | Comment                                          |
| :----: | :------- | :----- | :---------------------------------------- | :----------------------------------------------- |
| 0      | ID       | uint32 | [ID](cinematicsequences_dbc#id)           |                                                  |
| 1      | SoundID  | uint32 | [SoundID](cinematicsequences_dbc#soundid) |                                                  |
| 2      | Camera_0 | uint32 | [Camera_1](cinematicsequences_dbc#camera) | ID in [CinematicCamera.dbc](dbc-cinematiccamera) |
| 3      | Camera_1 | uint32 | [Camera_2](cinematicsequences_dbc#camera) |                                                  |
| 4      | Camera_2 | uint32 | [Camera_3](cinematicsequences_dbc#camera) |                                                  |
| 5      | Camera_3 | uint32 | [Camera_4](cinematicsequences_dbc#camera) |                                                  |
| 6      | Camera_4 | uint32 | [Camera_5](cinematicsequences_dbc#camera) |                                                  |
| 7      | Camera_5 | uint32 | [Camera_6](cinematicsequences_dbc#camera) |                                                  |
| 8      | Camera_6 | uint32 | [Camera_7](cinematicsequences_dbc#camera) |                                                  |
| 9      | Camera_7 | uint32 | [Camera_8](cinematicsequences_dbc#camera) |                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CinematicSequences).
