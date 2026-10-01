# creature\_respawn

[<-返回：角色](database-characters)

**\`creature\_respawn\` 表**

该表保存生物在世界中应被刷新的时间。在服务器崩溃的情况下，该表保存刷新数据，以便生物不会在服务器重启时立即刷新。生物刷新时间的保存频率可在 worldserver.conf.dist 的 SaveRespawnTimeImmediately 中进行控制。

**表结构**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符 |
| [respawnTime][2] | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mapId][3]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [instanceId][4]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | 实例标识符      |

[1]: #guid
[2]: #respawntime
[3]: #mapid
[4]: #instance

**字段说明**

### guid

角色 guid。参见 [characters.guid](characters#guid)。

### respawnTime

生物应被刷新的时间，以 Unix 时间表示。

### mapId

该生物刷新记录所适用的地图 ID。

### instance

如果生物在某个实例中被击杀，该字段保存该生物应在其中刷新的实例 ID。每个实例根据队伍的不同而不同，因此该字段对于跟踪哪些生物应在何时为哪些玩家刷新至关重要。
