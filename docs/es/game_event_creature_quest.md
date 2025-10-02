# game\_event\_creature\_quest

[<-Volver a:World](database-world)

**Tabla \`game\_event\_creature\_quest\`**

Esta tabla contiene información sobre misiones que solo deberían estar disponibles cuando hay un evento en curso.

**Estructura**

| Campo           | Tipo      | Atributo | Llave | Nulo | Por defecto | Extra | Comentario                    |
| --------------- | --------- | -------- | ----- | ---- | ----------- | ----- | ----------------------------- |
| [eventEntry][1] | TINYINT   | UNSIGNED |       | NO   |             |       | Entrada del evento del juego. |
| [id][2]         | MEDIUMINT | UNSIGNED | PRI   | NO   | 0           |       |                               |
| [quest][3]      | MEDIUMINT | UNSIGNED | PRI   | NO   | 0           |       |                               |

[1]: #evententry
[2]: #id
[3]: #quest

**Descripción de los campos**

### eventEntry

El ID del evento. Véase game\_event.eventEntry

### id

El ID del NPC. Véase criatura\_template.entry

### quest

El ID de la misión. Ver quest\_template.entry
