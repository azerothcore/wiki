# character\_arena\_stats

[<-返回:Characters](database-characters)

**\`character\_arena\_stats\` 表**

该表保存了角色在所有战队类型中的匹配等级（matchmaker rating）信息。

**表结构**

| Field                 | Type        | Attributes | Key | Null | Default | Extra | Comment |
| --------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]             | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [slot][2]             | TINYINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [matchmakerRating][3] | SMALLINT    | UNSIGNED   |     | NO   |         |       |         |
| [maxMMR][4]           | SMALLINT    | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #slot
[3]: #matchmakerrating
[4]: #maxmmr

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### slot

竞技场槽位索引：

| 值 | 说明 |
| ----- | ----------- |
| 0     | 2v2         |
| 1     | 3v3         |
| 2     | 5v5         |

### matchmakerRating

玩家的匹配等级。

### maxMMR

该角色在此竞技场槽位中曾达到过的最高匹配等级（MMR）。
