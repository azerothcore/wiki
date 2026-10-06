# WeaponSwingSounds2.dbc

[`Back-to:DBC`](dbc-index)

**The \`WeaponSwingSounds2.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field     | Type   | Comment                                    |
| :----: | :-------- | :----- | :----------------------------------------- |
| 0      | ID        | uint32 |                                            |
| 1      | SwingType | uint32 | ID in [ItemSubClass.dbc](dbc-itemsubclass) |
| 2      | Critical  | uint32 |                                            |
| 3      | SoundID   | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WeaponSwingSounds2).
