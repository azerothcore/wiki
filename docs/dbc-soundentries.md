# SoundEntries.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundEntries.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [soundentries_dbc](soundentries_dbc) table of the world database.

**Structure**

| Column | Field                  | Type   | soundentries\_dbc column                                          | Comment                                                    |
| :----: | :--------------------- | :----- | :---------------------------------------------------------------- | :--------------------------------------------------------- |
| 0      | ID                     | uint32 | [ID](soundentries_dbc#id)                                         |                                                            |
| 1      | SoundType              | uint32 | [SoundType](soundentries_dbc#soundtype)                           |                                                            |
| 2      | Name                   | string | [Name](soundentries_dbc#name)                                     |                                                            |
| 3      | File_0                 | string | [File_1](soundentries_dbc#file)                                   |                                                            |
| 4      | File_1                 | string | [File_2](soundentries_dbc#file)                                   |                                                            |
| 5      | File_2                 | string | [File_3](soundentries_dbc#file)                                   |                                                            |
| 6      | File_3                 | string | [File_4](soundentries_dbc#file)                                   |                                                            |
| 7      | File_4                 | string | [File_5](soundentries_dbc#file)                                   |                                                            |
| 8      | File_5                 | string | [File_6](soundentries_dbc#file)                                   |                                                            |
| 9      | File_6                 | string | [File_7](soundentries_dbc#file)                                   |                                                            |
| 10     | File_7                 | string | [File_8](soundentries_dbc#file)                                   |                                                            |
| 11     | File_8                 | string | [File_9](soundentries_dbc#file)                                   |                                                            |
| 12     | File_9                 | string | [File_10](soundentries_dbc#file)                                  |                                                            |
| 13     | Freq_0                 | uint32 | [Freq_1](soundentries_dbc#freq)                                   |                                                            |
| 14     | Freq_1                 | uint32 | [Freq_2](soundentries_dbc#freq)                                   |                                                            |
| 15     | Freq_2                 | uint32 | [Freq_3](soundentries_dbc#freq)                                   |                                                            |
| 16     | Freq_3                 | uint32 | [Freq_4](soundentries_dbc#freq)                                   |                                                            |
| 17     | Freq_4                 | uint32 | [Freq_5](soundentries_dbc#freq)                                   |                                                            |
| 18     | Freq_5                 | uint32 | [Freq_6](soundentries_dbc#freq)                                   |                                                            |
| 19     | Freq_6                 | uint32 | [Freq_7](soundentries_dbc#freq)                                   |                                                            |
| 20     | Freq_7                 | uint32 | [Freq_8](soundentries_dbc#freq)                                   |                                                            |
| 21     | Freq_8                 | uint32 | [Freq_9](soundentries_dbc#freq)                                   |                                                            |
| 22     | Freq_9                 | uint32 | [Freq_10](soundentries_dbc#freq)                                  |                                                            |
| 23     | DirectoryBase          | string | [DirectoryBase](soundentries_dbc#directorybase)                   |                                                            |
| 24     | VolumeFloat            | float  | [Volumefloat](soundentries_dbc#volumefloat)                       |                                                            |
| 25     | Flags                  | uint32 | [Flags](soundentries_dbc#flags)                                   |                                                            |
| 26     | MinDistance            | float  | [MinDistance](soundentries_dbc#mindistance)                       |                                                            |
| 27     | DistanceCutoff         | float  | [DistanceCutoff](soundentries_dbc#distancecutoff)                 |                                                            |
| 28     | EAXDef                 | uint32 | [EAXDef](soundentries_dbc#eaxdef)                                 |                                                            |
| 29     | SoundEntriesAdvancedID | uint32 | [SoundEntriesAdvancedID](soundentries_dbc#soundentriesadvancedid) | ID in [SoundEntriesAdvanced.dbc](dbc-soundentriesadvanced) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundEntries).
