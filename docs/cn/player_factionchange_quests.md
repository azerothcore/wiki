# player_factionchange_quest

[<-返回至:World](database-world)

**`player_factionchange_quest` 表**

确定在阵营转换时应更改哪些任务。

**表结构**

| Field                      | Type | Attributes | Key        | Null | Default | Extra | Comment |
| -------------------------- | ---- | ---------- | ---------- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid) | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |
| [horde_id](#hordeid)       | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |

**字段说明**

### alliance_id

[quest_template.id](quest_template#id)。

### horde_id

[quest_template.id](quest_template#id)。
