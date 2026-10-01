# areatrigger\_involvedrelation

[<-返回:World](database-world)

**\`areatrigger\_involvedrelation\` 表**

使一个触发器能够完成任务的某一个条件（探索）

如果表中存在针对某个任务的记录，那么在该玩家激活此区域触发器之前，该任务不会完成。触发之后任务不一定立即完成，但该任务的这一个条件已经满足。如果该任务唯一的条件就是探索某个区域，那么任务就会完成。

**表结构**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comments         |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 标识符           |
| [quest][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | 任务标识符       |

[1]: #id
[2]: #quest

**字段描述**

### id

这是来自 [AreaTrigger.dbc](dbc-areatrigger) 的触发器 ID

### quest

这是触发器所关联的任务 ID。

### 示例

| id  | quest |
| --- | ----- |
| 78  | 155   |
| 87  | 76    |
| 88  | 62    |
| 98  | 201   |
| 169 | 287   |
