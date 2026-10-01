# player_factionchange_titles

[<-返回至:World](database-world)

**`spell_cooldown_overrides` 表**

确定在阵营转换时应交换哪些头衔。

**表结构**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  |            | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            | PRI | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  |            | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            | PRI | YES  | NULL    |       |         |

**字段说明**

### alliance_id

来自 Titles.dbc 的 ID

### alliance_comment

头衔名称

### horde_id

来自 Titles.dbc 的 ID

### horde_comment

头衔名称
