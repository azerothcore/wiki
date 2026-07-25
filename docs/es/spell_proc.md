# spell\_proc

[<-Volver a: World](database-world)

**Tabla \`spell\_proc\`**

Esta tabla contiene información sobre en qué eventos (o procs) se activan ciertos hechizos. Todos los hechizos de esta tabla deben aplicar un aura SPELL\_AURA\_PROC\_TRIGGER\_SPELL (42). Cualquier entrada de esta tabla sobrescribirá la configuración de proc existente en la entrada DBC del hechizo.

**Estructura**

| Field                 | Type     | Attributes | Key | Null | Default | Extra  | Comment |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ------- |
| [SpellId][1]          | INT      | SIGNED     | PRI | NO   | 0       | Unique |         |
| [SchoolMask][2]       | TINYINT  | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyName][3]  | SMALLINT | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask0][4] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask1][5] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask2][6] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [ProcFlags][7]        | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellTypeMask][8]    | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellPhaseMask][9]   | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [HitMask][10]         | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [AttributesMask][11]     | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [DisableEffectsMask][12] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [ProcsPerMinute][13]     | FLOAT    |            |     | NO   | 0       |        |         |
| [Chance][14]             | FLOAT    |            |     | NO   | 0       |        |         |
| [Cooldown][15]           | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [Charges][16]            | TINYINT  | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #spellid
[2]: #schoolmask
[3]: #spellfamilyname
[4]: #spellfamilymask0
[5]: #spellfamilymask1
[6]: #spellfamilymask2
[7]: #procflags
[8]: #spelltypemask
[9]: #spellphasemask
[10]: #hitmask
[11]: #attributesmask
[12]: #disableeffectsmask
[13]: #procsperminute
[14]: #chance
[15]: #cooldown
[16]: #charges

**Descripción de los campos**

### SpellId

El ID del hechizo que es capaz de procear en un evento. (Puede usarse un spellId negativo para hechizos con rango)

### SchoolMask

Este campo contiene un bitmask que controla sobre qué tipos de hechizos puede activarse el proc. Por ejemplo, si un aura procea solo cuando la unidad sobre la que se lanza es impactada por hechizos de sombra (hechizo 34914). Para combinar escuelas de hechizo, simplemente suma los valores de bit.

| School ID | Bit | Name     |
| --------- | --- | -------- |
| 0         | 1   | Physical |
| 1         | 2   | Holy     |
| 2         | 4   | Fire     |
| 3         | 8   | Nature   |
| 4         | 16  | Frost    |
| 5         | 32  | Shadow   |
| 6         | 64  | Arcane   |

### SpellFamilyName

Este campo controla qué hechizos de un family name pueden procear el hechizo activado.

| ID  | Family Name  |
| --- | ------------ |
| 0   | Generic      |
| 3   | Mage         |
| 4   | Warrior      |
| 5   | Warlock      |
| 6   | Priest       |
| 7   | Druid        |
| 8   | Rogue        |
| 9   | Hunter       |
| 10  | Paladin      |
| 11  | Shaman       |
| 13  | Potion       |
| 15  | Death Knight |
| 53  | Monk         |
| 107 | Demon Hunter |

### SpellFamilyMask0

Este campo controla qué family flags de hechizos pueden procear el hechizo activado.

### SpellFamilyMask1

`campo-sin-descripción|5`

### SpellFamilyMask2

`campo-sin-descripción|6`

### ProcFlags

Si es distinto de cero, se usa para sobrescribir los ProcFlags originales del hechizo en el DBC.

Un bitmask que controla qué eventos activan el hechizo. Para combinar los eventos posibles, suma los bits de proc.

**Ejemplo:** 32+64=96 (PROC\_FLAG\_TAKEN\_MELEE\_SPELL\_HIT + PROC\_FLAG\_SUCCESSFUL\_RANGED\_HIT)

| Event                                   | Flag     | Bit value  | Comment                                                      |
| --------------------------------------- | -------- | ---------- | ------------------------------------------------------------ |
| PROC_FLAG_NONE                          | 0        | 0x00000000 |                                                              |
| PROC_FLAG_KILLED                        | 1        | 0x00000001 | Matado por el agresor                                        |
| PROC_FLAG_KILL_AND_GET_XP               | 2        | 0x00000002 | Muerte que otorga experiencia u honor                        |
| PROC_FLAG_SUCCESSFUL_MELEE_HIT          | 4        | 0x00000004 | Ataque cuerpo a cuerpo impactado con éxito                   |
| PROC_FLAG_TAKEN_MELEE_HIT               | 8        | 0x00000008 | Daño recibido de un impacto cuerpo a cuerpo                  |
| PROC_FLAG_SUCCESSFUL_MELEE_SPELL_HIT    | 16       | 0x00000010 | Ataque exitoso de hechizos que usan un arma cuerpo a cuerpo  |
| PROC_FLAG_TAKEN_MELEE_SPELL_HIT         | 32       | 0x00000020 | Daño recibido de hechizos que usan un arma cuerpo a cuerpo   |
| PROC_FLAG_SUCCESSFUL_RANGED_HIT         | 64       | 0x00000040 | Ataque a distancia impactado con éxito                       |
| PROC_FLAG_TAKEN_RANGED_HIT              | 128      | 0x00000080 | Daño recibido de un impacto de ataque a distancia            |
| PROC_FLAG_SUCCESSFUL_RANGED_SPELL_HIT   | 256      | 0x00000100 | Ataque a distancia exitoso de hechizos que usan un arma a distancia |
| PROC_FLAG_TAKEN_RANGED_SPELL_HIT        | 512      | 0x00000200 | Daño recibido de hechizos que usan un arma a distancia       |
| PROC_FLAG_SUCCESSFUL_POSITIVE_AOE_HIT   | 1024     | 0x00000400 | Hechizo de área impactado con éxito (no 100% seguro de si no se usa) |
| PROC_FLAG_TAKEN_POSITIVE_AOE            | 2048     | 0x00000800 | Hechizo de área positivo recibido (no 100% seguro de si no se usa) |
| PROC_FLAG_SUCCESSFUL_AOE_SPELL_HIT      | 4096     | 0x00001000 | Hechizo de daño en área impactado con éxito (no 100% seguro de si no se usa) |
| PROC_FLAG_TAKEN_AOE_SPELL_HIT           | 8192     | 0x00002000 | Hechizo de daño en área recibido (no 100% seguro de si no se usa) |
| PROC_FLAG_SUCCESSFUL_POSITIVE_SPELL     | 16384    | 0x00004000 | Hechizo positivo lanzado con éxito (por defecto solo en curación) |
| PROC_FLAG_TAKEN_POSITIVE_SPELL          | 32768    | 0x00008000 | Hechizo positivo recibido (por defecto solo en curación)     |
| PROC_FLAG_SUCCESSFUL_NEGATIVE_SPELL_HIT | 65536    | 0x00010000 | Hechizo negativo lanzado con éxito (por defecto solo en daño) |
| PROC_FLAG_TAKEN_NEGATIVE_SPELL_HIT      | 131072   | 0x00020000 | Hechizo negativo recibido (por defecto solo en daño)         |
| PROC_FLAG_DONE_PERIODIC                 | 262144   | 0x00040000 | Daño / curación periódica hecha, determinado por los flags 14-17 |
| PROC_FLAG_TAKEN_PERIODIC                | 524288   | 0x00080000 | Daño / curación periódica recibida, determinado por los flags 14-17 |
| PROC_FLAG_TAKEN_ANY_DAMAGE              | 1048576  | 0x00100000 | Cualquier daño recibido                                      |
| PROC_FLAG_ON_TRAP_ACTIVATION            | 2097152  | 0x00200000 | Al activar una trampa                                        |
| PROC_FLAG_TAKEN_OFFHAND_HIT             | 4194304  | 0x00400000 | Ataques cuerpo a cuerpo de mano secundaria recibidos (sin usar) |
| PROC_FLAG_SUCCESSFUL_OFFHAND_HIT        | 8388608  | 0x00800000 | Ataques cuerpo a cuerpo de mano secundaria exitosos          |
| PROC_FLAG_DEATH                         | 16777216 | 0x01000000 | Muerto de cualquier forma                                    |

### SpellTypeMask

Se usa para elegir qué tipos de hechizos pueden activar el proc; para combinar, simplemente suma los valores de bit.

| Event                       | Flag | Bit        | Comment              |
| --------------------------- | ---- | ---------- | -------------------- |
| PROC_SPELL_TYPE_NONE        | 0    | 0x00000000 |                      |
| PROC_SPELL_TYPE_DAMAGE      | 1    | 0x00000001 | solo hechizos de daño |
| PROC_SPELL_TYPE_HEAL        | 2    | 0x00000002 | solo hechizos de curación |
| PROC_SPELL_TYPE_NO_DMG_HEAL | 4    | 0x00000004 | todos los demás hechizos |
| PROC_SPELL_TYPE_MASK_ALL    | 7    | 0x00000007 | Todas las máscaras combinadas |

### SpellPhaseMask

En qué fase puede el hechizo activar el proc. Normalmente se usa una de ellas a la vez, pero también pueden combinarse.

| Event                     | Flag | Bit        | Comment                                                     |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------- |
| PROC_SPELL_PHASE_NONE     | 0    | 0x00000000 |                                                             |
| PROC_SPELL_PHASE_CAST     | 1    | 0x00000001 | se activa cuando el hechizo acaba de terminar de lanzarse   |
| PROC_SPELL_PHASE_HIT      | 2    | 0x00000002 | se activa cuando el hechizo impacta a su objetivo           |
| PROC_SPELL_PHASE_FINISH   | 4    | 0x00000004 | se activa después de que el hechizo ha hecho todos sus efectos sobre todos los objetivos |
| PROC_SPELL_PHASE_MASK_ALL | 7    | 0x00000007 | Todas las máscaras combinadas                               |

### HitMask

Se usa para añadir condiciones especiales a los hechizos; algunos hechizos podrían activarse solo en golpes críticos, por ejemplo.

| Event                   | Flag  | Bit        | Comment                          |
| ----------------------- | ----- | ---------- | -------------------------------- |
| PROC\_HIT\_NONE         | 0     | 0x00000000 | (especial, ver nota al pie)      |
| PROC\_HIT\_NORMAL       | 1     | 0x00000001 | solo golpes no críticos          |
| PROC\_HIT\_CRITICAL     | 2     | 0x00000002 | solo golpes críticos             |
| PROC\_HIT\_MISS         | 4     | 0x00000004 | autoexplicativo                  |
| PROC\_HIT\_FULL\_RESIST | 8     | 0x00000008 | solo en resistencia total (sin parcial) |
| PROC\_HIT\_DODGE        | 16    | 0x00000010 | autoexplicativo                  |
| PROC\_HIT\_PARRY        | 32    | 0x00000020 | autoexplicativo                  |
| PROC\_HIT\_BLOCK        | 64    | 0x00000040 | bloqueo parcial o total          |
| PROC\_HIT\_EVADE        | 128   | 0x00000080 | autoexplicativo                  |
| PROC\_HIT\_IMMUNE       | 256   | 0x00000100 | autoexplicativo                  |
| PROC\_HIT\_DEFLECT      | 512   | 0x00000200 | autoexplicativo                  |
| PROC\_HIT\_ABSORB       | 1024  | 0x00000400 | absorción parcial o total        |
| PROC\_HIT\_REFLECT      | 2048  | 0x00000800 | autoexplicativo                  |
| PROC\_HIT\_INTERRUPT    | 4096  | 0x00001000 | (sin usar por ahora)             |
| PROC\_HIT\_FULL\_BLOCK  | 8192  | 0x00002000 | solo en bloqueo total            |
| PROC\_HIT\_MASK\_ALL    | 12287 | 0x00002FFF | Todas las máscaras combinadas    |

PROC\_HIT\_NONE se activará en:

-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL, cuando el trigger es TAKEN
-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL+PROC\_HIT\_ABSORB, cuando el trigger es DONE

### AttributesMask

Añade comportamiento especial al proc; el hechizo podría activar el proc solo si se cumplen estas condiciones.

| Event                                   | Flag | Bit       | Comment                                                                                  |
| --------------------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------- |
| PROC\_ATTR\_REQ\_EXP\_OR\_HONOR         | 1    | 0x0000001 | requiere que el objetivo del proc dé exp u honor para que el aura procee                 |
| PROC\_ATTR\_TRIGGERED\_CAN\_PROC        | 2    | 0x0000002 | el aura puede procear incluso con hechizos activados (triggered)                          |
| PROC\_ATTR\_REQ\_MANA\_COST             | 4    | 0x0000004 | requiere que el hechizo activador tenga un coste de maná para que el aura procee          |
| PROC\_ATTR\_REQ\_SPELLMOD               | 8    | 0x0000008 | requiere que el hechizo activador esté afectado por el aura que procea para gastar cargas |
| PROC\_ATTR\_USE\_STACKS\_FOR\_CHARGES   | 16   | 0x0000010 | el proc consumido quita una acumulación (stack) del aura que procea en lugar de una carga |
| PROC\_ATTR\_REDUCE\_PROC\_60            | 128  | 0x0000080 | el aura debería tener una probabilidad reducida de procear si el nivel del actor del proc > 60 |
| PROC\_ATTR\_CANT\_PROC\_FROM\_ITEM\_CAST| 256  | 0x0000100 | no permite que el aura procee si el proc lo causa un hechizo lanzado por un objeto        |

### DisableEffectsMask

Bitmask para deshabilitar explícitamente que efectos de aura específicos activen el proc. Esto permite un control preciso sobre qué efectos de un aura multi-efecto pueden procear.

| Effect | Flag | Comment                                |
| ------ | ---- | -------------------------------------- |
| 0      | 1    | Deshabilita el efecto de proc de aura 0 |
| 1      | 2    | Deshabilita el efecto de proc de aura 1 |
| 2      | 4    | Deshabilita el efecto de proc de aura 2 |

### ProcsPerMinute

Si es distinto de cero, este campo controla las veces por minuto que el hechizo debería procear. No deberías establecer a la vez ProcsPerMinute y Chance; en ese caso ProcsPerMinute tiene prioridad.

### Chance

Si es distinto de cero, probabilidad de que el hechizo se active. Si tanto ProcsPerMinute como Chance se dejan en cero, se toma ProcChance del DBC.

### Cooldown

Define cooldowns ocultos en el hechizo, en milisegundos. También conocido como el cooldown interno del proc, o ICD.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `spell_proc_chk_1`.

### Charges

Si es distinto de cero, sobrescribe la cantidad de cargas de aura disponibles para procear. Si no, este valor se toma del DBC.
