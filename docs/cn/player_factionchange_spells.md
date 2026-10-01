# player_factionchange_spells

[<-返回至:World](database-world)

**`player_factionchange_spells` 表**

基本上包含了玩家更换阵营时所做的所有法术变更。

**表结构**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment][3] | TEXT |        |     | NO   |         |       |         |
| [horde_id][2]    | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_comment][4] | TEXT |          |     | NO   |         |       |         |

[1]: #allianceid
[2]: #hordeid
[3]: #alliancecomment
[4]: #hordecomment

**字段说明**

### alliance_id

这是联盟法术 ID。如果你转换到部落，且你的法术在此表中有对应记录，它们将被转换为 [\#horde_id](#hordeid)

### alliance_comment

便于识别联盟法术的可选注释（例如法术名称）。

### horde_id

这是部落法术 ID。如果你转换到联盟，且你的法术在此表中有对应记录，它们将被转换为 [\#alliance_id](#allianceid)

### horde_comment

便于识别部落法术的可选注释（例如法术名称）。
