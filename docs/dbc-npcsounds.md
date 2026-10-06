# NPCSounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`NPCSounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field     | Type   | Comment                                                                                         |
| :----: | :-------- | :----- | :---------------------------------------------------------------------------------------------- |
| 0      | ID        | uint32 |                                                                                                 |
| 1      | SoundID_0 | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 300 values used here are not in that file) |
| 2      | SoundID_1 | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 169 values used here are not in that file) |
| 3      | SoundID_2 | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 159 values used here are not in that file) |
| 4      | SoundID_3 | uint32 |                                                                                                 |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/NPCSounds).
