# spawn\_group

[<-Back-to:World](database-world)

**The \`spawn\_group\` table**

This table maps individual creature and gameobject spawns to their spawn groups. Each spawn can belong to one group, which controls its respawn behavior through the flags defined in [spawn\_group\_template](spawn_group_template).

**Table Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnType](#spawntype) | TINYINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnId](#spawnid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [chance](#chance)       | FLOAT   |            |     | NO   | 0       |       | Percent chance the member spawns, 0 = always |

**Description of the fields**

### groupId

This is the Group ID for the group. It must match a group already existing in the [spawn\_group\_template](spawn_group_template) table.

### spawnType

This is the spawn type:

| Value | Type       |
| ----- | ---------- |
| 0     | Creature   |
| 1     | GameObject |

### spawnId

This is the spawn ID (GUID) of the creature or game object that should be included in the group. The ID must exist in the [creature](creature) or [gameobject](gameobject) tables respectively.

### chance

The percent chance (0 to 100) that this member spawns at all. `0` means it always spawns. Use it for packs whose size varies: a pack of four where one member has `chance` 50 is a pack of three half of the time.

The chance is rolled once per map, together with the rest of the group, the first time one of its members spawns. A member whose chance failed stays absent until the map is created again (a new instance, or a server restart for a continent).

A group can also set which entries its members spawn as. See [spawn\_group\_entry](spawn_group_entry).
