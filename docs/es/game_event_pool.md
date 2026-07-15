# game_event_pool

[<-Volver a:World](database-world)

**Tabla \`game_event_pool\`**

Esta tabla determina si un pool dado está activo para un evento de juego dado.

**Estructura**

| Field                     | Type      | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| ------------------------- | --------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT  | SIGNED     |     | NO   |         |        | Entry del evento de juego. Pon un entry negativo para eliminar durante el evento. |
| [pool_entry](#pool_entry) | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | Unique | Id del pool                                                         |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Usar un número **positivo** **añadirá** el pool al evento cuando esté activo.

Usar un número **negativo** **eliminará** el pool del evento cuando esté activo.

### pool_entry

Se refiere a: [pool_pool.pool_id](pool_pool#pool_id).
