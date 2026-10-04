# SpellDuration.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellDuration.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellduration_dbc](spellduration_dbc) table of the world database.

**Structure**

| Column | Field            | Type   | spellduration\_dbc column                              | Comment |
| :----: | :--------------- | :----- | :----------------------------------------------------- | :------ |
| 0      | ID               | uint32 | [ID](spellduration_dbc#id)                             |         |
| 1      | Duration         | int32  | [Duration](spellduration_dbc#duration)                 |         |
| 2      | DurationPerLevel | int32  | [DurationPerLevel](spellduration_dbc#durationperlevel) |         |
| 3      | MaxDuration      | int32  | [MaxDuration](spellduration_dbc#maxduration)           |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellDuration).
