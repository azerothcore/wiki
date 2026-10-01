# spawn\_group

[<-返回至:World](database-world)

**`spawn\_group` 表**

此表将单个生物和游戏对象的刷新（spawn）映射到各自的刷新组。每个刷新点只能属于一个组，该组通过 [spawn\_group\_template](spawn_group_template) 中定义的标志控制其重生行为。

**表结构**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnType](#spawntype) | TINYINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnId](#spawnid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |

**字段说明**

### groupId

这是该组的组 ID。它必须与 [spawn\_group\_template](spawn_group_template) 表中已存在的组相匹配。

### spawnType

这是刷新类型：

| Value | Type       |
| ----- | ---------- |
| 0     | 生物        |
| 1     | 游戏对象    |

### spawnId

这是应包含在组中的生物或游戏对象的刷新 ID（GUID）。该 ID 必须分别存在于 [creature](creature) 或 [gameobject](gameobject) 表中。
