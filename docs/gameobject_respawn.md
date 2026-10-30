# gameobject\_respawn

[<-Back-to:Characters](database-characters)

**The \`gameobject\_respawn\` table**

This table holds the re-spawn time when game objects should be re spawned in the world. In case of a server crash, this table holds the re-spawn data so that the game objects don't re-spawn immediately on server restart. How often the re-spawn time is saved for game objects can be controlled in trinitycore.conf at SaveRespawnTimeImmediately. Usually the only objects that despawn and need to be re-spawned are chests and doors.

**Table: gameobject\_respawn's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment                  |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [respawnTime](#respawntime) | INT      | UNSIGNED | NO   |     | 0       |       |                          |
| [mapId](#mapid)             | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [instanceId](#instanceid)   | INT      | UNSIGNED | NO   | PRI | 0       |       | Instance Identifier      |

**Description of the table's fields**

### guid

The GUID of the game object. See [gameobject.guid](gameobject#guid).

### respawnTime

The time when the game object should be respawned in Unix time.

### mapid

The map ID where this gameobject respawn entry applies.

### instanceId

If the game object belonged in an instance, this field holds the instance ID where this game object should be respawned. Each instance is different depending on the group so this field is vital in keeping track of which game objects should be respawned for which players at what time.
