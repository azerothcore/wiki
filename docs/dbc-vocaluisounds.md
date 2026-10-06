# VocalUISounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`VocalUISounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field       | Type   | Comment                                                                                          |
| :----: | :---------- | :----- | :----------------------------------------------------------------------------------------------- |
| 0      | ID          | uint32 |                                                                                                  |
| 1      | VocalUIEnum | uint32 |                                                                                                  |
| 2      | RaceID      | uint32 | ID in [ChrRaces.dbc](chrraces)                                                                   |
| 3      | SoundID_0   | int32  | ID in [SoundEntries.dbc](dbc-soundentries) (42 of the 500 values used here are not in that file) |
| 4      | SoundID_1   | int32  | ID in [SoundEntries.dbc](dbc-soundentries) (40 of the 502 values used here are not in that file) |
| 5      | SoundID_2   | int32  |                                                                                                  |
| 6      | SoundID_3   | int32  |                                                                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/VocalUISounds).
