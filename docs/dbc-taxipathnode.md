# TaxiPathNode.dbc

[`Back-to:DBC`](dbc-index)

**The \`TaxiPathNode.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [taxipathnode_dbc](taxipathnode_dbc) table of the world database.

**Structure**

| Column | Field            | Type   | taxipathnode\_dbc column                              | Comment                                                                                 |
| :----: | :--------------- | :----- | :---------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| 0      | ID               | uint32 | [ID](taxipathnode_dbc#id)                             |                                                                                         |
| 1      | PathID           | uint32 | [PathID](taxipathnode_dbc#pathid)                     | ID in [TaxiPath.dbc](dbc-taxipath) (2 of the 911 values used here are not in that file) |
| 2      | NodeIndex        | uint32 | [NodeIndex](taxipathnode_dbc#nodeindex)               |                                                                                         |
| 3      | ContinentID      | uint32 | [ContinentID](taxipathnode_dbc#continentid)           | ID in [Map.dbc](map)                                                                    |
| 4      | Loc_X            | float  | [LocX](taxipathnode_dbc#locx)                         |                                                                                         |
| 5      | Loc_Y            | float  | [LocY](taxipathnode_dbc#locy)                         |                                                                                         |
| 6      | Loc_Z            | float  | [LocZ](taxipathnode_dbc#locz)                         |                                                                                         |
| 7      | Flags            | uint32 | [Flags](taxipathnode_dbc#flags)                       |                                                                                         |
| 8      | Delay            | uint32 | [Delay](taxipathnode_dbc#delay)                       |                                                                                         |
| 9      | ArrivalEventID   | uint32 | [ArrivalEventID](taxipathnode_dbc#arrivaleventid)     |                                                                                         |
| 10     | DepartureEventID | uint32 | [DepartureEventID](taxipathnode_dbc#departureeventid) |                                                                                         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TaxiPathNode).
