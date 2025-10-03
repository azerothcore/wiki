# game_event_gameobject

[<-Volver a:World](database-world)

**Tabla \`game_event_gameobject\`**

Contiene todas las instancias de gameobjects que participan en cualquier evento del juego.

**Estructura**

| Campo                     | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                                                                                    |
| ------------------------- | -------- | --------- | ----- | ---- | ----------- | ------ | --------------------------------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED    |       | NO   |             |        | Entrada del evento del juego. Colocar una entrada negativa para eliminarla durante el evento. |
| [guid](#guid)             | INT      | UNSIGNED  | PRI   | NO   |             | Unique |                                                                                               |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

El uso de un número **positivo** **agregará** el objeto al evento cuando se esté ejecutando.

El uso de un número **negativo** **eliminará** el objeto del evento cuando se esté ejecutando.

### guid

Se refiere a: [gameobject.guid](gameobject#guid).
