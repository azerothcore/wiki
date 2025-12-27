# game_event_condition

[<-Back-to:World](database-world)

**The \`game_event_condition\` table**

This table contains conditions to meet for the specified game event to be completed. Also contains the world state fields used for reporting the given conditions progress and/or max required value. This table will do absolutely nothing if you have not set the event to be a world event.

**Table Structure**

| Field                                          | Type        | Attributes | Key | Null | Default | Extra | Comment                 |
| ---------------------------------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ----------------------- |
| [eventEntry](#evententry)                      | TINYINT     | UNSIGNED   | PRI | NO   |         |       | Entry of the game event |
| [condition_id](#conditionid)                   | MEDIUMINT   | UNSIGNED   | PRI | NO   |         |       |                         |
| [req_num](#reqnum)                             | FLOAT       | SIGNED     |     | YES  | 0       |       |                         |
| [max_world_state_field](#maxworldstatefield)   | SMALLINT    | UNSIGNED   |     | NO   |         |       |                         |
| [done_world_state_field](#doneworldstatefield) | SMALLINT    | UNSIGNED   |     | NO   |         |       |                         |
| [description](#description)                    | VARCHAR(25) | SIGNED     |     | NO   |         |       |                         |

**Description of the fields**

### eventEntry

This is a link to the event entry in the [game_event](#game_event#evententry) table.

### condition_id

This is the condition ID for this particular world event condition. It is an arbitrary number, and you can have multiple conditions for each world event. It links to the condition_id field of the [game_event_quest_condition](#conditionid) table.

### req_num

This is an arbitrary value that determines when this condition is met. For example, if you set this value to 1000, and there is only one quest in [game_event_quest_condition](#conditionid) that will fulfill this condition, and it increases this condition by 100 (by setting the num field to 100), then you would need to have your players complete 10 of that quest to fulfill this condition.

### max_world_state_field

This is the world state update field number sent to the client that is used to report the maximum number of needed points in order to satisfy this condition. It can be found in gossip texts referenced with $XXXXw where XXXX is the world state number that will be sent when that gossip is displayed. If you are doing a custom event, you can pick any number you want that isn't in use, it just needs to match the custom text that you put into the [npc_text](npc_text) table.

### done_world_state_field

This is the world state update field number sent to the client that is used to report the number of accumulated points so far for this condition. It can be found in gossip texts referenced with $XXXXw where XXXX is the world state number that will be sent when that gossip is displayed. If you are doing a custom event, you can pick any number you want that isn't in use, it just needs to match the custom text that you put into the [npc_text](npc_text) table.

### description

Arbitrary text field describing this condition.
