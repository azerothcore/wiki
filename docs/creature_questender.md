# creature\_questender

[<-Back-to:World](database-world)

**The \`creature\_questender\` table**

Holds NPC quest ender relations on which NPCs finishes which quests.

**Table: creature\_questender's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment          |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [id](#id)       | INT  | UNSIGNED | NO   | PRI | 0       |       | Identifier       |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier |

**Description of the table's fields**

### id

The ID of the creature. See [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

The quest ID that the creature finishes. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
