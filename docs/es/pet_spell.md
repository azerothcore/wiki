# pet\_spell

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../pet_spell) [Spanish :es:](pet_spell)

**Tabla \`pet\_spell\`**

Esta tabla contiene información sobre hechizos de mascotas individuales.

**Estructura**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier         |
| [active][3] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #spell
[3]: #active

**Descripción de los campos**

### guid

GUID de la mascota. Ver [character\_pet.id](character_pet#id).

### spell

ID del hechizo. Ver [Spell.dbc](spell) columna 1.

### active

Boolean 0 o 1 que controla si el hechizo está activo o no.
