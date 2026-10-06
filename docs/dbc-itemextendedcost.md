# ItemExtendedCost.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemExtendedCost.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemextendedcost_dbc](itemextendedcost_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | itemextendedcost\_dbc column                                    | Comment                    |
| :----: | :------------------ | :----- | :-------------------------------------------------------------- | :------------------------- |
| 0      | ID                  | uint32 | [ID](itemextendedcost_dbc#id)                                   |                            |
| 1      | HonorPoints         | uint32 | [HonorPoints](itemextendedcost_dbc#honorpoints)                 |                            |
| 2      | ArenaPoints         | uint32 | [ArenaPoints](itemextendedcost_dbc#arenapoints)                 |                            |
| 3      | ArenaBracket        | uint32 | [ArenaBracket](itemextendedcost_dbc#arenabracket)               |                            |
| 4      | ItemID_0            | uint32 | [ItemID_1](itemextendedcost_dbc#itemid1)                        | ID in [Item.dbc](dbc-item) |
| 5      | ItemID_1            | uint32 | [ItemID_2](itemextendedcost_dbc#itemid2)                        | ID in [Item.dbc](dbc-item) |
| 6      | ItemID_2            | uint32 | [ItemID_3](itemextendedcost_dbc#itemid3)                        | ID in [Item.dbc](dbc-item) |
| 7      | ItemID_3            | uint32 | [ItemID_4](itemextendedcost_dbc#itemid4)                        | ID in [Item.dbc](dbc-item) |
| 8      | ItemID_4            | uint32 | [ItemID_5](itemextendedcost_dbc#itemid5)                        | ID in [Item.dbc](dbc-item) |
| 9      | ItemCount_0         | uint32 | [ItemCount_1](itemextendedcost_dbc#itemcount1)                  |                            |
| 10     | ItemCount_1         | uint32 | [ItemCount_2](itemextendedcost_dbc#itemcount2)                  |                            |
| 11     | ItemCount_2         | uint32 | [ItemCount_3](itemextendedcost_dbc#itemcount3)                  |                            |
| 12     | ItemCount_3         | uint32 | [ItemCount_4](itemextendedcost_dbc#itemcount4)                  |                            |
| 13     | ItemCount_4         | uint32 | [ItemCount_5](itemextendedcost_dbc#itemcount5)                  |                            |
| 14     | RequiredArenaRating | uint32 | [RequiredArenaRating](itemextendedcost_dbc#requiredarenarating) |                            |
| 15     | ItemPurchaseGroup   | uint32 | [ItemPurchaseGroup](itemextendedcost_dbc#itempurchasegroup)     |                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemExtendedCost).
