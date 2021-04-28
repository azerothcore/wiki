# game\_event\_quest\_condition

[<-Back-to:World](database-world.md)

**The \`game\_event\_quest\_condition\` table**

This table contains the mapping of a quest in a world event to the condition that it will fulfill. It also contains how much a given quest will add to a condition once that quest is completed by a player.

**Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------------|--------------|------------|-----|------|---------|-------|---------|
| [eventEntry][1]   | tinyint(3)   | unsigned   |     | NO   |         |       |         |
| [quest][2]        | mediumint(8) | unsigned   | PRI | NO   | 0       |       |         |
| [condition_id][3] | mediumint(8) | unsigned   |     | NO   | 0       |       |         |
| [num][4]          | FLOAT        | signed     |     | YES  | 0       |       |         |

[1]: #evententry
[2]: #quest
[3]: #condition_id
[4]: #num

**Description of the fields**

### eventEntry

The event that is associated with this quest and condition.

### quest

The quest that will trigger this condition.

### condition\_id

The condition that will be triggered on quest complete.

### num

The number of "units" (for lack of a better word) that will be added to the condition to fulfill the required number needed for the condition.
