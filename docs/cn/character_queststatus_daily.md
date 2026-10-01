# character\_queststatus\_daily

[<-返回:Characters](database-characters)

**\`character\_queststatus\_daily\` 表**

保存每个玩家每日任务的状态信息。任务必须是 type = 87，或者在 QuestFlags 中带有 4096 标志。

**表结构**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|----------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [quest][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符               |
| [time][3]  | INT     | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #quest
[3]: #time

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### quest

每日任务的任务 ID。参见 [quest\_template.entry](quest_template#entry)。

### time

任务领取的时间，以 Unix 时间表示。
