# SoundEntriesAdvanced.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundEntriesAdvanced.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                  | Type   | Comment                                                                                          |
| :----: | :--------------------- | :----- | :----------------------------------------------------------------------------------------------- |
| 0      | ID                     | uint32 |                                                                                                  |
| 1      | SoundEntryID           | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (4 of the 1628 values used here are not in that file) |
| 2      | InnerRadius2D          | float  |                                                                                                  |
| 3      | Time_A                 | uint32 |                                                                                                  |
| 4      | Time_B                 | uint32 |                                                                                                  |
| 5      | Time_C                 | uint32 |                                                                                                  |
| 6      | Time_D                 | uint32 |                                                                                                  |
| 7      | RandomOffsetRange      | uint32 |                                                                                                  |
| 8      | Usage                  | uint32 |                                                                                                  |
| 9      | TimeIntervalMin        | uint32 |                                                                                                  |
| 10     | TimeIntervalMax        | uint32 |                                                                                                  |
| 11     | VolumeSliderCategory   | uint32 |                                                                                                  |
| 12     | DuckToSFX              | float  |                                                                                                  |
| 13     | DuckToMusic            | float  |                                                                                                  |
| 14     | DuckToAmbience         | float  |                                                                                                  |
| 15     | InnerRadiusOfInfluence | float  |                                                                                                  |
| 16     | OuterRadiusOfInfluence | float  |                                                                                                  |
| 17     | TimeToDuck             | uint32 |                                                                                                  |
| 18     | TimeToUnduck           | uint32 |                                                                                                  |
| 19     | InsideAngle            | float  |                                                                                                  |
| 20     | OutsideAngle           | float  |                                                                                                  |
| 21     | OutsideVolume          | float  |                                                                                                  |
| 22     | OuterRadius2D          | float  |                                                                                                  |
| 23     | Name                   | string |                                                                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundEntriesAdvanced).
