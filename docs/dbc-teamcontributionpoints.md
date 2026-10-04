# TeamContributionPoints.dbc

[`Back-to:DBC`](dbc-index)

**The \`TeamContributionPoints.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [teamcontributionpoints_dbc](teamcontributionpoints_dbc) table of the world database.

**Structure**

| Column | Field | Type   | teamcontributionpoints\_dbc column      | Comment |
| :----: | :---- | :----- | :-------------------------------------- | :------ |
| 0      | ID    | uint32 | [ID](teamcontributionpoints_dbc#id)     |         |
| 1      | Data  | float  | [Data](teamcontributionpoints_dbc#data) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TeamContributionPoints).
