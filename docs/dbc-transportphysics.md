# TransportPhysics.dbc

[`Back-to:DBC`](dbc-index)

**The \`TransportPhysics.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment |
| :----: | :--------------- | :----- | :------ |
| 0      | ID               | uint32 |         |
| 1      | WaveAmp          | float  |         |
| 2      | WaveTimeScale    | float  |         |
| 3      | RollAmp          | float  |         |
| 4      | RollTimeScale    | float  |         |
| 5      | PitchAmp         | float  |         |
| 6      | PitchTimeScale   | float  |         |
| 7      | MaxBank          | float  |         |
| 8      | MaxBankTurnSpeed | float  |         |
| 9      | SpeedDampThresh  | float  |         |
| 10     | SpeedDamp        | float  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TransportPhysics).
