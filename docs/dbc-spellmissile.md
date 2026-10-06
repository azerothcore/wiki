# SpellMissile.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellMissile.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment |
| :----: | :----------------- | :----- | :------ |
| 0      | ID                 | uint32 |         |
| 1      | Flags              | uint32 |         |
| 2      | DefaultPitchMin    | float  |         |
| 3      | DefaultPitchMax    | float  |         |
| 4      | DefaultSpeedMin    | float  |         |
| 5      | DefaultSpeedMax    | float  |         |
| 6      | RandomizeFacingMin | float  |         |
| 7      | RandomizeFacingMax | float  |         |
| 8      | RandomizePitchMin  | float  |         |
| 9      | RandomizePitchMax  | float  |         |
| 10     | RandomizeSpeedMin  | float  |         |
| 11     | RandomizeSpeedMax  | float  |         |
| 12     | Gravity            | float  |         |
| 13     | MaxDuration        | float  |         |
| 14     | CollisionRadius    | float  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellMissile).
