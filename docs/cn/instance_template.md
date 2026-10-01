# instance\_template

[<-返回至:World](database-world)

**`instance\_template` 表**

此表包含每个副本的所有模板。当一个队伍进入副本时，会根据这些字段中的值创建该副本的新副本实例。

如果你想更改进入/离开副本时的起始位置，请前往 areatrigger\_teleport

**表结构**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [map][1]        | INT          | UNSIGNED   |     | NO   | NULL    |       |         |
| [parent][2]     | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |
| [script][3]     | VARCHAR(128) | SIGNED     |     | NO   | NULL    |       |         |
| [allowMount][4] | tinyiny(1)   | SIGNED     |     | NO   | 0       |       |         |

[1]: #map
[2]: #parent
[3]: #script
[4]: #allowmount

**字段说明**

### map

副本的地图 ID。参见 Maps.dbc

### parent

如果此副本是另一个副本的子副本，则此字段存放父副本的地图 ID。

### script

副本将使用并应用（如果有）的实例脚本的名称。

### allowMount

- 0 = 你不能在此副本内骑乘坐骑
- 1 = 你可以在此副本内骑乘坐骑
