# WorldChunkSounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldChunkSounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                      | Type   | Comment |
| :----: | :------------------------- | :----- | :------ |
| 0      | GeneratedID                | uint32 |         |
| 1      | WorldMapContinentID        | uint32 |         |
| 2      | ChunkX                     | uint32 |         |
| 3      | ChunkY                     | uint32 |         |
| 4      | SubchunkX                  | uint32 |         |
| 5      | SubchunkY                  | uint32 |         |
| 6      | ZoneIntroMusicID           | uint32 |         |
| 7      | ZoneMusicID                | uint32 |         |
| 8      | SoundAmbienceID            | uint32 |         |
| 9      | SoundProviderPreferencesID | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldChunkSounds).
