# player_factionchange_reputations

[<-返回至:World](database-world)

**`player_factionchange_reputations` 表**

基本上包含了玩家更换阵营时所做的所有阵营/声望变更。

**表结构**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            |     | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | SIGNED     | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            |     | YES  | NULL    |       |         |

**字段说明**

### alliance_id

这是联盟声望 ID。如果你转换到部落，且你的声望在此表中有对应记录，它们将被转换为 [\#horde_id](#hordeid)

参见 [character_reputation.faction](character_reputation#faction)

### alliance_comment

注释

### horde_id

这是部落声望 ID。如果你转换到联盟，且你的声望在此表中有对应记录，它们将被转换为 [\#alliance_id](#allianceid)

参见 [character_reputation.faction](character_reputation#faction)

### horde_comment

注释
