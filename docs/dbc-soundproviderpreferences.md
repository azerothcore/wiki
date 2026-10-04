# SoundProviderPreferences.dbc

[`Back-to:DBC`](dbc-index)

**The \`SoundProviderPreferences.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                    | Type   | Comment |
| :----: | :----------------------- | :----- | :------ |
| 0      | ID                       | uint32 |         |
| 1      | Description              | string |         |
| 2      | Flags                    | uint32 |         |
| 3      | EAXEnvironmentSelection  | uint32 |         |
| 4      | EAXDecayTime             | float  |         |
| 5      | EAX2EnvironmentSize      | float  |         |
| 6      | EAX2EnvironmentDiffusion | float  |         |
| 7      | EAX2Room                 | int32  |         |
| 8      | EAX2RoomHF               | int32  |         |
| 9      | EAX2DecayHFRatio         | float  |         |
| 10     | EAX2Reflections          | int32  |         |
| 11     | EAX2ReflectionsDelay     | float  |         |
| 12     | EAX2Reverb               | int32  |         |
| 13     | EAX2ReverbDelay          | float  |         |
| 14     | EAX2RoomRolloff          | float  |         |
| 15     | EAX2AirAbsorption        | float  |         |
| 16     | EAX3RoomLF               | uint32 |         |
| 17     | EAX3DecayLFRatio         | float  |         |
| 18     | EAX3EchoTime             | float  |         |
| 19     | EAX3EchoDepth            | float  |         |
| 20     | EAX3ModulationTime       | float  |         |
| 21     | EAX3ModulationDepth      | float  |         |
| 22     | EAX3HFReference          | float  |         |
| 23     | EAX3LFReference          | float  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SoundProviderPreferences).
