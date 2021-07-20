# pet\_spell\_cooldown

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../pet_spell_cooldown) [Spanish :es:](pet_spell_cooldown)

**Tabla \`pet\_spell\_cooldown\`**

Esta tabla contiene información sobre los tiempos de reutilización de hechizos de las mascotas.

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]  | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier                   |
| [time][3]  | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #time

**Descripción de los campos**

### guid

El GUID de la mascota. Ver [character\_pet.id](character_pet#id).

### spell

El ID del hechizo al que se aplica el tiempo de reutilización. Ver [Spell.dbc](spell) columna 1.

### time

El momento en que expira el tiempo de reutilización, en tiempo Unix.
