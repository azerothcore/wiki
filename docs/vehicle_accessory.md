# vehicle\_accessory

[<-Back-to:World](database-world)

**The \`vehicle\_accessory\` table**

This table is used to tell the server to spawn an additional NPC with this vehicle.

**Table Structure**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                                      |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------- |
| [guid][1]            | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                                              |
| [accessory_entry][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |                                              |
| [seat_id][3]         | TINYINT   | SIGNED     | PRI | NO   | 0       |       |                                              |
| [minion][4]          | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                                              |
| [description][5]     | text      | SIGNED     |     | NO   | "       |       |                                              |
| [summontype][6]      | TINYINT   | UNSIGNED   |     | NO   | 6       |       | see enum TempSummonType                      |
| [summontimer][7]     | INT       | UNSIGNED   |     | NO   | 30000   |       | timer, only relevant for certain summontypes |

[1]: #guid
[2]: #accessory_entry
[3]: #seat_id
[4]: #minion
[5]: #description
[6]: #summontype
[7]: #summontimer

**Description of the fields**

### guid

Guid of creature to be used as Vehicle, to be obtained from [creature](creature) table.

### accessory\_entry

Entry from creature\_template to be used as the rider/turret/addon to the main vehicle. ID from creature\_template.
Flying vehicles must have InhabitType set to (4 - Flying).

### seat\_id

Vehicle seat in witch the accessory should be spawned. See [VehicleSeat.dbc](VehicleSeat)

### minion

If value is 0 accessory will not die when vehicle dies.
If value is 1 accessory will die when the vehicle dies.

Note: When making detachable vehicles you will always want to use value 0, otherwise when the main vehicle dies so does the detached vehicles.

### description

Comment

### summontype

| Flag | Name                                   | Comments                                                            |
| ---- | -------------------------------------- | ------------------------------------------------------------------- |
| 1    | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | Despawns after a specified time OR when the creature disappears     |
| 2    | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | Despawns after a specified time OR when the creature dies           |
| 3    | TEMPSUMMON_TIMED_DESPAWN               | Despawns after a specified time                                     |
| 4    | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | Despawns after a specified time after the creature is out of combat |
| 5    | TEMPSUMMON_CORPSE_DESPAWN              | Despawns instantly after death                                      |
| 6    | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | Despawns after a specified time after death                         |
| 7    | TEMPSUMMON_DEAD_DESPAWN                | Despawns when the creature disappears                               |
| 8    | TEMPSUMMON_MANUAL_DESPAWN              | Despawns when UnSummon() is called                                  |

### summontimer

Timer linked to summontype
