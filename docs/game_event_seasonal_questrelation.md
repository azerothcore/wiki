# game\_event\_seasonal\_questrelation

[<-Back-to:World](database-world.md)

**The \`game\_event\_seasonal\_questrelation\` table**

Holds information on the game event seasonal quest relations to allow for resetting of quests with ZoneOrSort of -22.

**Structure**

| Field           | Type          | Attributes | Key | Null | Default | Extra | Comment                 |
|-----------------|---------------|------------|-----|------|---------|-------|-------------------------|
| [questId][1]    | INT       | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier        |
| [eventEntry][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Entry of the game event |

[1]: #questid
[2]: #evententry

**Description of the fields**

### quest

The id of the quest.

### event

The eventEntry of the game event that the seasonal quest belongs to.
