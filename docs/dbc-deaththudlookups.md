# DeathThudLookups.dbc

[`Back-to:DBC`](dbc-index)

**The \`DeathThudLookups.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment                                    |
| :----: | :----------------- | :----- | :----------------------------------------- |
| 0      | ID                 | uint32 |                                            |
| 1      | SizeClass          | uint32 |                                            |
| 2      | TerrainTypeSoundID | uint32 | ID in [TerrainType.dbc](dbc-terraintype)   |
| 3      | SoundEntryID       | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 4      | SoundEntryIDWater  | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DeathThudLookups).
