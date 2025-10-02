# game\_event\_condition\_save

[<-Volver a:Characters](database-characters)

**Tabla \`game\_event\_condition\_save\`**

**Estructura**

| Campo             | Tipo    | Atributo  | Llave | Nulo | Por defecto | Extra | Comentario |
| ----------------- | ------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [eventEntry][1]   | TINYINT | UNSIGNED  | PRI   | NO   |             |       |            |
| [condition_id][2] | INT     | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [done][3]         | FLOAT   | SIGNED    |       | SI   | 0           |       |            |

[1]: #evententry
[2]: #conditionid
[3]: #done

**Descripción de los campos**

### eventEntry

Este es un enlace a la entrada del evento en la tabla del game\_event.

### condition\_id

Consulte  [game\_event\_condition.condition\_id](game_event_condition#condition_id).

### done

Indica cuánto se ha hecho. Consulte[game\_event\_condition.req\_num](game_event_condition#req_num).
