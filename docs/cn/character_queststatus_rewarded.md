# character\_queststatus\_rewarded

[<-返回:Characters](database-characters)

**\`character\_queststatus\_rewarded\` 表**

该表保存玩家已获得的**每一个**已奖励任务的信息。

**表结构**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT        | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [quest][2]  | INT        | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符               |
| [active][3] | TINYINT    | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #quest
[3]: #active

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### quest

已奖励任务的任务 ID。参见 [quest\_template.id](quest_template#id)。

### active

始终设置为 1。用于在加载角色数据时在内部筛选出已奖励且处于激活状态的任务。
