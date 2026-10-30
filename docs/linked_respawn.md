# linked\_respawn

[<-Back-to:World](database-world)

**The \`linked\_respawn\` table**

This table links trash mobs to bosses so that if you kill the boss, the trash do not respawn before the instance is reset.
Gameobjects can be linked too!

**Table: linked\_respawn's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment            |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------- |
| [guid](#guid)             | INT     | UNSIGNED | NO   | PRI |         |       | dependent creature |
| [linkedGuid](#linkedguid) | INT     | UNSIGNED | NO   |     |         |       | master creature    |
| [linkType](#linktype)     | TINYINT | UNSIGNED | NO   | PRI | 0       |       |                    |

**Description of the table's fields**

### guid

This is the guid of the [creature](creature#guid) or [gameobject](gameobject#guid) you want to link.

### linkedGuid

This is the guid of the [creature](creature#guid) or [gameobject](gameobject#guid) (boss most likely) that you want to link to.

### linkType

| Value | Dependent  | Master     |
| ----- | ---------- | ---------- |
| 0     | creature   | creature   |
| 1     | creature   | gameobject |
| 2     | gameobject | gameobject |
| 3     | gameobject | creature   |
