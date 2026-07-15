# creature\_model\_info

[<-Volver a: World](database-world)

**Tabla \`creature\_model\_info\`**

Esta tabla contiene todos los modelos de los mobs, su género y otra información relacionada con el modelo. Esto significa que cuando una criatura usa otro modelo, esta información también cambiará.

**Estructura**

| Field                       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [DisplayID][1]              | int     | unsigned   | PRI | NO   | 0       |       |         |
| [BoundingRadius][2]         | float   |            |     | NO   | 0       |       |         |
| [CombatReach][3]            | float   |            |     | NO   | 0       |       |         |
| [Gender][4]                 | tinyint | unsigned   |     | NO   | 2       |       |         |
| [DisplayID_Other_Gender][5] | int     | unsigned   |     | NO   | 0       |       |         |

[1]: #displayid
[2]: #boundingradius
[3]: #combatreach
[4]: #gender
[5]: #displayidothergender

**Descripción de los campos**

### DisplayID

Display ID de [CreatureDisplayInfo.dbc](creaturedisplayinfo)

### BoundingRadius

Este campo no se usa. Su propósito es actualmente desconocido. Puede o no estar relacionado con el pathfinding.

### CombatReach

Este valor es el radio de la unidad en términos de mecánicas de juego: cuanto mayor sea este valor, mayor será el alcance de la unidad y también desde más lejos podrá recibir golpes.

### Gender

Género de la criatura

| Value | Description |
| ----- | ----------- |
| 0     | Male        |
| 1     | Female      |
| 2     | None        |

Nota: no modifiques este campo sin sniffs (ref commit: http://git.io/T7RLmA).

### DisplayID_Other_Gender

Apunta a Creature\_model\_info.modelid.
Cuando el entry es de género masculino (0) o femenino (1), este valor puede apuntar a la contraparte del género opuesto.
