# PvpDifficulty.dbc

[`Back-to:DBC`](dbc-index)

**The \`PvpDifficulty.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [pvpdifficulty_dbc](pvpdifficulty_dbc) table of the world database.

**Structure**

| Column | Field      | Type   | pvpdifficulty\_dbc column                  | Comment              |
| :----: | :--------- | :----- | :----------------------------------------- | :------------------- |
| 0      | ID         | uint32 | [ID](pvpdifficulty_dbc#id)                 |                      |
| 1      | MapID      | uint32 | [MapID](pvpdifficulty_dbc#mapid)           | ID in [Map.dbc](map) |
| 2      | RangeIndex | uint32 | [RangeIndex](pvpdifficulty_dbc#rangeindex) |                      |
| 3      | MinLevel   | uint32 | [MinLevel](pvpdifficulty_dbc#minlevel)     |                      |
| 4      | MaxLevel   | uint32 | [MaxLevel](pvpdifficulty_dbc#maxlevel)     |                      |
| 5      | Difficulty | uint32 | [Difficulty](pvpdifficulty_dbc#difficulty) |                      |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/PvpDifficulty).
