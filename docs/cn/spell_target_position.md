# spell\_target\_position

[<-返回:世界数据库](database-world)

**\`spell\_target\_position\` 表**

该表保存当法术的目标类型为 TARGET\_DST\_DB(17) 时，玩家应该被传送到哪个位置的坐标信息。

**表结构**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | 标识符      |
| [EffectIndex][7]   | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |            |
| [MapID][2]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |            |
| [PositionX][3]     | FLOAT     |            |     | NO   | 0       |       |            |
| [PositionY][4]     | FLOAT     |            |     | NO   | 0       |       |            |
| [PositionZ][5]     | FLOAT     |            |     | NO   | 0       |       |            |
| [Orientation][6]   | FLOAT     |            |     | NO   | 0       |       |            |
| [VerifiedBuild][8] | INT       |            |     | YES  | NULL    |       |            |

[1]: #id
[2]: #mapid
[3]: #positionx
[4]: #positiony
[5]: #positionz
[6]: #orientation
[7]: #effectindex
[8]: #verifiedbuild

**字段说明**

### id

法术 ID。参见 [Spell.dbc](spell)

### EffectIndex

该目标位置所适用的法术效果索引。

### MapID

玩家应该被传送到的地图。参见 [Map.dbc](map)。

### PositionX

法术目标目的地的 X 坐标。

### PositionY

法术目标目的地的 Y 坐标。

### PositionZ

法术目标目的地的 Z 坐标。

### Orientation

玩家出现在该位置时获得的方向。

### VerifiedBuild

验证此行的客户端构建版本（来自 WDB/ADB 提取）。如不适用则为 `NULL`。
