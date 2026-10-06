# character\_queststatus\_weekly

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_weekly\` table**

Holds information on the weekly quest status of every player. The timers reset at the same time the Raids reset.

**Table: character\_queststatus\_weekly's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment                  |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)   | INT  | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier         |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### quest

The quest ID of the rewarded quest. See [quest\_template.id](quest_template#id).
