# game_event_gameobject

[<-Volver a:World](database-world)

**Tabla \`game_event_gameobject\`**

Contiene todas las instancias de gameobject que participan en algún evento de juego.

**Estructura**

| Field                     | Type     | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| ------------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED     |     | NO   |         |        | Entry del evento de juego. Pon un entry negativo para eliminar durante el evento. |
| [guid](#guid)             | INT      | UNSIGNED   | PRI | NO   |         | Unique |                                                                     |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Usar un número **positivo** **añadirá** el objeto al evento cuando esté activo.

Usar un número **negativo** **eliminará** el objeto del evento cuando esté activo.

### guid

Se refiere a: [gameobject.guid](gameobject#guid).
