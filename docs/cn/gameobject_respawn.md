# gameobject\_respawn

[<-返回:Characters](database-characters)

**\`gameobject\_respawn\` 表**

此表保存游戏对象应重新生成（re-spawn）到世界中的重生时间。在服务器崩溃的情况下，此表保存了重生数据，以便游戏对象不会在服务器重启时立即重生。游戏对象重生时间的保存频率可以在 trinitycore.conf 中的 SaveRespawnTimeImmediately 处进行控制。通常需要消失并重新生成的只有宝箱（chests）和门（doors）。

**表结构**

| 字段            | 类型     | 属性     | 键 | 空 | 默认值 | 额外 | 注释                  |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符 |
| [respawnTime][2] | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mapId][3]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [instanceId][4]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | 副本标识符      |

[1]: #guid
[2]: #respawntime
[3]: #mapid
[4]: #instanceid

**字段说明**

### guid

游戏对象的 GUID。参见 [gameobject.guid](gameobject#guid)。

### respawnTime

游戏对象应重生的时间，以 Unix 时间表示。

### mapid

此 gameobject 重生条目所适用的地图 ID。

### instanceId

如果游戏对象原本属于某个副本，则此字段保存该游戏对象应重生的副本 ID。每个副本因队伍不同而不同，因此此字段对于跟踪哪些游戏对象应在何时为哪些玩家重生至关重要。
