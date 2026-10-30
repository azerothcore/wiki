# character\_queststatus\_rewarded

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_rewarded\` table**

This table holds information of **every** rewarded quest to a player.

**Table: character\_queststatus\_rewarded's Structure**

| Field             | Type    |          | Null | Key | Default | Extra | Comment                  |
| :---------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)     | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [quest](#quest)   | INT     | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier         |
| [active](#active) | TINYINT | UNSIGNED | NO   |     | 1       |       |                          |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### quest

The quest ID of the rewarded quest. See [quest\_template.id](quest_template#id).

### active

Always set to 1. Used internally to filter active rewarded quests when loading character data.
