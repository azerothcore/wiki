# SpellChainEffects.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellChainEffects.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                        | Type   | Comment |
| :----: | :--------------------------- | :----- | :------ |
| 0      | ID                           | uint32 |         |
| 1      | AvgSegLen                    | float  |         |
| 2      | Width                        | float  |         |
| 3      | NoiseScale                   | float  |         |
| 4      | TexCoordScale                | float  |         |
| 5      | SegDuration                  | uint32 |         |
| 6      | SegDelay                     | uint32 |         |
| 7      | Texture                      | string |         |
| 8      | Flags                        | uint32 |         |
| 9      | JointCount                   | uint32 |         |
| 10     | JointOffsetRadius            | float  |         |
| 11     | JointsPerMinorJoint          | uint32 |         |
| 12     | MinorJointsPerMajorJoint     | uint32 |         |
| 13     | MinorJointScale              | float  |         |
| 14     | MajorJointScale              | float  |         |
| 15     | JointMoveSpeed               | float  |         |
| 16     | JointSmoothness              | float  |         |
| 17     | MinDurationBetweenJointJumps | float  |         |
| 18     | MaxDurationBetweenJointJumps | float  |         |
| 19     | WaveHeight                   | float  |         |
| 20     | WaveFreq                     | float  |         |
| 21     | WaveSpeed                    | float  |         |
| 22     | MinWaveAngle                 | float  |         |
| 23     | MaxWaveAngle                 | float  |         |
| 24     | MinWaveSpin                  | float  |         |
| 25     | MaxWaveSpin                  | float  |         |
| 26     | ArcHeight                    | float  |         |
| 27     | MinArcAngle                  | float  |         |
| 28     | MaxArcAngle                  | float  |         |
| 29     | MinArcSpin                   | float  |         |
| 30     | MaxArcSpin                   | float  |         |
| 31     | DelayBetweenEffects          | float  |         |
| 32     | MinFlickerOnDuration         | float  |         |
| 33     | MaxFlickerOnDuration         | float  |         |
| 34     | MinFlickerOffDuration        | float  |         |
| 35     | MaxFlickerOffDuration        | float  |         |
| 36     | PulseSpeed                   | float  |         |
| 37     | PulseOnLength                | float  |         |
| 38     | PulseFadeLength              | float  |         |
| 39     | Alpha                        | uint8  |         |
| 40     | Red                          | int8   |         |
| 41     | Green                        | int8   |         |
| 42     | Blue                         | int8   |         |
| 43     | BlendMode                    | uint8  |         |
| 44     | Combo                        | string |         |
| 45     | RenderLayer                  | uint32 |         |
| 46     | TextureLength                | float  |         |
| 47     | WavePhase                    | float  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellChainEffects).
