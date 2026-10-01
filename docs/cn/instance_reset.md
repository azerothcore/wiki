# instance\_reset

[<-返回至:Characters](database-characters)

**`instance\_reset` 表**

英雄副本和团队副本将被重置的日期和时间（即具有固定重置间隔的副本，该间隔与某些玩家进入副本的时间无关）。如果在 worldserver 配置中更改了 Rate.InstanceResetTime，请清除此表中的所有数据并重启服务器，以便用更新后的 "resettime" 重新填充。

**表结构**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [mapid][1]      | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [difficulty][2] | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [resettime][3]  | INT      | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #mapid
[2]: #difficulty
[3]: #resettime

**字段说明**

### mapid

副本所在的地图 ID。参见 [Map.dbc](map)。

### difficulty

副本难度。

### resettime

此副本（地图）将被重置的日期/时间，以 Unix 时间表示。
