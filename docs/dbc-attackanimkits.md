# AttackAnimKits.dbc

[`Back-to:DBC`](dbc-index)

**The \`AttackAnimKits.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field           | Type   | Comment                                          |
| :----: | :-------------- | :----- | :----------------------------------------------- |
| 0      | ID              | uint32 |                                                  |
| 1      | AnimationData   | uint32 | ID in [AnimationData.dbc](dbc-animationdata)     |
| 2      | AttackAnimTypes | uint32 | ID in [AttackAnimTypes.dbc](dbc-attackanimtypes) |
| 3      | Flags           | uint32 |                                                  |
| 4      | WhichHand       | uint32 |                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AttackAnimKits).
