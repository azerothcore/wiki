# game_graveyard

[<-返回:世界](database-world)

**\`game_graveyard\` 表**

| 字段 (Field)          | 类型 (Type)    | 键 (Key) | 空 (Null) | 默认 (Default) |
| --------------------- | -------------- | -------- | --------- | -------------- |
| [ID](#id)             | INT            | PRI      | NO        | 0              |
| [Map](#map)           | INT            |          | NO        | 0              |
| [x](#x)               | FLOAT          |          | NO        | 0              |
| [y](#y)               | FLOAT          |          | NO        | 0              |
| [z](#z)               | FLOAT          |          | NO        | 0              |
| [Comment](#omment)    | VARCHAR(255)   |          | YES       | NULL           |

**字段说明**

### ID
墓地的 ID。参见 [WorldSafeLocs.dbc](https://wowdev.wiki/DB/WorldSafeLocs)

### Map
传送到墓地之前幽灵（ghost）位置所在区域的 ID。参见 Map.dbc 第 1 列

### x

角色幽灵被传送到的墓地的 X 坐标。

### y

角色幽灵被传送到的墓地的 Y 坐标。

### z

角色幽灵被传送到的墓地的 Z 坐标。

### Comment

该行的自定义注释。
