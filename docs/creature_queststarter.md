# creature\_queststarter

[<-Back-to:World](database-world.md)

**The \`creature\_queststarter\` table**

Holds NPC quest giver relations on which NPCs start which quests.

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment          |
|------------|--------------|------------|-----|------|---------|-------|------------------|
| [id][1]    | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Identifier       |
| [quest][2] | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Description of the fields**

### id

The ID of the creature. See [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

The quest ID that the creature starts. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
