# creature\_respawn

[<-Back-to:Characters](database-characters)

**The \`creature\_respawn\` table**

This table holds the respawn time when creatures should be respawned in the world. In case of a server crash, this table holds the respawn data so that the creatures don't respawn immediately on server restart. How often the respawn time is saved for creatures can be controlled in worldserver.conf.dist at SaveRespawnTimeImmediately.

**Table Structure**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [respawnTime][2] | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mapId][3]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [instanceId][4]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | Instance Identifier      |

[1]: #guid
[2]: #respawntime
[3]: #mapid
[4]: #instance

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### respawnTime

The time when the creature should be respawned in Unix time.

### mapId

`field-no-description|3`

### instance

If the creature was killed in an instance, this field holds the instance ID where this creature should be respawned. Each instance is different depending on the group so this field is vital in keeping track of which creatures should be respawned for which players at what time.
