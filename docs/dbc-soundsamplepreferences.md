# SoundSamplePreferences.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundSamplePreferences.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                | Type    | Comment |
| :----: | :------------------- | :------ | :------ |
| 0      | ID                   | uint32  |         |
| 1      | Direct               | uint32  |         |
| 2      | DirectHF             | unknown |         |
| 3      | Room                 | uint32  |         |
| 4      | RoomHF               | unknown |         |
| 5      | Obstruction          | unknown |         |
| 6      | OcclusionLFRatio     | float   |         |
| 7      | Unknown_0            | unknown |         |
| 8      | OcclusionLFRatio     | float   |         |
| 9      | OcclusionRoomRatio   | float   |         |
| 10     | Unknown_1            | unknown |         |
| 11     | ExclusionLFRatio     | float   |         |
| 12     | Unknown_2            | unknown |         |
| 13     | OcclusionDirectRatio | float   |         |
| 14     | OutsideVolumeHF      | float   |         |
| 15     | AirAbsorptionFactor  | float   |         |
| 16     | Unknown_3            | unknown |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundSamplePreferences).
