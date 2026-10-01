# areatrigger\_tavern

[<-返回:World](database-world)

**\`areatrigger\_tavern\` 表**

当玩家进入城市或旅店时启用一个触发器。这会使玩家进入休息状态。

**表结构**

| Field     | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| --------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 标识符     |
| [name][2] | text      |            |     | YES  |         |       |            |
| [faction][3] | INT    | UNSIGNED   |     | NO   | 0       |       |            |

[1]: #id
[2]: #name
[3]: #faction

**字段描述**

### id

这是触发器标识符，参见 [AreaTrigger.dbc](dbc-areatrigger)

### name

城市或旅店的名称。这纯粹用于描述目的。

### faction

休息触发器生效所需的阵营。`0` 表示没有阵营限制。

### 示例

| id  | name                                         |
| --- | -------------------------------------------- |
| 71  | Westfall - Sentinel Hill Inn                 |
| 98  | Nesingwary's Expedition                      |
| 178 | Strahnbrad                                   |
| 562 | Elwynn Forest - Goldshire - Lion's Pride Inn |
| 682 | Redridge Mountains - Lakeshire Inn           |
