# game_event_creature

[<-Volver a:World](database-world)

**Tabla \`game_event_creature\`**

Contiene todas las instancias de criaturas que deben generarse o desgenerarse durante eventos de juego definidos.

**Estructura**

| Campo                     | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                                                                                    |
| ------------------------- | -------- | --------- | ----- | ---- | ----------- | ------ | --------------------------------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED    |       | NO   |             |        | Entrada del evento del juego. Colocar una entrada negativa para eliminarla durante el evento. |
| [guid](#guid)             | INT      | UNSIGNED  | PRI   | NO   |             | Unique |                                                                                               |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Usar un número **positivo** **agregará** la criatura al evento cuando se esté ejecutando.

Usar un número **negativo** **eliminará** la criatura del evento cuando se esté ejecutando.

### guid

Se refiere a: [creature.guid](creature#guid).
