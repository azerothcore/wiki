# instance

[<-返回至:Characters](database-characters)

**`instance` 表**

此表保存了所有当前尚未重置的副本的静态信息。

**表结构**

| Field                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]                  | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [map][2]                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [resettime][3]           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [difficulty][4]          | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [completedEncounters][5] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [data][6]                | TINYTEXT | SIGNED     |     | NO   |         |       |         |

[1]: #id
[2]: #map
[3]: #resettime
[4]: #difficulty
[5]: #completedencounters
[6]: #data

**字段说明**

### id

副本 ID。此编号对每个副本都是唯一的。

### map

副本所在的地图 ID。参见 [Map.dbc](map)。

### resettime

副本将被重置的时间，以 Unix 时间表示。对于团队副本和英雄副本，此字段为零。
每个特定队伍的团队副本和英雄副本的重置时间存储在 [instance\_reset](instance_reset) 表中。

### difficulty

当前副本的难度。

| Value | Description   |
| ----- | ------------- |
| 0     | 10-man Normal |
| 1     | 25-man Normal |
| 2     | 10-man Heroic |
| 3     | 25-man Heroic |

### completedEncounters

此副本中已完成的首领战斗的位掩码。每一位对应实例脚本中定义的一场首领战斗。

### data

属于该单独副本的特定数据。
