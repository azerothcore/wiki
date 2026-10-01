# character\_aura

[<-返回:Characters](database-characters)

**\`character\_aura\` 表**

包含角色加载时所载入的增益/减益（aura）信息，这样角色在登出时所带有的增益/减益在重新登录后仍然保留。一个法术最多可以有三个增益/减益效果，分别对应其三个法术效果。

**表结构**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                       |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [guid][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier      |
| [casterGuid][2]      | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       | Full Global Unique Identifier |
| [itemGuid][3]        | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [spell][4]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [effectMask][5]      | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [recalculateMask][6] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |
| [stackCount][7]      | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                               |
| [amount0][8]         | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [amount1][9]         | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [amount2][10]        | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount0][11]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount1][12]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount2][13]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [maxDuration][14]    | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainTime][15]     | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainCharges][16]  | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |

[1]: #guid
[2]: #casterguid
[3]: #itemguid
[4]: #spell
[5]: #effectmask
[6]: #recalculatemask
[7]: #stackcount
[8]: #amount
[9]: #amount
[10]: #amount
[11]: #baseamount0
[12]: #baseamount1
[13]: #baseamount2
[14]: #maxduration
[15]: #remaintime
[16]: #remaincharges

**字段说明**

### guid

受该增益/减益影响的目标的 GUID。参见 [characters.guid](characters#guid)。

### casterGuid

施放该增益/减益的玩家的 GUID。参见 [characters.guid](characters#guid)。

### itemGuid

施放该增益/减益的物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### spell

施加该增益/减益的法术。参见 [Spell.dbc](spell) 第 1 列。

### effectMask

该增益/减益来源法术的效果索引。一个法术最多有三个效果，索引为 0、1 或 2。

### recalculateMask

`field-no-description|5`

### stackcount

决定角色拥有该法术的叠加层数。

### amount

与该增益/减益相关联的修正值。

### base\_amount0

`field-no-description|11`

### base\_amount1

`field-no-description|12`

### base\_amount2

`field-no-description|13`

### maxduration

该增益/减益的最大持续时间，单位为毫秒。

### remaintime

该增益/减益的剩余时间，单位为毫秒。-1 表示该增益/减益为永久效果。

### remaincharges

该增益/减益剩余的充能次数。
