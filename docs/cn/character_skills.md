# character\_skills

[<-返回:Characters](database-characters)

**\`character\_skills\` 表**

该表保存每个角色的所有技能列表。

**表结构**

| Field      | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [skill][2] | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [value][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [max][4]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #skill
[3]: #value
[4]: #max

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### skill

角色拥有的技能。这些技能的列表可以在此处找到。

### value

角色当前拥有的技能等级（value）。

### max

给定技能在某一等级内可以达到的最大值。
