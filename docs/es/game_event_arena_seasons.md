# game_event_arena_seasons

[<-Volver a:World](database-world)

**Tabla \`game_event_arena_seasons\`**

Esta información proviene de rastreos y NO debe modificarse.

**Estructura**

| Campo           | Tipo    | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                    |
| --------------- | ------- | --------- | ----- | ---- | ----------- | ------ | ----------------------------- |
| [eventEntry][1] | TINYINT | UNSIGNED  |       | NO   |             | Unique | Entrada del evento del juego. |
| [season][2]     | TINYINT | UNSIGNED  |       | NO   |             | Unique | Número de temporada de Arena  |

[1]: #evententry
[2]: #season

**Descripción de los campos**

### eventEntry

[game_event.eventEntry](game_event#eventEntry)

### season

Número de temporada de Arena: 1 - 9

| eventEntry | season | Comentario (no forma parte de la base de datos) |
| ---------- | ------ | :---------------------------------------------- |
| 75         | 1      | TBC - Season 1: "Gladiator"                     |
| 76         | 2      | TBC - Season 2: "Merciless Gladiator"           |
| 55         | 3      | TBC - Season 3: "Vengeful Gladiator"            |
| 56         | 4      | TBC - Season 4: "Brutal Gladiator"              |
| 57         | 5      | WotLK - Season 5: "Deadly Gladiator"            |
| 58         | 6      | WotLK - Season 6: "Furious Gladiator"           |
| 59         | 7      | WotLK - Season 7: "Relentless Gladiator"        |
| 60         | 8      | WotLK - Season 8: "Wrathful Gladiator"          |
| 31         | 9      | Arena Tournament: (No utilizar)                  |
