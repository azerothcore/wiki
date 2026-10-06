# TransportRotation.dbc

[`Back-to:DBC`](dbc-index)

**The \`TransportRotation.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [transportrotation_dbc](transportrotation_dbc) table of the world database.

**Structure**

| Column | Field         | Type   | transportrotation\_dbc column                        | Comment |
| :----: | :------------ | :----- | :--------------------------------------------------- | :------ |
| 0      | ID            | uint32 | [ID](transportrotation_dbc#id)                       |         |
| 1      | GameObjectsID | uint32 | [GameObjectsID](transportrotation_dbc#gameobjectsid) |         |
| 2      | TimeIndex     | uint32 | [TimeIndex](transportrotation_dbc#timeindex)         |         |
| 3      | Rot_X         | float  | [RotX](transportrotation_dbc#rotx)                   |         |
| 4      | Rot_Y         | float  | [RotY](transportrotation_dbc#roty)                   |         |
| 5      | Rot_Z         | float  | [RotZ](transportrotation_dbc#rotz)                   |         |
| 6      | Rot_W         | float  | [RotW](transportrotation_dbc#rotw)                   |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TransportRotation).
