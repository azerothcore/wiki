# game_event_creature

[<-Volver a:World](database-world)

**Tabla \`game_event_creature\`**

Contiene todas las instancias de creature que deben aparecer/desaparecer durante los eventos de juego definidos.

**Estructura**

| Field                     | Type     | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| ------------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED     |     | NO   |         |        | Entry del evento de juego. Pon un entry negativo para eliminar durante el evento. |
| [guid](#guid)             | INT      | UNSIGNED   | PRI | NO   |         | Unique |                                                                     |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Usar un número **positivo** **añadirá** la creature al evento cuando esté activo.

Usar un número **negativo** **eliminará** la creature del evento cuando esté activo.

### guid

Se refiere a: [creature.guid](creature#guid).
