# gameobject\_respawn

[<-Back-to:Characters](database-characters.md)

**The \`gameobject\_respawn\` table**

This table holds the re-spawn time when game objects should be re spawned in the world. In case of a server crash, this table holds the re-spawn data so that the game objects don't re-spawn immediately on server restart. How often the re-spawn time is saved for game objects can be controlled in trinitycore.conf at SaveRespawnTimeImmediately. Usually the only objects that despawn and need to be re-spawned are chests and doors.

**Structure**

| Field            | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|------------------|---------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]        | INT(10) | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [respawntime][2] | INT(10) | unsigned   |     | NO   | 0       |       |                          |
| [instance][3]    | INT(10) | unsigned   | PRI | NO   | 0       |       | Instance Identifier      |

[1]: #guid
[2]: #respawntime
[3]: #instance

**Description of the fields**

### guid

The GUID of the game object. See gameobject.guid

### respawntime

The time when the game object should be respawned in Unix time.

### instance

If the game object belonged in an instance, this field holds the instance ID where this game object should be respawned. Each instance is different depending on the group so this field is vital in keeping track of which game objects should be respawned for which players at what time.
