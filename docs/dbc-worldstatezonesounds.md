# WorldStateZoneSounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldStateZoneSounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                      | Type   | Comment                                                            |
| :----: | :------------------------- | :----- | :----------------------------------------------------------------- |
| 0      | WorldStateID               | uint32 |                                                                    |
| 1      | WorldStateValue            | uint32 |                                                                    |
| 2      | AreaID                     | uint32 | ID in [AreaTable.dbc](areatable)                                   |
| 3      | WMOAreaID                  | uint32 | ID in [WMOAreaTable.dbc](dbc-wmoareatable)                         |
| 4      | ZoneIntroMusicID           | uint32 | ID in [ZoneIntroMusicTable.dbc](dbc-zoneintromusictable)           |
| 5      | ZoneMusicID                | uint32 | ID in [ZoneMusic.dbc](dbc-zonemusic)                               |
| 6      | SoundAmbienceID            | uint32 |                                                                    |
| 7      | SoundProviderPreferencesID | uint32 | ID in [SoundProviderPreferences.dbc](dbc-soundproviderpreferences) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldStateZoneSounds).
