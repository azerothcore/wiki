# DestructibleModelData.dbc

[`Back-to:DBC`](dbc-index)

**The \`DestructibleModelData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [destructiblemodeldata_dbc](destructiblemodeldata_dbc) table of the world database.

**Structure**

| Column | Field                       | Type   | destructiblemodeldata\_dbc column                                                    | Comment                                                      |
| :----: | :-------------------------- | :----- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 0      | ID                          | uint32 | [ID](destructiblemodeldata_dbc#id)                                                   |                                                              |
| 1      | State0ImpactEffectDoodadSet | uint32 | [State0Wmo](destructiblemodeldata_dbc#state0wmo)                                     |                                                              |
| 2      | State0AmbientDoodadSet      | uint32 | [State0DestructionDoodadSet](destructiblemodeldata_dbc#state0destructiondoodadset)   |                                                              |
| 3      | State1Wmo                   | uint32 | [State0ImpactEffectDoodadSet](destructiblemodeldata_dbc#state0impacteffectdoodadset) | ID in [GameObjectDisplayInfo.dbc](dbc-gameobjectdisplayinfo) |
| 4      | State1DestructionDoodadSet  | uint32 | [State0AmbientDoodadSet](destructiblemodeldata_dbc#state0ambientdoodadset)           |                                                              |
| 5      | State1ImpactEffectDoodadSet | uint32 | [State1Wmo](destructiblemodeldata_dbc#state1wmo)                                     |                                                              |
| 6      | State1AmbientDoodadSet      | uint32 | [State1DestructionDoodadSet](destructiblemodeldata_dbc#state1destructiondoodadset)   |                                                              |
| 7      | State2Wmo                   | uint32 | [State1ImpactEffectDoodadSet](destructiblemodeldata_dbc#state1impacteffectdoodadset) | ID in [GameObjectDisplayInfo.dbc](dbc-gameobjectdisplayinfo) |
| 8      | State2DestructionDoodadSet  | uint32 | [State1AmbientDoodadSet](destructiblemodeldata_dbc#state1ambientdoodadset)           |                                                              |
| 9      | State2ImpactEffectDoodadSet | uint32 | [State2Wmo](destructiblemodeldata_dbc#state2wmo)                                     |                                                              |
| 10     | State2AmbientDoodadSet      | uint32 | [State2DestructionDoodadSet](destructiblemodeldata_dbc#state2destructiondoodadset)   |                                                              |
| 11     | State3Wmo                   | uint32 | [State2ImpactEffectDoodadSet](destructiblemodeldata_dbc#state2impacteffectdoodadset) | ID in [GameObjectDisplayInfo.dbc](dbc-gameobjectdisplayinfo) |
| 12     | State3InitDoodadSet         | uint32 | [State2AmbientDoodadSet](destructiblemodeldata_dbc#state2ambientdoodadset)           |                                                              |
| 13     | State3AmbientDoodadSet      | uint32 | [State3Wmo](destructiblemodeldata_dbc#state3wmo)                                     |                                                              |
| 14     | EjectDirection              | uint32 | [State3DestructionDoodadSet](destructiblemodeldata_dbc#state3destructiondoodadset)   |                                                              |
| 15     | RepairGroundFx              | uint32 | [State3ImpactEffectDoodadSet](destructiblemodeldata_dbc#state3impacteffectdoodadset) |                                                              |
| 16     | DoNotHighlight              | uint32 | [State3AmbientDoodadSet](destructiblemodeldata_dbc#state3ambientdoodadset)           |                                                              |
| 17     | HealEffect                  | uint32 | [Field17](destructiblemodeldata_dbc#field)                                           |                                                              |
| 18     | HealEffectSpeed             | uint32 | [Field18](destructiblemodeldata_dbc#field)                                           |                                                              |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DestructibleModelData).
