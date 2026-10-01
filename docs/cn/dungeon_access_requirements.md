# dungeon\_access\_requirements

[<-返回:世界](database-world)

**\`dungeon\_access\_requirements\` 表**

**表结构**

| 字段                  | 类型         | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
| ---------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [dungeon_access_id][1] | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_type][2]  | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_id][3]    | MEDIUMINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_note][4]  | VARCHAR(255) |            |     | YES  | NULL    |       |         |
| [faction][5]           | TINYINT      | UNSIGNED   |     | NO   | 2       |       |         |
| [priority][6]          | TINYINT      | UNSIGNED   |     | YES  | NULL    |       |         |
| [leader_only][7]       | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [comment][8]           | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #dungeonaccessid
[2]: #requirementtype
[3]: #requirementid
[4]: #requirementnote
[5]: #faction
[6]: #priority
[7]: #leaderonly
[8]: #comment

**字段说明**

### dungeon_access_id

来自 [dungeon_access_template.id](dungeon_access_template#id) 的 ID。

### requirement_type

| 值 | 类型        | 注释                         |
| :---- | :---------- | :------------------------------ |
| 0     | 成就 (Achievement) |                                 |
| 1     | 任务 (Quest)       |                                 |
| 2     | 物品 (Item)        | 该物品不能在银行中。 |

### requirement_id

取决于所选的 [requirement_type][2]，为成就、任务或物品的 ID。

### requirement_note

当你未满足要求就试图进入副本时所显示的文本。

### faction

| 值 | 注释  |
| :---- | :------- |
| 0     | 联盟 (Alliance) |
| 1     | 部落 (Horde)    |
| 2     | 双方 (Both)     |

### priority

要求的优先级顺序，按类型排序。0 为最高优先级。

### leader_only

0 = 对每个试图进入的玩家都检查要求。

1 = 仅检查队伍队长是否满足要求。

### comment
