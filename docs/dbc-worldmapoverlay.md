# WorldMapOverlay.dbc

[`Back-to:DBC`](dbc-index)

**The \`WorldMapOverlay.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [worldmapoverlay_dbc](worldmapoverlay_dbc) table of the world database.

**Structure**

| Column | Field         | Type   | worldmapoverlay\_dbc column                        | Comment                                    |
| :----: | :------------ | :----- | :------------------------------------------------- | :----------------------------------------- |
| 0      | ID            | uint32 | [ID](worldmapoverlay_dbc#id)                       |                                            |
| 1      | MapAreaID     | uint32 | [MapAreaID](worldmapoverlay_dbc#mapareaid)         | ID in [WorldMapArea.dbc](dbc-worldmaparea) |
| 2      | AreaID_0      | uint32 | [AreaID_1](worldmapoverlay_dbc#areaid)             | ID in [AreaTable.dbc](areatable)           |
| 3      | AreaID_1      | uint32 | [AreaID_2](worldmapoverlay_dbc#areaid)             | ID in [AreaTable.dbc](areatable)           |
| 4      | AreaID_2      | uint32 | [AreaID_3](worldmapoverlay_dbc#areaid)             | ID in [AreaTable.dbc](areatable)           |
| 5      | AreaID_3      | uint32 | [AreaID_4](worldmapoverlay_dbc#areaid)             | ID in [AreaTable.dbc](areatable)           |
| 6      | MapPoint_X    | uint32 | [MapPointX](worldmapoverlay_dbc#mappointx)         |                                            |
| 7      | MapPoint_Y    | uint32 | [MapPointY](worldmapoverlay_dbc#mappointy)         |                                            |
| 8      | TextureName   | string | [TextureName](worldmapoverlay_dbc#texturename)     |                                            |
| 9      | TextureWidth  | uint32 | [TextureWidth](worldmapoverlay_dbc#texturewidth)   |                                            |
| 10     | TextureHeight | uint32 | [TextureHeight](worldmapoverlay_dbc#textureheight) |                                            |
| 11     | Offset_X      | uint32 | [OffsetX](worldmapoverlay_dbc#offsetx)             |                                            |
| 12     | Offset_Y      | uint32 | [OffsetY](worldmapoverlay_dbc#offsety)             |                                            |
| 13     | HitRectTop    | uint32 | [HitRectTop](worldmapoverlay_dbc#hitrecttop)       |                                            |
| 14     | HitRectLeft   | uint32 | [HitRectLeft](worldmapoverlay_dbc#hitrectleft)     |                                            |
| 15     | HitRectBottom | uint32 | [HitRectBottom](worldmapoverlay_dbc#hitrectbottom) |                                            |
| 16     | HitRectRight  | uint32 | [HitRectRight](worldmapoverlay_dbc#hitrectright)   |                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WorldMapOverlay).
