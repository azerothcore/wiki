# creature\_queststarter

[<-Back-to:World](database-world)

**The \`creature\_queststarter\` table**

Holds NPC quest giver relations on which NPCs start which quests.

**Table: creature\_queststarter's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment          |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [id](#id)       | INT  | UNSIGNED | NO   | PRI | 0       |       | Identifier       |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier |

**Description of the table's fields**

### id

The ID of the creature. See [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

The quest ID that the creature starts. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
