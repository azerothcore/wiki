# WorldMapContinent.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldMapContinent.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field             | Type   | Comment              |
| :----: | :---------------- | :----- | :------------------- |
| 0      | ID                | uint32 |                      |
| 1      | MapID             | uint32 | ID in [Map.dbc](map) |
| 2      | LocLeft           | uint32 |                      |
| 3      | LocRight          | uint32 |                      |
| 4      | LocTop            | uint32 |                      |
| 5      | LocBottom         | uint32 |                      |
| 6      | ContinentOffset_X | float  |                      |
| 7      | ContinentOffset_Y | float  |                      |
| 8      | scale             | float  |                      |
| 9      | TaxiMinX          | float  |                      |
| 10     | TaxiMinY          | float  |                      |
| 11     | TaxiMaxX          | float  |                      |
| 12     | TaxiMaxY          | float  |                      |
| 13     | WorldMapID        | uint32 |                      |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldMapContinent).
