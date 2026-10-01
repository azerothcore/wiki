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

Replaces the cooldown of the spell, in milliseconds. See [spell\_dbc.RecoveryTime](spell_dbc#recoverytime).

### CategoryRecoveryTime

Replaces the category cooldown of the spell, in milliseconds. See [spell\_dbc.CategoryRecoveryTime](spell_dbc#categoryrecoverytime).

### StartRecoveryTime

Replaces the global cooldown the spell starts, in milliseconds. See [spell\_dbc.StartRecoveryTime](spell_dbc#startrecoverytime).

### StartRecoveryCategory

Replaces the global cooldown category of the spell. See [spell\_dbc.StartRecoveryCategory](spell_dbc#startrecoverycategory).

### Comment

A description of the entry. Not used by the core.
