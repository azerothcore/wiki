# AreaGroup.dbc

[`Back-to:DBC`](dbc-index)

**The \`AreaGroup.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [areagroup_dbc](areagroup_dbc) table of the world database.

**Structure**

| Column | Field      | Type   | areagroup\_dbc column                  | Comment                          |
| :----: | :--------- | :----- | :------------------------------------- | :------------------------------- |
| 0      | ID         | uint32 | [ID](areagroup_dbc#id)                 |                                  |
| 1      | AreaID_0   | uint32 | [AreaID_1](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 2      | AreaID_1   | uint32 | [AreaID_2](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 3      | AreaID_2   | uint32 | [AreaID_3](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 4      | AreaID_3   | uint32 | [AreaID_4](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 5      | AreaID_4   | uint32 | [AreaID_5](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 6      | AreaID_5   | uint32 | [AreaID_6](areagroup_dbc#areaid)       | ID in [AreaTable.dbc](areatable) |
| 7      | NextAreaID | uint32 | [NextAreaID](areagroup_dbc#nextareaid) |                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AreaGroup).
