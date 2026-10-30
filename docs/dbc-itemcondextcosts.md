# ItemCondExtCosts.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemCondExtCosts.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts.

**Structure**

| Column | Field                 | Type   | Comment                                            |
| :----: | :-------------------- | :----- | :------------------------------------------------- |
| 0      | ID                    | uint32 |                                                    |
| 1      | CondExtendedCost      | uint32 |                                                    |
| 2      | ItemExtendedCostEntry | uint32 | ID in [ItemExtendedCost.dbc](dbc-itemextendedcost) |
| 3      | ArenaSeason           | uint32 |                                                    |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemCondExtCosts).
