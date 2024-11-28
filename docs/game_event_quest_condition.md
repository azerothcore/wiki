# game_event_quest_condition

[<-Back-to:World](database-world)

**The \`game_event_quest_condition\` table**

This table contains the mapping of a quest in a world event to the condition that it will fulfill. It also contains how much a given quest will add to a condition once that quest is completed by a player.

**Table Structure**

| Field                        | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry](#evententry)    | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [quest](#quest)              | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [condition_id](#conditionid) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [num](#num)                  | FLOAT     | SIGNED     |     | YES  | 0       |       |         |

**Description of the fields**

### eventEntry

The event that is associated with this quest and condition.

### quest

The quest that will trigger this condition.

### condition_id

The condition that will be triggered on quest complete.

### num

The number of "units" (for lack of a better word) that will be added to the condition to fulfill the required number needed for the condition.
