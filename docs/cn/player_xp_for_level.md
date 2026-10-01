# player_xp_for_level

[<-返回至:World](database-world)

**`player_xp_for_level` 表**

包含升到下一级所需经验值的信息。数据来自抓包（sniffs）。

**表结构**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Level][1]      | TINYINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [Experience][2] | INT     | UNSIGNED   |     | NO   | NULL    |       |         |

[1]: #level
[2]: #experience

**字段说明**

该表设置了玩家升级所需经验值。

### Level

玩家等级。

### Experience

从 "lvl" 字段的值升级到 "lvl" + 1 所需的经验值。

### 示例

| Level | Experience |
| ----- | ---------- |
| 1     | 400        |
| 2     | 900        |
| 3     | 1400       |
| 4     | 2100       |
| 5     | 2800       |
