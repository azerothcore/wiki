# creature\_questender

[<-返回：世界](database-world)

**\`creature\_questender\` 表**

保存 NPC 任务结束者关系，即哪些 NPC 完成哪些任务。

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

该生物完成的任务 ID。参见 [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
