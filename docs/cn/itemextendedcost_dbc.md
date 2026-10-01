# itemextendedcost_dbc

[<-返回至:World](database-world)

**\`itemextendedcost_dbc\` 表**

**表结构**

| Field                                       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                   | INT  | UNSIGNED   | PRI | NO   | 0       |
| [HonorPoints](#honorpoints)                 | INT  | UNSIGNED   |     | NO   | 0       |
| [ArenaPoints](#arenapoints)                 | INT  | UNSIGNED   |     | NO   | 0       |
| [ArenaBracket](#arenabracket)               | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_1](#itemid1)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_2](#itemid2)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_3](#itemid3)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_4](#itemid4)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_5](#itemid5)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_1](#itemcount1)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_2](#itemcount2)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_3](#itemcount3)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_4](#itemcount4)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_5](#itemcount5)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [RequiredArenaRating](#requiredarenarating) | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemPurchaseGroup](#itempurchasegroup)     | INT  | UNSIGNED   |     | NO   | 0       |

**字段说明**

### ID

在 [npc_vendor](npc_vendor#extendedcost) 中使用的 ID

### HonorPoints

所需荣誉点数的数额。

### ArenaPoints

所需竞技场点数的数额。

### ArenaBracket

| Value | Format |
| :-----: | :------: |
| 0     | 2 v 2  |
| 1     | 3 v 3  |
| 2     | 5 v 5  |

### ItemID_1

购买 [ItemID_1](#itemid1) 所需的物品 [Entry](item_template#entry)。

### ItemID_2

购买 [ItemID_2](#itemid2) 所需的物品 [Entry](item_template#entry)。

### ItemID_3

购买 [ItemID_3](#itemid3) 所需的物品 [Entry](item_template#entry)。

### ItemID_4

购买 [ItemID_4](#itemid4) 所需的物品 [Entry](item_template#entry)。

### ItemID_5

购买 [ItemID_5](#itemid5) 所需的物品 [Entry](item_template#entry)。

### ItemCount_1

[ItemID_1](#itemid1) 所需的数量。

### ItemCount_2

[ItemID_2](#itemid2) 所需的数量。

### ItemCount_3

[ItemID_3](#itemid3) 所需的数量。

### ItemCount_4

[ItemID_4](#itemid4) 所需的数量。

### ItemCount_5

[ItemID_5](#itemid5) 所需的数量。

### RequiredArenaRating

所需的个人竞技场等级数额。

### ItemPurchaseGroup 

尚未使用
