# ItemGroupSounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemGroupSounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field        | Type   | Comment                                                                                        |
| :----: | :----------- | :----- | :--------------------------------------------------------------------------------------------- |
| 0      | ID           | uint32 |                                                                                                |
| 1      | SoundEntry_0 | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (2 of the 20 values used here are not in that file) |
| 2      | SoundEntry_1 | uint32 |                                                                                                |
| 3      | SoundEntry_2 | uint32 |                                                                                                |
| 4      | SoundEntry_3 | uint32 |                                                                                                |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemGroupSounds).
