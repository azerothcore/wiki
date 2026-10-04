# spell\_cooldown\_overrides

[<-Back-to:World](database-world)

**The \`spell\_cooldown\_overrides\` table**

Used to give NPC spells cooldowns for mindcontroll.

**Table: spell\_cooldown\_overrides's Structure**

| Field                                           | Type |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [Id](#id)                                       | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [RecoveryTime](#recoverytime)                   | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [CategoryRecoveryTime](#categoryrecoverytime)   | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [StartRecoveryTime](#startrecoverytime)         | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [StartRecoveryCategory](#startrecoverycategory) | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [Comment](#comment)                             | TEXT |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
