# Material.dbc

[`Back-to:DBC`](dbc-index)

**The \`Material.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                    |
| :----: | :--------------- | :----- | :----------------------------------------- |
| 0      | ID               | uint32 |                                            |
| 1      | Flags            | uint32 |                                            |
| 2      | FoleySoundID     | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 3      | SheatheSoundID   | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 4      | UnsheatheSoundID | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Material).
