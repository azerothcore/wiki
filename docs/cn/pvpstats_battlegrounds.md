# pvpstats\_battlegrounds

[<-返回至:Characters](database-characters)

**\`pvpstats\_battlegrounds\` 表**

此表保存关于战场（BattleGround）得分的数据。要启用此类信息的存储，请在 **worldserver.config.dist** 文件中设置 **Battleground.StoreStatistics.Enable = 1**。

**表结构**

| Field               | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]             | BIGINT   | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [winner_faction][2] | TINYINT  | SIGNED     |     | NO   |         |                |         |
| [bracket_id][3]     | TINYINT  | UNSIGNED   |     | NO   |         |                |         |
| [type][4]           | TINYINT  | UNSIGNED   |     | NO   |         |                |         |
| [date][5]           | DATETIME | SIGNED     |     | NO   |         |                |         |

[1]: #id
[2]: #winnerfaction
[3]: #bracketid
[4]: #type
[5]: #date

**字段说明**

### id

标识某个战场（BattleGround）的唯一值。

### winner\_faction

赢得战场的阵营：

| Value | Description |
| ----- | ----------- |
| 0     | HORDE       |
| 1     | ALLIANCE    |
| 2     | NONE        |

### bracket\_id

标识分组等级范围：

| Value | Level range |
| ----- | ----------- |
| 1     | 10-19       |
| 2     | 20-29       |
| 3     | 30-39       |
| 4     | 40-49       |
| 5     | 50-59       |
| 6     | 60-69       |
| 7     | 70-79       |
| 8     | 80          |

### type

战场类型：

| Value | Description            |
| ----- | ---------------------- |
| 1     | Alterac Valley         |
| 2     | Warsong Gulch          |
| 3     | Arathi Basin           |
| 7     | Eye of the Storm       |
| 9     | Strand of the Ancients |
| 30    | Isle of Conquest       |

### date

战场结束的日期和时间。
