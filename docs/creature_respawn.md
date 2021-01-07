# creature\_respawn

[<-Back-to:Characters](database-characters.md)

**The \`creature\_respawn\` table**

This table holds the respawn time when creatures should be respawned in the world. In case of a server crash, this table holds the respawn data so that the creatures don't respawn immediately on server restart. How often the respawn time is saved for creatures can be controlled in TrinityCore.conf at SaveRespawnTimeImmediately.

**Structure**

| Field            | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|------------------|---------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]        | int(10) | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [respawntime][2] | int(10) | unsigned   |     | NO   | 0       |       |                          |
| [instance][3]    | int(10) | unsigned   | PRI | NO   | 0       |       | Instance Identifier      |

[1]: #guid
[2]: #respawntime
[3]: #instance

**Description of the fields**

### guid

The GUID of the creature. See creature.guid

### respawntime

The time when the creature should be respawned in Unix time.

### instance

If the creature was killed in an instance, this field holds the instance ID where this creature should be respawned. Each instance is different depending on the group so this field is vital in keeping track of which creatures should be respawned for which players at what time.
