# NameGen.dbc

[`Back-to:DBC`](dbc-index)

**The \`NameGen.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field  | Type   | Comment                        |
| :----: | :----- | :----- | :----------------------------- |
| 0      | ID     | uint32 |                                |
| 1      | Name   | string |                                |
| 2      | RaceID | uint32 | ID in [ChrRaces.dbc](chrraces) |
| 3      | Sex    | uint32 |                                |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/NameGen).
