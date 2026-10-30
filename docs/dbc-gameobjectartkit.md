# GameObjectArtKit.dbc

[`Back-to:DBC`](dbc-index)

**The \`GameObjectArtKit.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [gameobjectartkit_dbc](gameobjectartkit_dbc) table of the world database.

**Structure**

| Column | Field              | Type   | gameobjectartkit\_dbc column                       | Comment |
| :----: | :----------------- | :----- | :------------------------------------------------- | :------ |
| 0      | ID                 | uint32 | [ID](gameobjectartkit_dbc#id)                      |         |
| 1      | TextureVariation_0 | string | [Texture_1](gameobjectartkit_dbc#texture)          |         |
| 2      | TextureVariation_1 | string | [Texture_2](gameobjectartkit_dbc#texture)          |         |
| 3      | TextureVariation_2 | string | [Texture_3](gameobjectartkit_dbc#texture)          |         |
| 4      | AttachModel_0      | string | [Attach_Model_1](gameobjectartkit_dbc#attachmodel) |         |
| 5      | AttachModel_1      | string | [Attach_Model_2](gameobjectartkit_dbc#attachmodel) |         |
| 6      | AttachModel_2      | string | [Attach_Model_3](gameobjectartkit_dbc#attachmodel) |         |
| 7      | AttachModel_3      | string | [Attach_Model_4](gameobjectartkit_dbc#attachmodel) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GameObjectArtKit).
