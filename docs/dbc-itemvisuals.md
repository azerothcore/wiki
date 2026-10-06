# ItemVisuals.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemVisuals.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                                                                                  |
| :----: | :--------------- | :----- | :------------------------------------------------------------------------------------------------------- |
| 0      | ID               | uint32 |                                                                                                          |
| 1      | VisualEffectID_0 | int32  | ID in [ItemVisualEffects.dbc](dbc-itemvisualeffects) (5 of the 47 values used here are not in that file) |
| 2      | VisualEffectID_1 | int32  |                                                                                                          |
| 3      | VisualEffectID_2 | int32  | ID in [ItemVisualEffects.dbc](dbc-itemvisualeffects) (6 of the 54 values used here are not in that file) |
| 4      | VisualEffectID_3 | int32  |                                                                                                          |
| 5      | VisualEffectID_4 | int32  | ID in [ItemVisualEffects.dbc](dbc-itemvisualeffects) (2 of the 55 values used here are not in that file) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemVisuals).
