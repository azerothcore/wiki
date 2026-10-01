# game\_event\_creature\_quest

[<-Volver a:World](database-world)

**Tabla \`game\_event\_creature\_quest\`**

Esta tabla contiene información sobre quests que solo deberían estar disponibles cuando un evento está teniendo lugar.

**Estructura**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [eventEntry][1] | TINYINT   | UNSIGNED   |     | NO   |         |       | Entry del evento de juego. |
| [id][2]         | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [quest][3]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                          |

[1]: #evententry
[2]: #id
[3]: #quest

**Descripción de los campos**

### eventEntry

El ID del evento. Ver game\_event.eventEntry

### id

El ID del NPC. Ver creature\_template.entry

### quest

El ID de la quest. Ver quest\_template.entry
