# WorldMapArea.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldMapArea.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [worldmaparea_dbc](worldmaparea_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | worldmaparea\_dbc column                                    | Comment                                |
| :----: | :------------------ | :----- | :---------------------------------------------------------- | :------------------------------------- |
| 0      | ID                  | uint32 | [ID](worldmaparea_dbc#id)                                   |                                        |
| 1      | MapID               | uint32 | [MapID](worldmaparea_dbc#mapid)                             | ID in [Map.dbc](map)                   |
| 2      | AreaID              | uint32 | [AreaID](worldmaparea_dbc#areaid)                           | ID in [AreaTable.dbc](areatable)       |
| 3      | AreaName            | string | [AreaName](worldmaparea_dbc#areaname)                       |                                        |
| 4      | LocLeft             | float  | [LocLeft](worldmaparea_dbc#locleft)                         |                                        |
| 5      | LocRight            | float  | [LocRight](worldmaparea_dbc#locright)                       |                                        |
| 6      | LocTop              | float  | [LocTop](worldmaparea_dbc#loctop)                           |                                        |
| 7      | LocBottom           | float  | [LocBottom](worldmaparea_dbc#locbottom)                     |                                        |
| 8      | DisplayMapID        | int32  | [DisplayMapID](worldmaparea_dbc#displaymapid)               | ID in [Map.dbc](map)                   |
| 9      | DefaultDungeonFloor | int32  | [DefaultDungeonFloor](worldmaparea_dbc#defaultdungeonfloor) | ID in [DungeonMap.dbc](dbc-dungeonmap) |
| 10     | ParentWorldMapID    | uint32 | [ParentWorldMapID](worldmaparea_dbc#parentworldmapid)       |                                        |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldMapArea).
