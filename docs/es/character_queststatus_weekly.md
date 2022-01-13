# character\_queststatus\_weekly

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_queststatus\_weekly\`**

Contiene información sobre el estado de las misiones semanales de cada jugador. Los temporizadores se reinician al mismo tiempo que se reinician las incursiones.

**Estructura**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |

[1]: #guid
[2]: #quest

**Descripción de los campos**

### guid

El GUID del personaje. Consulte [characters.guid](characters#guid).

### quest

El ID de misión de la misión recompensada. Consulte [quest\_template.id](quest_template#id).
