# player\_factionchange\_items

[<-返回至:World](database-world)

**`player_factionchange_items` 表**

基本上是玩家更换阵营时所做的所有物品变更。

**表结构**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][2]      | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment][3] | TEXT |            |     | NO   |         |       |         |
| [horde_id][5]         | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_comment][6]    | TEXT |            |     | NO   |         |       |         |

[2]: #allianceid
[3]: #alliancecomment
[5]: #hordeid
[6]: #hordecomment

## 字段说明

### alliance\_id

联盟物品 ID。如果你转换到部落，且你的物品在此表中有对应记录，它们将被转换为 [\#horde\_id](#hordeid)

### alliance\_comment

用于方便识别物品名称。注释格式应为 name(ItemLevel)

### horde\_id

部落物品 ID。如果你转换到联盟，且你的物品在此表中有对应记录，它们将被转换为 [\#alliance\_id](#allianceid)

### horde\_comment

用于方便识别物品名称。注释格式应为 name (ItemLevel)
