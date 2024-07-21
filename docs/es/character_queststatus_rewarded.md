# character\_queststatus\_rewarded

[<-Volver a:Characters](database-characters)

**Tabla \`character\_queststatus\_rewarded\`**

Esta tabla contiene información de ** cada ** misión recompensada para un jugador.

**Estructura**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT        | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2]  | INT        | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [active][3] | TINYINT    | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #quest
[3]: #active

**Descripción de los campos**

### guid

El GUID del carácter. Consulte  [characters.guid](characters#guid).

### quest

El ID de misión de la misión recompensada. Ver [quest\_template.id](quest_template#id).

### active

`campo-sin-descripción|3`
