# linked\_respawn

[<-Back-to:World](database-world.md)

**The \`linked\_respawn\` table**

This table links trash mobs to bosses so that if you kill the boss, the trash do not respawn before the instance is reset.
Gameobjects can be linked too!

**Structure**

| Field           | Type       | Attributes | Key | Null | Default | Extra | Comment            |
|-----------------|------------|------------|-----|------|---------|-------|--------------------|
| [guid][1]       | INT    | UNSIGNED   | PRI | NO   |         |       | Dependent Creature |
| [linkedGuid][2] | INT    | UNSIGNED   |     | NO   |         |       | Master Creature    |
| [linkType][3]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |                    |

[1]: #guid
[2]: #linkedguid
[3]: #linktype

**Description of the fields**

### guid

This is the guid of the [creature](http://www.azerothcore.org/wiki/creature#guid) or [gameobject](http://www.azerothcore.org/wiki/gameobject#guid) you want to link.

### linkedGuid

This is the guid of the [creature](http://www.azerothcore.org/wiki/creature#guid) or [gameobject](http://www.azerothcore.org/wiki/gameobject#guid) (boss most likely) that you want to link to.

### linkedType

| Value | Dependent  | Master     |
|-------|------------|------------|
| 0     | creature   | creature   |
| 1     | creature   | gameobject |
| 2     | gameobject | gameobject |
| 3     | gameobject | creature   |
