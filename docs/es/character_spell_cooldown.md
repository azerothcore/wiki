# character\_spell\_cooldown

[<-Volver a:Characters](database-characters)

**Tabla \`character\_spell\_cooldown\`**

Mantiene la recarga de hechizos restantes de los personajes o del hechizo de un Item por cada personaje.

**Estructura**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier                   |
| [item][3]     | INT       | UNSIGNED   |     | NO   | 0       |       | Item Identifier                    |
| [time][4]     | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |
| [needSend][5] | INT       | UNSIGNED   |     | NO   | 1       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #item
[4]: #time
[5]: #needsend

**Descripción de los Campos**

### guid

Identificador Global Único o GUID del personaje. Véase [characters.guid](characters#guid).

### spell

ID del hechizo en particular. Véase [Spell.dbc](spell) columna 1.

### item

Si el hechizo fue lanzado desde un Item, el ID del Item en este caso. Véase [item\_template.entry](item_template#entry).

### time

El tiempo en que terminará la recarga del hechizo, medido en [Tiempo Unix](https://es.wikipedia.org/wiki/Tiempo_Unix).

### needSend

`Campo-sin-descripción|5`
