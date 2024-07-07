# spawn\_group\_template

[<-Back-to:World](database-world)

**The \`spawn\_group\_template\` table**

This table contains Spawn Group names and flags.

**Table Structure**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [roupId][1]    | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [roupName][2]  | VARCHAR(100) |            |     | NO   | NULL    |       |         |
| [roupFlags][3] | INT          | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #roupid
[2]: #roupname
[3]: #roupflags

**Description of the fields**

### groupId

This is the Group ID for the group. It must be a unique number. Groups 0-4 are reserved for system tasks.

### groupName

This is a descriptive name for the group.

### groupFlags

These are the flags that will apply to the group.

| Flag                                   | Number | Description                                                                                                                                          |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPAWNGROUP\_FLAG\_NONE                 | 0x00   | No flags applied                                                                                                                                     |
| SPAWNGROUP\_FLAG\_SYSTEM               | 0x01   | This group is a system group (applies to standard groups 0-4)                                                                                        |
| SPAWNGROUP\_FLAG\_COMPATIBILITY\_MODE  | 0x02   | This group will contain legacy objects/creatures that don't work with dynamic spawn changes                                                          |
| SPAWNGROUP\_FLAG\_MANUAL\_SPAWN        | 0x04   | This group will not be spawned by core by default. Scripts can manually spawn/despawn these groups on demand.                                        |
| SPAWNGROUP\_FLAG\_DYNAMIC\_SPAWN\_RATE | 0x08   | This group will have dynamic spawn rates applied (by default quest interested creatures/gos and gather nodes use this)                               |
| SPAWNGROUP\_FLAG\_ESCORTQUESTNPC       | 0x10   | This group contains Escort quest NPCs. This further enhances Dynamic spawn to begin respawn time at the point a quest is taken and the escort begins |
