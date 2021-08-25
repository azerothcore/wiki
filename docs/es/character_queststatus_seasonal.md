﻿# character\_queststatus\_seasonal

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_queststatus\_seasonal\`**

Contiene información sobre el estado de la misión de temporada (misiones con ZoneOSort of -22) de cada jugador. Las misiones se reinician al final de la entrada de evento correspondiente.

**Estructura**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [event][3] | INT     | UNSIGNED   |     | NO   | 0       |       | Event Identifier         |

[1]: #guid
[2]: #quest
[3]: #event

**Descripción de los campos**

### guid

El GUID del personaje. Consulte [characters.guid](characters#guid).

### quest

El ID de misión de la misión recompensada. Consulte [quest\_template.id](quest_template#id).

### event

El eventEntry del evento del juego al que pertenece la misión de temporada.
