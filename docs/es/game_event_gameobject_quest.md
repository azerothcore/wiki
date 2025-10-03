# game\_event\_gameobject\_quest

[<-Volver a:World](database-world)

**Tabla \`game\_event\_gameobject\_quest\`**

Esta tabla contiene información sobre misiones que solo deberían estar disponibles cuando hay un evento en curso.

**Estructura**

| Campo           | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                   |
| --------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------------------------- |
| [eventEntry][1] | TINYINT   | UNSIGNED  | PRI   | NO   |             |       | Entrada del evento del juego |
| [id][2]         | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |                              |
| [quest][3]      | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |                              |

[1]: #evententry
[2]: #id
[3]: #quest

**Descripción de los campos**

### id

El ID del objeto del juego. Ver gameobject\_template.entry

### quest

El ID de la misión. Ver quest\_template.entry

### eventEntry

El identificador del evento. Ver game\_event.eventEntry
