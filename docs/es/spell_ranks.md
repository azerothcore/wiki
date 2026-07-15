# spell\_ranks

[<-Volver a: World](database-world)

**Tabla \`spell\_ranks\`**

Tabla usada por el core para agrupar diferentes rangos de hechizos (el texto gris que se ve en los hechizos con rango) en un único "tronco de hechizo" (spell stem). Esto implica en parte comprobaciones para el apilamiento de auras (p. ej. distintos niveles del mismo hechizo). Un hechizo no puede estar vinculado a múltiples cadenas de rango (son "únicos").

**Estructura**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [first_spell_id][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]       | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [rank][3]           | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #first_spell_id
[2]: #spell_id
[3]: #rank

**Descripción de los campos**

### first\_spell\_id

SpellId de [Spell.dbc](spell) que es el primer rango de la cadena de rangos del hechizo. Identifica la cadena entera.

### spell\_id

SpellId de [Spell.dbc](spell).

### rank

Un entero que ordena el hechizo dentro de la cadena de rangos de hechizo para el \`spell\_id\` dado. Puede diferir del texto de rango en el juego (por ejemplo, algunos rangos en el cliente empiezan por el nivel 0, mientras que el servidor siempre empieza por el nivel 1 en adelante). Deben cumplirse varias condiciones:

-   Se requieren al menos dos niveles
-   No puede haber saltos entre rangos (p. ej. un hechizo siendo nivel 3 y otro siendo nivel 5 mientras falta por completo el nivel 4)
-   No puede haber duplicados en los rangos.
