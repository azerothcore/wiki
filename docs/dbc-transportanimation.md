# TransportAnimation.dbc

[`Back-to:DBC`](dbc-index)

**The \`TransportAnimation.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [transportanimation_dbc](transportanimation_dbc) table of the world database.

**Structure**

| Column | Field       | Type   | transportanimation\_dbc column                    | Comment                                      |
| :----: | :---------- | :----- | :------------------------------------------------ | :------------------------------------------- |
| 0      | ID          | uint32 | [ID](transportanimation_dbc#id)                   |                                              |
| 1      | TransportID | uint32 | [TransportID](transportanimation_dbc#transportid) |                                              |
| 2      | TimeIndex   | uint32 | [TimeIndex](transportanimation_dbc#timeindex)     |                                              |
| 3      | Pos_X       | float  | [PosX](transportanimation_dbc#posx)               |                                              |
| 4      | Pos_Y       | float  | [PosY](transportanimation_dbc#posy)               |                                              |
| 5      | Pos_Z       | float  | [PosZ](transportanimation_dbc#posz)               |                                              |
| 6      | SequenceID  | uint32 | [SequenceID](transportanimation_dbc#sequenceid)   | ID in [AnimationData.dbc](dbc-animationdata) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TransportAnimation).
