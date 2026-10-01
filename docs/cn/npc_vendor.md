# npc\_vendor

[<-返回:World](database-world)

## 基本信息

此表保存所有出售物品或货币的 NPC 的商人数据。一个商人最多只能持有 150 件物品（15 页），这一限制已硬编码在模拟器中，如果你修改它，客户端将会崩溃。

### 价格

每件物品或货币的价格（以金币计）在其对应的物品模板条目中定义为 [item_template.BuyPrice](item_template#buyprice)。
特殊花费（荣誉、徽章等）在此表的 [ExtendedCost](#extendedcost) 列中定义。

### GM 模式

如果你在 GM 模式下打开商人的窗口，你会看到该商人出售的所有物品。如果你关闭 GM 模式，你会像普通玩家一样看到出售的物品（例如：如果你无法使用某件物品且无法交易它，你将不会在列表中看到它）。


## 表结构

| Field             | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [slot][2]         | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [item][3]         | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [maxcount][4]     | TINYINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [incrtime][5]     | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [ExtendedCost][6] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [VerifiedBuild][7] | INT      |            |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #slot
[3]: #item
[4]: #maxcount
[5]: #incrtime
[6]: #extendedcost
[7]: #verifiedbuild


## 字段说明

### entry

生物（creature）的 ID。参见 [creature\_template.entry](creature_template#entry)。

### slot

物品在商人窗口打开时的位置。从 0 到 x，从上到下，从左到右。
*注意：如果你的物品列表都在槽位 0，而你将其中一件编辑为槽位 1 或任意其他数字，该物品将始终排在最后，因为其他所有物品都在槽位 0。*

### item

物品 ID。参见 [item\_template.entry](item_template#entry)。

### maxcount

商人在任何时刻持有的最大物品数量。如果你希望商人无限量地持有该物品，请将其设置为 **0**，否则设置为任意正数。下图中圈出的就是 maxcount 值。

### incrtime

与 [maxcount](#maxcount) 结合使用，此字段指示商人列表每隔多久（以秒为单位）刷新一次，以及限量物品的数量每隔多久补货一次。对于限量物品，每次刷新时，数量会增加 [item\_template.BuyCount](item_template#buycount)。

### ExtendedCost

此处的值对应 [ItemExtendedCost.dbc](itemextendedcost_dbc#id) 中的 ID，该 ID 控制物品的非货币价格，无论是荣誉点数、竞技场点数、不同类型的徽章还是以上各项的组合。
