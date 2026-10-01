# character\_queststatus\_monthly

[<-返回:Characters](database-characters)

**\`character\_queststatus\_monthly\` 表**

**表结构**

| Field       | Type | Attributes | Key | Null | Default | Extra  | Comment                  |
| ----------- | ---- | ---------- | --- | ---- | ------- | ------ | ------------------------ |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   | 0       |        | 全局唯一标识符           |
| [quest][2]  | INT  | UNSIGNED   | PRI | NO   | 0       |        | 任务标识符               |

[1]: #guid
[2]: #quest

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### quest

已奖励任务的任务 ID。参见 [quest\_template.id](quest_template#id)。
