# creature\_respawn

[<-Back-to:Characters](database-characters)

**The \`creature\_respawn\` table**

This table holds the respawn time when creatures should be respawned in the world. In case of a server crash, this table holds the respawn data so that the creatures don't respawn immediately on server restart. How often the respawn time is saved for creatures can be controlled in [worldserver.conf.dist](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist) at SaveRespawnTimeImmediately.

**Table: creature\_respawn's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment                  |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [respawnTime](#respawntime) | INT      | UNSIGNED | NO   |     | 0       |       |                          |
| [mapId](#mapid)             | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [instanceId](#instanceid)   | INT      | UNSIGNED | NO   | PRI | 0       |       | Instance Identifier      |

**Description of the table's fields**

### guid

The GUID of the creature spawn. See [creature.guid](creature#guid).

### respawnTime

The time when the creature should be respawned in Unix time.

### mapId

The map ID where this creature respawn entry applies.

### instanceId

If the creature was killed in an instance, this field holds the instance ID where this creature should be respawned. Each instance is different depending on the group so this field is vital in keeping track of which creatures should be respawned for which players at what time.
