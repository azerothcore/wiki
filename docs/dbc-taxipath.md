# TaxiPath.dbc

[`Back-to:DBC`](dbc-index)

**The \`TaxiPath.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [taxipath_dbc](taxipath_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | taxipath\_dbc column                      | Comment                              |
| :----: | :----------- | :----- | :---------------------------------------- | :----------------------------------- |
| 0      | ID           | uint32 | [ID](taxipath_dbc#id)                     |                                      |
| 1      | FromTaxiNode | uint32 | [FromTaxiNode](taxipath_dbc#fromtaxinode) | ID in [TaxiNodes.dbc](dbc-taxinodes) |
| 2      | ToTaxiNode   | uint32 | [ToTaxiNode](taxipath_dbc#totaxinode)     | ID in [TaxiNodes.dbc](dbc-taxinodes) |
| 3      | Cost         | uint32 | [Cost](taxipath_dbc#cost)                 |                                      |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TaxiPath).
