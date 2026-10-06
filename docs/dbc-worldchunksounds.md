# WorldChunkSounds.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldChunkSounds.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                      | Type   | Comment |
| :----: | :------------------------- | :----- | :------ |
| 0      | WorldMapContinentID        | uint32 |         |
| 1      | ChunkX                     | uint32 |         |
| 2      | ChunkY                     | uint32 |         |
| 3      | SubchunkX                  | uint32 |         |
| 4      | SubchunkY                  | uint32 |         |
| 5      | ZoneIntroMusicID           | uint32 |         |
| 6      | ZoneMusicID                | uint32 |         |
| 7      | SoundAmbienceID            | uint32 |         |
| 8      | SoundProviderPreferencesID | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldChunkSounds).
