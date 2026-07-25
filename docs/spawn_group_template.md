# spawn\_group\_template

[<-Back-to:World](database-world)

**The \`spawn\_group\_template\` table**

This table defines spawn group templates with their names and behavior flags. Spawn groups allow logical grouping of creature and gameobject spawns with per-group control over respawn behavior.

**Table Structure**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)       | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [groupName](#groupname)   | VARCHAR(100) |            |     | NO   | NULL    |       |         |
| [groupFlags](#groupflags) | INT          | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the fields**

### groupId

This is the Group ID for the group. It must be a unique number. Groups 0 and 1 are reserved system groups:

- Group 0: "Default Group" — System group using dynamic respawn by default.
- Group 1: "Legacy Group" — System group using compatibility mode (legacy respawn behavior).

### groupName

This is a descriptive name for the group.

### groupFlags

These are the flags that will apply to the group.

| Flag                                   | Number | Description                                                                                                                                          |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPAWNGROUP\_FLAG\_NONE                 | 0x00   | No flags applied                                                                                                                                     |
| SPAWNGROUP\_FLAG\_SYSTEM               | 0x01   | This group is a system group. System groups cannot be manually spawned or despawned via GM commands.                                                  |
| SPAWNGROUP\_FLAG\_COMPATIBILITY\_MODE  | 0x02   | This group uses legacy respawn behavior: the creature corpse remains on the map until the respawn timer expires, then the creature respawns in place. When this flag is not set, creatures are fully removed on death and recreated fresh by the respawn scheduler. |
| SPAWNGROUP\_FLAG\_MANUAL\_SPAWN        | 0x04   | This group will not be spawned by core by default. Scripts can manually spawn/despawn these groups on demand using SmartAI actions or GM commands.    |
| SPAWNGROUP\_FLAG\_DYNAMIC\_SPAWN\_RATE | 0x08   | This group will have dynamic spawn rates applied (by default quest interested creatures/gos and gather nodes use this)                               |
| SPAWNGROUP\_FLAG\_ESCORTQUESTNPC       | 0x10   | This group contains Escort quest NPCs. This further enhances Dynamic spawn to begin respawn time at the point a quest is taken and the escort begins |

> The `Respawn.ForceCompatibilityMode` worldserver configuration option can force all spawns to use legacy (compatibility mode) behavior regardless of group flags.
