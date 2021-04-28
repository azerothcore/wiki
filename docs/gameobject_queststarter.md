# gameobject\_queststarter

[<-Back-to:World](database-world.md)

**The \`gameobject\_queststarter\` table**

Holds game object quest giver relations. The game objects in this table should all be of type QUESTGIVER (2).

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment          |
|------------|--------------|------------|-----|------|---------|-------|------------------|
| [id][1]    | MEDIUMINT(8) | UNSIGNED   | PRI | NO   | 0       |       |                  |
| [quest][2] | MEDIUMINT(8) | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Description of the fields**

### id

The template ID of the game object. See [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### quest

The quest ID that this game object starts. See [quest\_template.entry](http://www.azerothcore.org/wiki/quest_template#id)
