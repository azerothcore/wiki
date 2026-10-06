# ZoneMusic.dbc

[`Back-to:DBC`](dbc-index)

**The \`ZoneMusic.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                   | Type   | Comment                                                                                         |
| :----: | :---------------------- | :----- | :---------------------------------------------------------------------------------------------- |
| 0      | ID                      | uint32 |                                                                                                 |
| 1      | Name                    | string |                                                                                                 |
| 2      | SilenceIntervalMinDay   | uint32 |                                                                                                 |
| 3      | SilenceIntervalMinNight | uint32 |                                                                                                 |
| 4      | SilenceIntervalMaxDay   | uint32 |                                                                                                 |
| 5      | SilenceIntervalMaxNight | uint32 |                                                                                                 |
| 6      | MusicDay                | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (4 of the 359 values used here are not in that file) |
| 7      | MusicNight              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (4 of the 355 values used here are not in that file) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ZoneMusic).
