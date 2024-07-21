# creature\_questender

[<-Back-to:World](database-world)

**The \`creature\_questender\` table**

Holds NPC quest ender relations on which NPCs finishes which quests.

**Table Structure**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier       |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Description of the fields**

### id

The ID of the creature. See [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

The quest ID that the creature finishes. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
