# spell\_script\_names

[<-Volver a: World](database-world)

**Tabla \`spell\_script\_names\`**

Contiene los emparejamientos de spell id a ScriptName para usar en spell scripts.

**Estructura**

| Field           | Type     | Attributes | Key    | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | ------ | ---- | ------- | ----- | ------- |
| [spell_id][1]   | INT      | SIGNED     | UNIQUE | NO   | NONE    |       |         |
| [ScriptName][2] | char(64) | UNSIGNED   | UNIQUE | NO   | NONE    |       |         |

[1]: #spellid
[2]: #scriptname

**Descripción de los campos**

### spell\_id

El ID del hechizo a enlazar. Si es negativo y es el primer rango de un hechizo, incluye todos los rangos del hechizo especificado en la tabla spell\_ranks.

Un hechizo puede tener más de un script asignado.

### ScriptName

El nombre del script para el/los hechizo(s) dado(s).
