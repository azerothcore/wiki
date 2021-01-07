# character\_queststatus\_seasonal

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\_seasonal\` table**

Holds information on the seasonal quest (quests with ZoneOrSort of -22) status of every player. The quests reset at the end of the corresponding eventEntry.

**Structure**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|------------|---------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]  | int(10) | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | int(10) | unsigned   | PRI | NO   | 0       |       | Quest Identifier         |
| [event][3] | int(10) | unsigned   |     | NO   | 0       |       | Event Identifier         |

[1]: #guid
[2]: #quest
[3]: #event

**Description of the fields**

### guid

The guid of the character.

### quest

The entry of the quest.

### event

The eventEntry of the game event that the seasonal quest belongs to.
