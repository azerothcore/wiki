# character_achievement_offline_updates

[<-返回至:Characters](database-characters)

**\`character_achievement_offline_updates\` 表**

存储角色离线时对其成就的更新。

**表结构**

| Field                       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid](#guid)               | INT     | UNSIGNED   | IDX | NO   |         |       |         |
| [update_type](#updatetype)  | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [arg1](#arg1)               | INT     | UNSIGNED   |     | NO   |         |       |         |
| [arg2](#arg2)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |
| [arg3](#arg3)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### update_type

支持的类型：1 - COMPLETE_ACHIEVEMENT；2 - UPDATE_CRITERIA

### arg1

对于类型 1：成就 ID；对于类型 2：ACHIEVEMENT_CRITERIA_TYPE

### arg2

对于类型 2：用于更新成就条件（criteria）的 miscValue1

### arg3

对于类型 2：用于更新成就条件（criteria）的 miscValue1
