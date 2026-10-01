# player_factionchange_achievement

[<-返回至:World](database-world)

**`player_factionchange_achievement` 表**

基本上是玩家更换阵营时所做的所有成就变更。

**表结构**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            |     | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | SIGNED     | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            |     | YES  | NULL    |       |         |

## 字段说明

### alliance_id

联盟成就 ID。如果你转换到部落，且你的成就在此表中有对应记录，它们将被转换为 [\#horde_id](##hordeid)

### alliance_comment

注释

### horde_id

部落成就 ID。如果你转换到联盟，且你的成就在此表中有对应记录，它们将被转换为 [\#alliance_id](#allianceid)

### horde_comment

注释
