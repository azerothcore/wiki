# character\_queststatus\_monthly

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../character_queststatus_monthly) [Spanish :es:](character_queststatus_monthly)

**Tabla \`character\_queststatus\_monthly\`**

**Estructura**

| Field       | Type | Attributes | Key | Null | Default | Extra  | Comment                  |
| ----------- | ---- | ---------- | --- | ---- | ------- | ------ | ------------------------ |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   | 0       |        | Global Unique Identifier |
| [quest][2]  | INT  | UNSIGNED   | PRI | NO   | 0       |        | Quest Identifier         |

[1]: #guid
[2]: #quest

**Descripción de los campos**

### guid

El guid del personaje. Ver [characters.guid](characters#guid).

### quest

El ID de misión de la misión recompensada. Ver [quest\_template.id](quest_template#id).
