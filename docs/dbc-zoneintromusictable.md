# ZoneIntroMusicTable.dbc

[`Back-to:DBC`](dbc-index)

**The \`ZoneIntroMusicTable.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field           | Type   | Comment                                    |
| :----: | :-------------- | :----- | :----------------------------------------- |
| 0      | ID              | uint32 |                                            |
| 1      | Name            | string |                                            |
| 2      | SoundID         | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 3      | Priority        | uint32 |                                            |
| 4      | MinDelayMinutes | uint32 |                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ZoneIntroMusicTable).
