# vehicle\_accessory

[<-Volver a:World](database-world)

**Tabla \`vehicle\_accessory\`**

Esta tabla se usa para indicarle al servidor que haga aparecer un NPC adicional con este vehículo.

**Estructura**

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

**Descripción de los campos**

### guid

Guid de la creature a usar como vehículo, obtenido de la tabla [creature](creature).

### accessory\_entry

Entry de creature\_template a usar como jinete/torreta/complemento del vehículo principal. ID de creature\_template.
Los vehículos voladores deben tener InhabitType fijado a (4 - Flying).

### seat\_id

Asiento del vehículo en el que debe aparecer el accesorio. Ver [VehicleSeat.dbc](vehicleseat)

### minion

Si el valor es 0, el accesorio no morirá cuando muera el vehículo.
Si el valor es 1, el accesorio morirá cuando muera el vehículo.

Nota: Al crear vehículos desmontables siempre querrás usar el valor 0, de lo contrario, cuando muera el vehículo principal, también morirán los vehículos desmontados.

### description

Comentario

### summontype

| Flag | Name                                   | Comments                                                            |
| ---- | -------------------------------------- | ------------------------------------------------------------------- |
| 1    | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | Desaparece tras un tiempo especificado O cuando la creature desaparece |
| 2    | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | Desaparece tras un tiempo especificado O cuando la creature muere   |
| 3    | TEMPSUMMON_TIMED_DESPAWN               | Desaparece tras un tiempo especificado                              |
| 4    | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | Desaparece tras un tiempo especificado después de que la creature esté fuera de combate |
| 5    | TEMPSUMMON_CORPSE_DESPAWN              | Desaparece al instante tras la muerte                               |
| 6    | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | Desaparece tras un tiempo especificado después de la muerte         |
| 7    | TEMPSUMMON_DEAD_DESPAWN                | Desaparece cuando la creature desaparece                            |
| 8    | TEMPSUMMON_MANUAL_DESPAWN              | Desaparece cuando se llama a UnSummon()                             |

### summontimer

Temporizador ligado a summontype
