# vehicle\_template\_accessory

[<-Back-to:World](database-world.md)

**The \`vehicle\_template\_accessory\` table**

Records in this table can be overwritten by [vehicle\_accessory](vehicle_accessory) table

**Structure**

| Field                | Type         | Attributes | Key | Null | Default | Extra | Comment                                      |
|----------------------|--------------|------------|-----|------|---------|-------|----------------------------------------------|
| [entry][1]           | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       |                                              |
| [accessory_entry][2] | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |                                              |
| [seat_id][3]         | TINYINT(1)   | signed     | PRI | NO   | 0       |       |                                              |
| [minion][4]          | TINYINT(1)   | unsigned   |     | NO   | 0       |       |                                              |
| [description][5]     | text         | signed     |     | NO   |         |       |                                              |
| [summontype][6]      | TINYINT(3)   | unsigned   |     | NO   | 6       |       | see enum TempSummonType                      |
| [summontimer][7]     | int(10)      | unsigned   |     | NO   | 30000   |       | timer, only relevant for certain summontypes |

[1]: #entry
[2]: #accessory_entry
[3]: #seat_id
[4]: #minion
[5]: #description
[6]: #summontype
[7]: #summontimer

**Description of the fields**

### entry

Entry of creature to be used as Vehicle. Entry from [creature_template](creature_template#entry).

### accessory\_entry

Entry from [creature_template](creature_template#entry) to be used as the rider/turret/addon to the main vehicle. ID from creature\_template.

### seat\_id

Vehicle seat in witch the accessory should be spawned. See [VehicleSeat.dbc](VehicleSeat).

### minion

If value is 0 accessory will not die when vehicle dies.
If value is 1 accessory will die when the vehicle dies.

### description

Comment

### summontype

| Flag | Name                                   | Comments                                                            |
|------|----------------------------------------|---------------------------------------------------------------------|
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
