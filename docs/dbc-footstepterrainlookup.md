# FootstepTerrainLookup.dbc

[`Back-to:DBC`](dbc-index)

**The \`FootstepTerrainLookup.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment                                                                                                  |
| :----: | :----------------- | :----- | :------------------------------------------------------------------------------------------------------- |
| 0      | ID                 | uint32 |                                                                                                          |
| 1      | CreatureFootstepID | uint32 | ID in [CreatureSoundData.dbc](dbc-creaturesounddata) (1 of the 22 values used here are not in that file) |
| 2      | TerrainSoundID     | uint32 | ID in [TerrainTypeSounds.dbc](dbc-terraintypesounds)                                                     |
| 3      | SoundID            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                               |
| 4      | SoundIDSplash      | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                               |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/FootstepTerrainLookup).
