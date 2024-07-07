# game\_event\_condition\_save

[<-Back-to:Characters](database-characters)

**The \`game\_event\_condition\_save\` table**

**Table Structure**

| Field             | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry][1]   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [condition_id][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [done][3]         | FLOAT   | SIGNED     |     | YES  | 0       |       |         |

[1]: #evententry
[2]: #conditionid
[3]: #done

**Description of the fields**

### eventEntry

This is a link to the event entry in the game\_event table.

### condition\_id

See [game\_event\_condition.condition\_id](game_event_condition#condition_id).

### done

Indicates how much has been done. See [game\_event\_condition.req\_num](game_event_condition#req_num).
