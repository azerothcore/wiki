# game_event_quest_condition

[<-Volver a:World](database-world)

**Tabla \`game_event_quest_condition\`**

Esta tabla contiene la correspondencia entre una quest de un evento mundial y la condición que esta cumplirá. También contiene cuánto añade una quest dada a una condición una vez que un jugador completa esa quest.

**Estructura**

| Field                        | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry](#evententry)    | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [quest](#quest)              | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [condition_id](#conditionid) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [num](#num)                  | FLOAT     | SIGNED     |     | YES  | 0       |       |         |

**Descripción de los campos**

### eventEntry

El evento que está asociado con esta quest y condición.

### quest

La quest que activará esta condición.

### condition_id

La condición que se activará al completar la quest.

### num

El número de "unidades" (a falta de una palabra mejor) que se añadirán a la condición para cumplir el número requerido necesario para la condición.
