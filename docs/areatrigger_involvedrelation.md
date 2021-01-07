# areatrigger\_involvedrelation

[<-Back-to:World](database-world.md)

**The \`areatrigger\_involvedrelation\` table**

Enable a trigger to finish one condition of a quest (explore)

If there is a record in the table for a quest, then the quest will not be completed until the player activates this areatriger. The quest is not necessarily finished after that, but that one condition of the quest is satisfied. If the only condition of the quest is to explore an area, then the quest will be complete.

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comments         |
|------------|--------------|------------|-----|------|---------|-------|------------------|
| [id][1]    | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Identifier       |
| [quest][2] | mediumint(8) | unsigned   |     | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Description of the fields**

### id

This is the trigger ID from [AreaTrigger.dbc](DBC-AreaTrigger)

### quest

This is the quest id that the trigger is tied to.
