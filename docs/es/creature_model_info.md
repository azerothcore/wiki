# creature\_model\_info

[<-Volver a:World](database-world)

**Tabla \`creature\_model\_info\`**

Esta tabla contiene todos los modelos de criaturas, su género y otra información relacionada con el modelo. Esto significa que cuando una criatura usa otro modelo, esta información también cambia.

**Estructura**

| Campo                       | Tipo    | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------------------- | ------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [DisplayID][1]              | int     | unsigned  | PRI   | NO   | 0           |       |            |
| [BoundingRadius][2]         | float   |           |       | NO   | 0           |       |            |
| [CombatReach][3]            | float   |           |       | NO   | 0           |       |            |
| [Gender][4]                 | tinyint | unsigned  |       | NO   | 2           |       |            |
| [DisplayID_Other_Gender][5] | int     | unsigned  |       | NO   | 0           |       |            |

[1]: #displayid
[2]: #boundingradius
[3]: #combatreach
[4]: #gender
[5]: #displayidothergender

**Descripción de los campos**

### DisplayID

ID de pantalla de [CreatureDisplayInfo.dbc](CreatureDisplayInfo)

### BoundingRadius

Este campo no se utiliza. Se desconoce su propósito. Puede estar relacionado con la búsqueda de rutas.

### CombatReach

Este valor es el radio de la unidad en términos de la mecánica del juego: cuanto mayor sea este valor, mayor será el alcance de la unidad y también más lejos podrá ser golpeada.

### Gender

Género de la criatura

| Valor | Descripción |
| ----- | ----------- |
| 0     | Masculino   |
| 1     | Femenino    |
| 2     | Ninguno     |

Nota: no modifique este campo sin rastrearlo o hablar con Kinzcool antes (ref. commit: http://git.io/T7RLmA).

### DisplayID_Other_Gender

Apunta a Creature\_modelo\_info.modelid.
Cuando la entrada es de género masculino (0) o femenino (1), este valor puede apuntar a la contraparte del género opuesto.
