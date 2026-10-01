# creature\_queststarter

[<-返回：世界](database-world)

**\`creature\_queststarter\` 表**

保存 NPC 任务给予者关系，即哪些 NPC 开始哪些任务。

**表结构**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 标识符       |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符 |

[1]: #id
[2]: #quest

**字段说明**

### id

生物 ID。参见 [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

该生物开始的任务 ID。参见 [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
