# character\_queststatus\_seasonal

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_seasonal\` table**

Holds information on the seasonal quest (quests with ZoneOrSort of -22) status of every player. The quests reset at the end of the corresponding eventEntry.

**Table: character\_queststatus\_seasonal's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment                  |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)   | INT  | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier         |
| [event](#event) | INT  | UNSIGNED | NO   |     | 0       |       | Event Identifier         |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### quest

The quest ID of the rewarded quest. See [quest\_template.id](quest_template#id).

### event

The eventEntry of the game event that the seasonal quest belongs to.
