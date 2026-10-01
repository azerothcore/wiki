# linked_respawn

[<-返回:World](database-world)

**\`linked_respawn\` 表**

该表将小怪与首领关联起来，这样如果你击杀首领，在副本重置之前小怪不会重生。游戏对象（Gameobject）也可以被关联！

**表结构**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment            |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [guid][1]       | INT     | UNSIGNED   | PRI | NO   |         |       | Dependent Creature |
| [linkedGuid][2] | INT     | UNSIGNED   |     | NO   |         |       | Master Creature    |
| [linkType][3]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |                    |

[1]: #guid
[2]: #linkedguid
[3]: #linktype

**字段说明**

### guid

这是你想要关联的 [creature](creature#guid) 或 [gameobject](gameobject#guid) 的 guid。

### linkedGuid

这是你想要关联到的 [creature](creature#guid) 或 [gameobject](gameobject#guid)（通常为首领）的 guid。

### linkedType

| 值      | 从属        | 主控        |
| ----- | ---------- | ---------- |
| 0     | creature   | creature   |
| 1     | creature   | gameobject |
| 2     | gameobject | gameobject |
| 3     | gameobject | creature   |
