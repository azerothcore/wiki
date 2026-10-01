# character\_instance

[<-返回:Characters](database-characters)

**\`character\_instance\` 表**

包含角色的副本（instance）数据。

**表结构**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [instance][2]  | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [permanent][3] | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [extended][4]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |

[1]: #guid
[2]: #instance
[3]: #permanent
[4]: #extended

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### instance

副本 ID。参见 [instance.id](instance#id)。

### permanent

布尔值 0 或 1，控制玩家是否已绑定到该副本。只有当玩家（或其队伍/团队）击杀了一个在 [flags\_extras](creature_template#flagsextra) 字段中设置了 CREATURE\_FLAG\_EXTRA\_INSTANCE\_BIND 标志的生物时，玩家才会被绑定到该副本。

### extended

布尔值（0 或 1）。如果为 1，表示玩家已将副本的重置计时器额外延长了一个重置周期。
