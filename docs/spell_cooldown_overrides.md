# spell_cooldown_overrides

[<-Back-to:World](database-world)

**The \`spell_cooldown_overrides\` table**

Used to give NPC spells cooldowns for mindcontroll.

**Table Structure**

| Field                                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                                       | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [RecoveryTime](#recoverytime)                   | INT  | UNSIGNED   |     | YES  | 0       |       |         |
| [CategoryRecoveryTime](#categoryrecoverytime)   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryTime](#startrecoverytime)         | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryCategory](#startrecoverycategory) | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment](#comment)                             | TEXT |            |     | YES  | NULL    |       |         |

**Description of the fields**

### Id

Spell ID from [Spell.dbc](spell)

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
