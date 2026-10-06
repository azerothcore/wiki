# AnimationData.dbc

[`Back-to:DBC`](dbc-index)

**The \`AnimationData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field        | Type   | Comment |
| :----: | :----------- | :----- | :------ |
| 0      | ID           | uint32 |         |
| 1      | Name         | string |         |
| 2      | Weaponflags  | uint32 |         |
| 3      | Bodyflags    | uint32 |         |
| 4      | Flags        | uint32 |         |
| 5      | FallbackID   | uint32 |         |
| 6      | BehaviorID   | uint32 |         |
| 7      | BehaviorTier | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AnimationData).
