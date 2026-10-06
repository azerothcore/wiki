# ScreenEffect.dbc

[`Back-to:DBC`](dbc-index)

**The \`ScreenEffect.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field           | Type   | Comment                                      |
| :----: | :-------------- | :----- | :------------------------------------------- |
| 0      | ID              | uint32 |                                              |
| 1      | Name            | string |                                              |
| 2      | Type            | uint32 |                                              |
| 3      | Color           | int32  |                                              |
| 4      | Edge            | uint32 |                                              |
| 5      | BW              | uint32 |                                              |
| 6      | UnkParam        | uint32 |                                              |
| 7      | LightParamsID   | int32  | ID in [LightParams.dbc](dbc-lightparams)     |
| 8      | SoundAmbienceID | uint32 | ID in [SoundAmbience.dbc](dbc-soundambience) |
| 9      | ZoneMusicID     | uint32 | ID in [ZoneMusic.dbc](dbc-zonemusic)         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ScreenEffect).
