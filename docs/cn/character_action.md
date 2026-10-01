# character\_action

[<-返回至:Characters](database-characters)

**\`character\_action\` 表**

包含每个角色的所有单独按钮数据。按钮是 GUI 中你可以在其中放置例如法术、物品或宏作为快捷方式的任何位置。

**表结构**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spec][2]   | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [action][4] | INT        | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | TINYINT    | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #spec
[3]: #button
[4]: #action
[5]: #type

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### spec

spec = 0 是第一个专精，spec = 1 是第二个专精。

### button

动作条上动作图标将被放置的按钮 ID。

特殊动作条用于姿态、光环、宠物、潜行和其他类似的特殊模式。

**可能的值**

| 按钮 ID | 动作条（键位）               |
| ------- | ---------------------------- |
| 1-11    | 1 (SHIFT + 1)                |
| 12-23   | 2 (SHIFT + 2)                |
| 24-35   | 3 (SHIFT + 3) h1. 右侧动作条  |
| 36-47   | 4 (SHIFT + 4) 右侧动作条 2    |
| 48-59   | 5 (SHIFT + 5) h1. 右下动作条  |
| 60-71   | 6 (SHIFT + 6) 左下动作条      |
| 72-83   | 1 特殊A                      |
| 84-95   | 1 特殊B                      |
| 96-107  | 1 特殊C                      |
| 108-119 | 1 特殊D                      |

### action

根据 type 的值，这可能是法术 ID（Spell.dbc）、物品 ID 或宏 ID。

### type

动作的类型：

**可能的类型**

| 值   | 描述     |
| ---- | -------- |
| 0    | 法术     |
| 1    | 点击     |
| 32   | 装备方案 |
| 64   | 宏       |
| 65   | 点击宏   |
| 128  | 物品     |
