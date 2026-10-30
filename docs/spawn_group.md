# spawn\_group

[<-Back-to:World](database-world)

**The \`spawn\_group\` table**

This table maps individual creature and gameobject spawns to their spawn groups. Each spawn can belong to one group, which controls its respawn behavior through the flags defined in [spawn\_group\_template](spawn_group_template).

**Table: spawn\_group's Structure**

| Field                   | Type    |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [groupId](#groupid)     | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [spawnType](#spawntype) | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [spawnId](#spawnid)     | INT     | UNSIGNED | NO   | PRI |         |       |         |

**Description of the table's fields**

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
