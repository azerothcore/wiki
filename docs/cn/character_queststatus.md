# character\_queststatus

[<-返回:Characters](database-characters)

**\`character\_queststatus\` 表**

保存每个角色的任务状态信息。

**表结构**

| Field             | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | -------- | ---------- | --- | ---- | ------- |------ | ------------------------ |
| [guid][1]         | INT      | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [quest][2]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符               |
| [status][3]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [explored][4]     | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [timer][5]        | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount1][6]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount2][7]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount3][8]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount4][9]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount1][10]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount2][11]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount3][12]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount4][13]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount5][14]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount6][15]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [playercount][16] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #quest
[3]: #status
[4]: #explored
[5]: #timer
[6]: #mobcount
[7]: #mobcount
[8]: #mobcount
[9]: #mobcount
[10]: #itemcount
[11]: #itemcount
[12]: #itemcount
[13]: #itemcount
[14]: #itemcount
[15]: #itemcount
[16]: #playercount

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### quest

任务 ID。参见 [quest\_template.entry](quest_template#entry)。

### status

当前任务状态。

**可能的值**

| Value | Status                     | Comments                                    |
| ----- | -------------------------- | ------------------------------------------- |
| 0     | QUEST\_STATUS\_NONE        | 任务不显示在任务列表中；默认值              |
| 1     | QUEST\_STATUS\_COMPLETE    | 任务已完成                                  |
| 2     | QUEST\_STATUS\_UNAVAILABLE | 未使用                                      |
| 3     | QUEST\_STATUS\_INCOMPLETE  | 任务在任务日志中处于激活状态但尚未完成      |
| 4     | QUEST\_STATUS\_AVAILABLE   | 未使用                                      |
| 5     | QUEST\_STATUS\_FAILED      | 玩家未能完成该任务                          |

### explored

布尔值（1 或 0），表示角色是否已探索完成该任务所需的探索区域。

### timer

限时任务剩余的完成时间（以毫秒为单位）。仅用于有时间限制的任务。

### mobcount

针对第一个生物或游戏对象（如果有）当前的击杀或施法计数。与 quest\_template 表对应。

### itemcount

交付类任务中第一个物品（如果有）当前的物品数量。与 quest\_template 表对应。

### playercount

当前的玩家击杀计数。在 quest\_template 中必需。
