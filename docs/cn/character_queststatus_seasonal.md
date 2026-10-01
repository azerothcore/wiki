# character\_queststatus\_seasonal

[<-返回:Characters](database-characters)

**\`character\_queststatus\_seasonal\` 表**

保存每个玩家季节性任务（ZoneOrSort 为 -22 的任务）的状态信息。这些任务会在对应的 eventEntry 结束时重置。

**表结构**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [quest][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符               |
| [event][3] | INT     | UNSIGNED   |     | NO   | 0       |       | 事件标识符               |

[1]: #guid
[2]: #quest
[3]: #event

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### quest

已奖励任务的任务 ID。参见 [quest\_template.id](quest_template#id)。

### event

该季节性任务所属游戏事件的 eventEntry。
