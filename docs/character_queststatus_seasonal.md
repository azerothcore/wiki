# character\_queststatus\_seasonal

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_seasonal\` table**

Holds information on the seasonal quest (quests with ZoneOrSort of -22) status of every player. The quests reset at the end of the corresponding eventEntry.

**Table Structure**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | INT     | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [event][3] | INT     | UNSIGNED   |     | NO   | 0       |       | Event Identifier         |

[1]: #guid
[2]: #quest
[3]: #event

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### quest

The quest ID of the rewarded quest. See [quest\_template.id](quest_template#id).

### event

The eventEntry of the game event that the seasonal quest belongs to.
