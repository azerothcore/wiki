# Stationery.dbc

[`Back-to:DBC`](dbc-index)

**The \`Stationery.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field   | Type   | Comment                    |
| :----: | :------ | :----- | :------------------------- |
| 0      | ID      | uint32 |                            |
| 1      | ItemID  | uint32 | ID in [Item.dbc](dbc-item) |
| 2      | Texture | string |                            |
| 3      | Flags   | uint32 |                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Stationery).
