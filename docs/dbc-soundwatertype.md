# SoundWaterType.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundWaterType.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field        | Type   | Comment                                    |
| :----: | :----------- | :----- | :----------------------------------------- |
| 0      | ID           | uint32 |                                            |
| 1      | SoundType    | uint32 |                                            |
| 2      | SoundSubtype | uint32 |                                            |
| 3      | SoundID      | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundWaterType).
