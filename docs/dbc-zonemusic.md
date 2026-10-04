# ZoneMusic.dbc

[`Back-to:DBC`](dbc-index)

**The \`ZoneMusic.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                   | Type   | Comment |
| :----: | :---------------------- | :----- | :------ |
| 0      | ID                      | uint32 |         |
| 1      | Name                    | uint32 |         |
| 2      | SilenceIntervalMinDay   | uint32 |         |
| 3      | SilenceIntervalMinNight | uint32 |         |
| 4      | SilenceIntervalMaxDay   | uint32 |         |
| 5      | SilenceIntervalMaxNight | uint32 |         |
| 6      | MusicDay                | uint32 |         |
| 7      | MusicNight              | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ZoneMusic).
