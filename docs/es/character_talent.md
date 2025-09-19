# character\_talent

[<-Volver a:Characters](database-characters)

**Tabla \`character\_talent\`**

Contiene todos los datos de talentos individuales de cada personaje. Esto solo se usa como una tabla de almacenamiento, los valores se leen desde aquí y se escriben en character\_spell, y viceversa, cuando un jugador cambia de especificación.

**Estructura**

| Campo         | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [guid][1]     | INT       | UNSIGNED  | PRI   | NO   |             |       |            |
| [spell][2]    | MEDIUMINT | UNSIGNED  | PRI   | NO   |             |       |            |
| [specMask][3] | TINYINT   | UNSIGNED  | PRI   | NO   | 0           |       |            |

[1]: #guid
[2]: #spell
[3]: #specmask

**Descripción de los campos**

### guid

El guid del personaje. Ver [characters.guid](characters#guid).

### spell

El id del hechizo. Ver [Spell.dbc](spell) columna 1.

### specMask

| Valor | Datos                        | 
| ----- | ---------------------------- |
| 0     | es la primera especificación | 
| 1     | es la segunda especificación |
