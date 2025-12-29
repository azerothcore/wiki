# character\_talent

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../character_talent) [Spanish :es:](character_talent)

**Tabla \`character\_talent\`**

Contiene todos los datos de talentos individuales de cada personaje. Esto solo se usa como una tabla de almacenamiento, los valores se leen desde aquí y se escriben en character\_spell, y viceversa, cuando un jugador cambia de especificación.

**Estructura**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   |         |       |         |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [specMask][3] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #guid
[2]: #spell
[3]: #specmask

**Descripción de los campos**

### guid

El guid del personaje. Ver [characters.guid](characters#guid).

### spell

El id del hechizo. Ver [Spell.dbc](spell) columna 1.

### specMask

Máscara de bits que guarda las especificaciones utilizando el talent.
| Value | Type                              |
| ----- | --------------------------------- |
| 1     | Primera especificación            |
| 2     | Segunda especificación            |
| 3     | Ambas especificaciones            |
