# lfg\_dungeon\_rewards

[<-返回至:World](database-world)

**\`lfg\_dungeon\_rewards\` 表**

`table-no-description|0`

**表结构**

| Field              | Type    | Attributes | Key | Null | Default | Extra | Comment                                                                                         |
| ------------------ | ------- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------------------------------- |
| [dungeonId][1]     | INT     | UNSIGNED   | PRI | NO   | 0       |       | 来自 dbc 的副本条目                                                       |
| [maxlevel][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       | 发放此奖励的最高等级                                                      |
| [firstQuestId][3]  | INT     | UNSIGNED   |     | NO   | 0       |       | 当天第一次副本的带奖励的任务 id                                            |
| [otherQuestId][6]  | INT     | UNSIGNED   |     | NO   | 0       |       | 当天第 N 次副本的带奖励的任务 id                                          |

[1]: #dungeonid
[2]: #maxlevel
[3]: #firstquestid
[6]: #otherquestid

**字段说明**

### dungeonId

来自 LFGDungeons.dbc 的副本 ID

### maxlevel

发放此奖励的最高等级

### firstQuestId

当天第一次副本的带奖励的任务 Quest\_template.id。

### otherQuestId

当天第 N 次副本的带奖励的任务 Quest\_template.id
