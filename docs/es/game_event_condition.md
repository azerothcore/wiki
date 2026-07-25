# game_event_condition

[<-Volver a:World](database-world)

**Tabla \`game_event_condition\`**

Esta tabla contiene las condiciones que se deben cumplir para que el evento de juego indicado se complete. También contiene los campos de world state usados para informar del progreso de las condiciones y/o del valor máximo requerido. Esta tabla no hará absolutamente nada si no has marcado el evento como evento mundial.

**Estructura**

| Field                                          | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------------------------------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [eventEntry](#evententry)                      | TINYINT     | UNSIGNED   | PRI | NO   |         |       | Entry del evento de juego |
| [condition_id](#conditionid)                   | MEDIUMINT   | UNSIGNED   | PRI | NO   |         |       |                          |
| [req_num](#reqnum)                             | FLOAT       | SIGNED     |     | YES  | 0       |       |                          |
| [max_world_state_field](#maxworldstatefield)   | SMALLINT    | UNSIGNED   |     | NO   |         |       |                          |
| [done_world_state_field](#doneworldstatefield) | SMALLINT    | UNSIGNED   |     | NO   |         |       |                          |
| [description](#description)                    | VARCHAR(25) | SIGNED     |     | NO   |         |       |                          |

**Descripción de los campos**

### eventEntry

Este es un enlace al entry del evento en la tabla [game_event](#game_event#evententry).

### condition_id

Este es el ID de condición para esta condición concreta de evento mundial. Es un número arbitrario, y puedes tener varias condiciones para cada evento mundial. Enlaza con el campo condition_id de la tabla [game_event_quest_condition](#conditionid).

### req_num

Este es un valor arbitrario que determina cuándo se cumple esta condición. Por ejemplo, si fijas este valor en 1000, y solo hay una quest en [game_event_quest_condition](#conditionid) que cumple esta condición, y esta incrementa la condición en 100 (fijando el campo num a 100), entonces necesitarías que tus jugadores completaran 10 veces esa quest para cumplir la condición.

### max_world_state_field

Este es el número de campo de actualización de world state enviado al cliente que se usa para informar del número máximo de puntos necesarios para satisfacer esta condición. Se puede encontrar en los textos de gossip referenciados con $XXXXw donde XXXX es el número de world state que se enviará cuando ese gossip se muestre. Si estás haciendo un evento personalizado, puedes elegir cualquier número que no esté en uso; solo tiene que coincidir con el texto personalizado que pongas en la tabla [npc_text](npc_text).

### done_world_state_field

Este es el número de campo de actualización de world state enviado al cliente que se usa para informar del número de puntos acumulados hasta ahora para esta condición. Se puede encontrar en los textos de gossip referenciados con $XXXXw donde XXXX es el número de world state que se enviará cuando ese gossip se muestre. Si estás haciendo un evento personalizado, puedes elegir cualquier número que no esté en uso; solo tiene que coincidir con el texto personalizado que pongas en la tabla [npc_text](npc_text).

### description

Campo de texto arbitrario que describe esta condición.
