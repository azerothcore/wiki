# pet\_aura

[<-返回至:Characters](database-characters)

**`pet_aura` 表**

**表结构**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                       |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [guid][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier      |
| [casterGuid][2]      | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       | Full Global Unique Identifier |
| [spell][3]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [effectMask][4]      | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [recalculateMask][5] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |
| [stackCount][6]      | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                               |
| [amount0][7]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount1][8]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount2][9]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount0][10]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount1][11]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount2][12]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [maxDuration][13]    | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainTime][14]     | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainCharges][15]  | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |

[1]: #guid
[2]: #casterguid
[3]: #spell
[4]: #effectmask
[5]: #recalculatemask
[6]: #stackcount
[7]: #amount
[8]: #amount
[9]: #amount
[10]: #baseamount
[11]: #baseamount
[12]: #baseamount
[13]: #maxduration
[14]: #remaintime
[15]: #remaincharges

## 字段说明

### guid

受该光环影响目标的 GUID。参见 [character\_pet.id](character_pet#id)。

### casterGuid

施放该光环的玩家的 GUID。参见 [characters.guid](characters#guid)。

### spell

该光环来自的法术。参见 [Spell.dbc](spell) 第 1 列。

### effectMask

光环所来自法术的效果索引。一个法术最多有三个效果，索引为 0、1 或 2。

### recalculateMask

`field-no-description|5`

### stackCount

决定角色拥有该法术的层数。

### amount

与该光环关联的修正值。

### base\_amount

`field-no-description|10-12`

### maxDuration

光环的最大持续时间。

### remainTime

光环剩余的秒数。-1 表示光环无限持续。

### remainCharges

光环剩余的充能次数。
