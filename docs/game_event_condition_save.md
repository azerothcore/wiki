# game\_event\_condition\_save

[<-Back-to:Characters](database-characters)

**The \`game\_event\_condition\_save\` table**

Stores the saved progress of game event conditions.

**Table: game\_event\_condition\_save's Structure**

| Field                        | Type    |          | Null | Key | Default | Extra | Comment |
| :--------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [eventEntry](#evententry)    | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [condition_id](#conditionid) | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [done](#done)                | FLOAT   |          | YES  |     | 0       |       |         |

**Description of the table's fields**

### eventEntry

This is a link to the event entry in the game\_event table.

### condition\_id

See [game\_event\_condition.condition\_id](game_event_condition#conditionid).

### done

Indicates how much has been done. See [game\_event\_condition.req\_num](game_event_condition#reqnum).
