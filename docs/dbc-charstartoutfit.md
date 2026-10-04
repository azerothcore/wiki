# CharStartOutfit.dbc

[`Back-to:DBC`](dbc-index)

**The \`CharStartOutfit.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [charstartoutfit_dbc](charstartoutfit_dbc) table of the world database.

**Structure**

| Column | Field            | Type   | charstartoutfit\_dbc column                           | Comment |
| :----: | :--------------- | :----- | :---------------------------------------------------- | :------ |
| 0      | ID               | uint32 | [ID](charstartoutfit_dbc#id)                          |         |
| 1      | RaceID           | uint8  | [RaceID](charstartoutfit_dbc#raceid)                  |         |
| 2      | ClassID          | uint8  | [ClassID](charstartoutfit_dbc#classid)                |         |
| 3      | SexID            | uint8  | [SexID](charstartoutfit_dbc#sexid)                    |         |
| 4      | OutfitID         | uint8  | [OutfitID](charstartoutfit_dbc#outfitid)              |         |
| 5      | ItemID_0         | int32  | [ItemID_1](charstartoutfit_dbc#itemid)                |         |
| 6      | ItemID_1         | int32  | [ItemID_2](charstartoutfit_dbc#itemid)                |         |
| 7      | ItemID_2         | int32  | [ItemID_3](charstartoutfit_dbc#itemid)                |         |
| 8      | ItemID_3         | int32  | [ItemID_4](charstartoutfit_dbc#itemid)                |         |
| 9      | ItemID_4         | int32  | [ItemID_5](charstartoutfit_dbc#itemid)                |         |
| 10     | ItemID_5         | int32  | [ItemID_6](charstartoutfit_dbc#itemid)                |         |
| 11     | ItemID_6         | int32  | [ItemID_7](charstartoutfit_dbc#itemid)                |         |
| 12     | ItemID_7         | int32  | [ItemID_8](charstartoutfit_dbc#itemid)                |         |
| 13     | ItemID_8         | int32  | [ItemID_9](charstartoutfit_dbc#itemid)                |         |
| 14     | ItemID_9         | int32  | [ItemID_10](charstartoutfit_dbc#itemid)               |         |
| 15     | ItemID_10        | int32  | [ItemID_11](charstartoutfit_dbc#itemid)               |         |
| 16     | ItemID_11        | int32  | [ItemID_12](charstartoutfit_dbc#itemid)               |         |
| 17     | ItemID_12        | int32  | [ItemID_13](charstartoutfit_dbc#itemid)               |         |
| 18     | ItemID_13        | int32  | [ItemID_14](charstartoutfit_dbc#itemid)               |         |
| 19     | ItemID_14        | int32  | [ItemID_15](charstartoutfit_dbc#itemid)               |         |
| 20     | ItemID_15        | int32  | [ItemID_16](charstartoutfit_dbc#itemid)               |         |
| 21     | ItemID_16        | int32  | [ItemID_17](charstartoutfit_dbc#itemid)               |         |
| 22     | ItemID_17        | int32  | [ItemID_18](charstartoutfit_dbc#itemid)               |         |
| 23     | ItemID_18        | int32  | [ItemID_19](charstartoutfit_dbc#itemid)               |         |
| 24     | ItemID_19        | int32  | [ItemID_20](charstartoutfit_dbc#itemid)               |         |
| 25     | ItemID_20        | int32  | [ItemID_21](charstartoutfit_dbc#itemid)               |         |
| 26     | ItemID_21        | int32  | [ItemID_22](charstartoutfit_dbc#itemid)               |         |
| 27     | ItemID_22        | int32  | [ItemID_23](charstartoutfit_dbc#itemid)               |         |
| 28     | ItemID_23        | int32  | [ItemID_24](charstartoutfit_dbc#itemid)               |         |
| 29     | DisplayItemID_0  | int32  | [DisplayItemID_1](charstartoutfit_dbc#displayitemid)  |         |
| 30     | DisplayItemID_1  | int32  | [DisplayItemID_2](charstartoutfit_dbc#displayitemid)  |         |
| 31     | DisplayItemID_2  | int32  | [DisplayItemID_3](charstartoutfit_dbc#displayitemid)  |         |
| 32     | DisplayItemID_3  | int32  | [DisplayItemID_4](charstartoutfit_dbc#displayitemid)  |         |
| 33     | DisplayItemID_4  | int32  | [DisplayItemID_5](charstartoutfit_dbc#displayitemid)  |         |
| 34     | DisplayItemID_5  | int32  | [DisplayItemID_6](charstartoutfit_dbc#displayitemid)  |         |
| 35     | DisplayItemID_6  | int32  | [DisplayItemID_7](charstartoutfit_dbc#displayitemid)  |         |
| 36     | DisplayItemID_7  | int32  | [DisplayItemID_8](charstartoutfit_dbc#displayitemid)  |         |
| 37     | DisplayItemID_8  | int32  | [DisplayItemID_9](charstartoutfit_dbc#displayitemid)  |         |
| 38     | DisplayItemID_9  | int32  | [DisplayItemID_10](charstartoutfit_dbc#displayitemid) |         |
| 39     | DisplayItemID_10 | int32  | [DisplayItemID_11](charstartoutfit_dbc#displayitemid) |         |
| 40     | DisplayItemID_11 | int32  | [DisplayItemID_12](charstartoutfit_dbc#displayitemid) |         |
| 41     | DisplayItemID_12 | int32  | [DisplayItemID_13](charstartoutfit_dbc#displayitemid) |         |
| 42     | DisplayItemID_13 | int32  | [DisplayItemID_14](charstartoutfit_dbc#displayitemid) |         |
| 43     | DisplayItemID_14 | int32  | [DisplayItemID_15](charstartoutfit_dbc#displayitemid) |         |
| 44     | DisplayItemID_15 | int32  | [DisplayItemID_16](charstartoutfit_dbc#displayitemid) |         |
| 45     | DisplayItemID_16 | int32  | [DisplayItemID_17](charstartoutfit_dbc#displayitemid) |         |
| 46     | DisplayItemID_17 | int32  | [DisplayItemID_18](charstartoutfit_dbc#displayitemid) |         |
| 47     | DisplayItemID_18 | int32  | [DisplayItemID_19](charstartoutfit_dbc#displayitemid) |         |
| 48     | DisplayItemID_19 | int32  | [DisplayItemID_20](charstartoutfit_dbc#displayitemid) |         |
| 49     | DisplayItemID_20 | int32  | [DisplayItemID_21](charstartoutfit_dbc#displayitemid) |         |
| 50     | DisplayItemID_21 | int32  | [DisplayItemID_22](charstartoutfit_dbc#displayitemid) |         |
| 51     | DisplayItemID_22 | int32  | [DisplayItemID_23](charstartoutfit_dbc#displayitemid) |         |
| 52     | DisplayItemID_23 | int32  | [DisplayItemID_24](charstartoutfit_dbc#displayitemid) |         |
| 53     | InventoryType_0  | int32  | [InventoryType_1](charstartoutfit_dbc#inventorytype)  |         |
| 54     | InventoryType_1  | int32  | [InventoryType_2](charstartoutfit_dbc#inventorytype)  |         |
| 55     | InventoryType_2  | int32  | [InventoryType_3](charstartoutfit_dbc#inventorytype)  |         |
| 56     | InventoryType_3  | int32  | [InventoryType_4](charstartoutfit_dbc#inventorytype)  |         |
| 57     | InventoryType_4  | int32  | [InventoryType_5](charstartoutfit_dbc#inventorytype)  |         |
| 58     | InventoryType_5  | int32  | [InventoryType_6](charstartoutfit_dbc#inventorytype)  |         |
| 59     | InventoryType_6  | int32  | [InventoryType_7](charstartoutfit_dbc#inventorytype)  |         |
| 60     | InventoryType_7  | int32  | [InventoryType_8](charstartoutfit_dbc#inventorytype)  |         |
| 61     | InventoryType_8  | int32  | [InventoryType_9](charstartoutfit_dbc#inventorytype)  |         |
| 62     | InventoryType_9  | int32  | [InventoryType_10](charstartoutfit_dbc#inventorytype) |         |
| 63     | InventoryType_10 | int32  | [InventoryType_11](charstartoutfit_dbc#inventorytype) |         |
| 64     | InventoryType_11 | int32  | [InventoryType_12](charstartoutfit_dbc#inventorytype) |         |
| 65     | InventoryType_12 | int32  | [InventoryType_13](charstartoutfit_dbc#inventorytype) |         |
| 66     | InventoryType_13 | int32  | [InventoryType_14](charstartoutfit_dbc#inventorytype) |         |
| 67     | InventoryType_14 | int32  | [InventoryType_15](charstartoutfit_dbc#inventorytype) |         |
| 68     | InventoryType_15 | int32  | [InventoryType_16](charstartoutfit_dbc#inventorytype) |         |
| 69     | InventoryType_16 | int32  | [InventoryType_17](charstartoutfit_dbc#inventorytype) |         |
| 70     | InventoryType_17 | int32  | [InventoryType_18](charstartoutfit_dbc#inventorytype) |         |
| 71     | InventoryType_18 | int32  | [InventoryType_19](charstartoutfit_dbc#inventorytype) |         |
| 72     | InventoryType_19 | int32  | [InventoryType_20](charstartoutfit_dbc#inventorytype) |         |
| 73     | InventoryType_20 | int32  | [InventoryType_21](charstartoutfit_dbc#inventorytype) |         |
| 74     | InventoryType_21 | int32  | [InventoryType_22](charstartoutfit_dbc#inventorytype) |         |
| 75     | InventoryType_22 | int32  | [InventoryType_23](charstartoutfit_dbc#inventorytype) |         |
| 76     | InventoryType_23 | int32  | [InventoryType_24](charstartoutfit_dbc#inventorytype) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CharStartOutfit).
