# LFGDungeonExpansion.dbc

[`Back-to:DBC`](dbc-index)

**The \`LFGDungeonExpansion.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field          | Type   | Comment                                  |
| :----: | :------------- | :----- | :--------------------------------------- |
| 0      | ID             | uint32 |                                          |
| 1      | LfgDungeonID   | uint32 | ID in [LfgDungeons.dbc](dbc-lfgdungeons) |
| 2      | Expansion      | uint32 |                                          |
| 3      | RandomID       | uint32 |                                          |
| 4      | HardLevelMin   | uint32 |                                          |
| 5      | HardLevelMax   | uint32 |                                          |
| 6      | TargetLevelMin | uint32 |                                          |
| 7      | TargetLevelMax | uint32 |                                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LFGDungeonExpansion).
