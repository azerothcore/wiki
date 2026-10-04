# game\_event\_quest\_condition

[<-Back-to:World](database-world)

**The \`game\_event\_quest\_condition\` table**

This table contains the mapping of a quest in a world event to the condition that it will fulfill. It also contains how much a given quest will add to a condition once that quest is completed by a player.

**Table: game\_event\_quest\_condition's Structure**

| Field                        | Type    |          | Null | Key | Default | Extra | Comment                  |
| :--------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [eventEntry](#evententry)    | TINYINT | UNSIGNED | NO   |     |         |       | Entry of the game event. |
| [quest](#quest)              | INT     | UNSIGNED | NO   | PRI | 0       |       |                          |
| [condition_id](#conditionid) | INT     | UNSIGNED | NO   |     | 0       |       |                          |
| [num](#num)                  | FLOAT   |          | YES  |     | 0       |       |                          |

**Description of the table's fields**

### eventEntry

The event that is associated with this quest and condition.

### quest

The quest that will trigger this condition.

### condition_id

The condition that will be triggered on quest complete.

### num

The number of "units" (for lack of a better word) that will be added to the condition to fulfill the required number needed for the condition.
