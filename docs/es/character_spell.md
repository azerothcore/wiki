# character\_spell

[<-Volver a:Characters](database-characters)

**Tabla \`character\_spell\`**

Contiene información para los hechizos de cada personaje.

**Estructura**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier         |
| [specMask][3] | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #spell
[3]: #specmask

**Descripción de los campos**

### guid

El GUID del personaje. Consulte [characters.guid](characters#guid).

### spell

La identificación del hechizo. Consulte la columna 1 de[Spell.dbc](spell).

### specMask

Máscara de bits que guarda las especificaciones utilizando el hechizo.
| Value | Type                              |
| ----- | --------------------------------- |
| 1     | Primera especificación            |
| 2     | Segunda especificación            |
| 3     | Ambas especificaciones            |
