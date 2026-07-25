# spell_cooldown_overrides

[<-Volver a: World](database-world)

**Tabla \`spell_cooldown_overrides\`**

Se usa para dar cooldowns a los hechizos de NPC para el control mental (mindcontroll).

**Estructura**

| Field                                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                                       | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [RecoveryTime](#recoverytime)                   | INT  | UNSIGNED   |     | YES  | 0       |       |         |
| [CategoryRecoveryTime](#categoryrecoverytime)   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryTime](#startrecoverytime)         | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [StartRecoveryCategory](#startrecoverycategory) | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment](#comment)                             | TEXT |            |     | YES  | NULL    |       |         |

**Descripción de los campos**

### Id

ID del hechizo de [Spell.dbc](spell)

### RecoveryTime

`campo-sin-descripción|2`

### CategoryRecoveryTime

`campo-sin-descripción|3`

### StartRecoveryTime

`campo-sin-descripción|4`

### StartRecoveryCategory

`campo-sin-descripción|5`

### Comment

`campo-sin-descripción|6`
