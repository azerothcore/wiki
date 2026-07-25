# lfg_dungeon_template

[<-Volver a:World](database-world)

**Tabla \`lfg_dungeon_template\`**

Se usa para dar cooldowns a los spells de los NPC para el control mental (mindcontroll).

**Estructura**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                        |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------ |
| [dungeonId](#dungeonid)         | INT          | UNSIGNED   | PRI | NO   | 0       |       | Unique id from LFGDungeons.dbc |
| [name](#name)                   | VARCHAR(255) |            |     | YES  | NULL    |       |                                |
| [position_x](#positionx)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_y](#positiony)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_z](#positionz)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [orientation](#orientation)     | FLOAT        |            |     | NO   | 0       |       |                                |
| [VerifiedBuild](#verifiedbuild) | INT          |            |     | YES  | NULL    |       |                                |

**Descripción de los campos**

### DungionId

Unique id from LFGDungeons.dbc

### name

Nombre de la mazmorra

### poisition_x

`campo-sin-descripción|3`

### poisition_y

`campo-sin-descripción|4`

### poisition_z

`campo-sin-descripción|5`

### orientation

`campo-sin-descripción|6`

### VerifiedBuild

Este campo se usa para determinar si los datos proceden de sniffs verificados.

Si el valor es 0 entonces aún no se ha parseado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0 entonces se ha parseado con sniffs de esa build de cliente concreta.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
