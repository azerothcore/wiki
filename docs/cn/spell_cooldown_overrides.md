# spell_cooldown_overrides

[<-返回至:World](database-world)

**\`spell_cooldown_overrides\` 表**

用于为受心灵控制（mind control）影响的 NPC 法术提供冷却时间。

**表结构**

| Field                                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                                       | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [RecoveryTime](#recoverytime)                   | INT  | UNSIGNED   |     | YES  | 0       |       |         |
| [CategoryRecoveryTime](#categoryrecoverytime)   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryTime](#startrecoverytime)         | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryCategory](#startrecoverycategory) | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment](#comment)                             | TEXT |            |     | YES  | NULL    |       |         |

**字段说明**

### Id

来自 [Spell.dbc](spell) 的法术 ID

### RecoveryTime

`field-no-description|2`

### CategoryRecoveryTime

`field-no-description|3`

### StartRecoveryTime

`field-no-description|4`

### StartRecoveryCategory

`field-no-description|5`

### Comment

`field-no-description|6`
