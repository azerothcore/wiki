# GameObjectArtKit.dbc

[`Back-to:DBC`](dbc-index)

**The \`GameObjectArtKit.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [gameobjectartkit_dbc](gameobjectartkit_dbc) table of the world database.

**Structure**

| Column | Field              | Type   | Comment |
| :----: | :----------------- | :----- | :------ |
| 0      | ID                 | uint32 |         |
| 1      | TextureVariation_0 | string |         |
| 2      | TextureVariation_1 | string |         |
| 3      | TextureVariation_2 | string |         |
| 4      | AttachModel_0      | string |         |
| 5      | AttachModel_1      | string |         |
| 6      | AttachModel_2      | string |         |
| 7      | AttachModel_3      | string |         |
| 8      | AttachModel_4      | string |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GameObjectArtKit).
