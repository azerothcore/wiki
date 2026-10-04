# character\_queststatus\_daily

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_daily\` table**

Holds information on the daily quest status of every player. The quest must have type = 87 or the 4096 flag at QuestFlags.

**Table: character\_queststatus\_daily's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment                  |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)   | INT  | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier         |
| [time](#time)   | INT  | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### guid

The character GUID. See [characters.guid](characters#guid).

### quest

The quest ID of the daily quest. See [quest\_template.ID](quest_template#id).

### time

The time when the quest was taken, in Unix time.
