# character\_achievement\_progress

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_achievement\_progress\`**

**Estructura**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [criteria][2] | SMALLINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [counter][3]  | INT         | UNSIGNED   |     | NO   |         |       |         |
| [date][4]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #criteria
[3]: #counter
[4]: #date

**Descripción de los campos**

### guid

El GUID del personaje. Consulte [characters.guid](characters#guid).

### criteria

Criterios de [Achievement\_Criteria.dbc](achievement_criteria).

### counter

`campo-sin-descripción|3`

### date

La fecha en la que se obtuvo este logro. Consulte [Unix timestamp Calculator](http://www.unixtimestamp.com/index.php).
