# spell\_bonus\_data

[<-Volver a: World](database-world)

**Tabla \`spell\_bonus\_data\`**

Tabla usada para almacenar coeficientes personalizados de bonus de daño/curación.

**Estructura**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [direct_bonus][2] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [dot_bonus][3]    | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_bonus][4]     | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_dot_bonus][5] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [comments][6]     | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #direct_bonus
[3]: #dot_bonus
[4]: #ap_bonus
[5]: #ap_dot_bonus
[6]: #comments

**Descripción de los campos**

### entry

ID del hechizo. Ver Spell.dbc.

Solo el primer rango del hechizo necesita datos si el hechizo existe en Spell\_ranks y los coeficientes son iguales para cada rango.

### direct\_bonus

Daño directo de poder de hechizo (spell power).

Si < 0

Calcula el coeficiente de poder de hechizo por defecto.

Si = 0

No aplica ningún coeficiente de poder de hechizo. (No escala el daño con el poder de hechizo)

Si > 0

Usa esto como nuevo coeficiente de poder de hechizo.

### dot\_bonus

Daño de hechizo a lo largo del tiempo (damage over time).

Si < 0
Calcula el coeficiente de poder de hechizo por defecto.
Si = 0
No aplica ningún coeficiente de poder de hechizo. (No escala el daño con el poder de hechizo)
Si > 0
Usa esto como nuevo coeficiente de poder de hechizo.

### ap\_bonus

Daño directo cuerpo a cuerpo/a distancia.

Si < 0

Calcula el coeficiente de poder de ataque (attack power) por defecto.

Si = 0

No aplica ningún coeficiente de poder de ataque. (No escala el daño con el poder de ataque)

Si > 0

Usa esto como nuevo coeficiente de poder de ataque.

### ap\_dot\_bonus

Daño cuerpo a cuerpo/a distancia a lo largo del tiempo.

Si < 0

Calcula el coeficiente de poder de ataque por defecto.

Si = 0

No aplica ningún coeficiente de poder de ataque. (No escala el daño con el poder de ataque)

Si > 0

Usa esto como nuevo coeficiente de poder de ataque.

### comments

Comentario sobre por qué tiene tales valores y el nombre del hechizo.
