# game_event_condition

[<-Volver a:World](database-world)

**Tabla \`game_event_condition\`**

Esta tabla contiene las condiciones que se deben cumplir para completar el evento de juego especificado. También contiene los campos de estado mundial que se utilizan para informar el progreso de las condiciones dadas y/o el valor máximo requerido. Esta tabla no tendrá ninguna función si no se ha configurado el evento como mundial.

**Estructura**

| Campo                                          | Tipo        | Atributo | Llave | Nulo | Por defecto | Extra | Comentario                   |
| ---------------------------------------------- | ----------- | -------- | ----- | ---- | ----------- | ----- | ---------------------------- |
| [eventEntry](#evententry)                      | TINYINT     | UNSIGNED | PRI   | NO   |             |       | Entrada del evento del juego |
| [condition_id](#conditionid)                   | MEDIUMINT   | UNSIGNED | PRI   | NO   |             |       |                              |
| [req_num](#reqnum)                             | FLOAT       | SIGNED   |       | SI   | 0           |       |                              |
| [max_world_state_field](#maxworldstatefield)   | SMALLINT    | UNSIGNED |       | NO   |             |       |                              |
| [done_world_state_field](#doneworldstatefield) | SMALLINT    | UNSIGNED |       | NO   |             |       |                              |
| [description](#description)                    | VARCHAR(25) | SIGNED   |       | NO   |             |       |                              |

**Descripción de los campos**

### eventEntry

Este es un enlace a la entrada del evento en la tabla [game_event](#game_event#evententry).

### condition_id

Este es el ID de condición para esta condición de evento mundial en particular. Es un número arbitrario y se pueden tener varias condiciones para cada evento mundial. Se vincula al campo condition_id de la tabla [game_event_quest_condition](#conditionid).

### req_num

Este valor es arbitrario y determina cuándo se cumple esta condición. Por ejemplo, si estableces este valor en 1000 y solo hay una misión en [game_event_quest_condition](#conditionid) que cumple esta condición, y la aumentas en 100 (estableciendo el campo num en 100), tus jugadores deberán completar 10 misiones de esa misión para cumplirla.

### max_world_state_field

Este es el número del campo de actualización del estado mundial que se envía al cliente y que se utiliza para informar la cantidad máxima de puntos necesarios para cumplir esta condición. Se puede encontrar en los textos de chismes referenciados con $XXXXw, donde XXXX es el número del estado mundial que se enviará al mostrarse el chisme. Si está creando un evento personalizado, puede elegir cualquier número que no esté en uso; solo debe coincidir con el texto personalizado que introdujo en la tabla [npc_text](npc_text).

### done_world_state_field

Este es el número del campo de actualización del estado mundial que se envía al cliente y que se utiliza para informar la cantidad de puntos acumulados hasta el momento para esta condición. Se puede encontrar en los textos de chismes referenciados con $XXXXw, donde XXXX es el número del estado mundial que se enviará al mostrarse dicho chisme. Si está creando un evento personalizado, puede elegir cualquier número que no esté en uso; solo debe coincidir con el texto personalizado que introdujo en la tabla [npc_text](npc_text).

### description

Campo de texto arbitrario que describe esta condición.
