# ItemDisplayInfo.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemDisplayInfo.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemdisplayinfo_dbc](itemdisplayinfo_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | itemdisplayinfo\_dbc column                              | Comment                                                  |
| :----: | :------------------ | :----- | :------------------------------------------------------- | :------------------------------------------------------- |
| 0      | ID                  | uint32 | [ID](itemdisplayinfo_dbc#id)                             |                                                          |
| 1      | ModelName_0         | string | [ModelName_1](itemdisplayinfo_dbc#modelname)             |                                                          |
| 2      | ModelName_1         | string | [ModelName_2](itemdisplayinfo_dbc#modelname)             |                                                          |
| 3      | ModelTexture_0      | string | [ModelTexture_1](itemdisplayinfo_dbc#modeltexture)       |                                                          |
| 4      | ModelTexture_1      | string | [ModelTexture_2](itemdisplayinfo_dbc#modeltexture)       |                                                          |
| 5      | InventoryIcon_0     | string | [InventoryIcon_1](itemdisplayinfo_dbc#inventoryicon)     |                                                          |
| 6      | InventoryIcon_1     | string | [InventoryIcon_2](itemdisplayinfo_dbc#inventoryicon)     |                                                          |
| 7      | GeosetGroup_0       | uint32 | [GeosetGroup_1](itemdisplayinfo_dbc#geosetgroup)         |                                                          |
| 8      | GeosetGroup_1       | uint32 | [GeosetGroup_2](itemdisplayinfo_dbc#geosetgroup)         |                                                          |
| 9      | GeosetGroup_2       | uint32 | [GeosetGroup_3](itemdisplayinfo_dbc#geosetgroup)         |                                                          |
| 10     | Flags               | uint32 | [Flags](itemdisplayinfo_dbc#flags)                       |                                                          |
| 11     | SpellVisualID       | uint32 | [SpellVisualID](itemdisplayinfo_dbc#spellvisualid)       | ID in [SpellVisual.dbc](dbc-spellvisual)                 |
| 12     | GroupSoundIndex     | uint32 | [GroupSoundIndex](itemdisplayinfo_dbc#groupsoundindex)   | ID in [ItemGroupSounds.dbc](dbc-itemgroupsounds)         |
| 13     | HelmetGeosetVisID_0 | uint32 | [HelmetGeosetVis_1](itemdisplayinfo_dbc#helmetgeosetvis) | ID in [HelmetGeosetVisData.dbc](dbc-helmetgeosetvisdata) |
| 14     | HelmetGeosetVisID_1 | uint32 | [HelmetGeosetVis_2](itemdisplayinfo_dbc#helmetgeosetvis) | ID in [HelmetGeosetVisData.dbc](dbc-helmetgeosetvisdata) |
| 15     | Texture_0           | string | [Texture_1](itemdisplayinfo_dbc#texture)                 |                                                          |
| 16     | Texture_1           | string | [Texture_2](itemdisplayinfo_dbc#texture)                 |                                                          |
| 17     | Texture_2           | string | [Texture_3](itemdisplayinfo_dbc#texture)                 |                                                          |
| 18     | Texture_3           | string | [Texture_4](itemdisplayinfo_dbc#texture)                 |                                                          |
| 19     | Texture_4           | string | [Texture_5](itemdisplayinfo_dbc#texture)                 |                                                          |
| 20     | Texture_5           | string | [Texture_6](itemdisplayinfo_dbc#texture)                 |                                                          |
| 21     | Texture_6           | string | [Texture_7](itemdisplayinfo_dbc#texture)                 |                                                          |
| 22     | Texture_7           | string | [Texture_8](itemdisplayinfo_dbc#texture)                 |                                                          |
| 23     | ItemVisual          | int32  | [ItemVisual](itemdisplayinfo_dbc#itemvisual)             | ID in [ItemVisuals.dbc](dbc-itemvisuals)                 |
| 24     | ParticleColorID     | uint32 | [ParticleColorID](itemdisplayinfo_dbc#particlecolorid)   |                                                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemDisplayInfo).
