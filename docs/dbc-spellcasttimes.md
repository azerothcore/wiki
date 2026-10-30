# SpellCastTimes.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellCastTimes.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellcasttimes_dbc](spellcasttimes_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | spellcasttimes\_dbc column              | Comment |
| :----: | :------- | :----- | :-------------------------------------- | :------ |
| 0      | ID       | uint32 | [ID](spellcasttimes_dbc#id)             |         |
| 1      | Base     | int32  | [Base](spellcasttimes_dbc#base)         |         |
| 2      | PerLevel | int32  | [PerLevel](spellcasttimes_dbc#perlevel) |         |
| 3      | Minimum  | int32  | [Minimum](spellcasttimes_dbc#minimum)   |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellCastTimes).
