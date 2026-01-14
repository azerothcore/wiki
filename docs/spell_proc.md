# spell\_proc

[<-Back-to:World](database-world)

**The \`spell\_proc\` table**

This table holds information on what events (or procs) certain spells are activated. All spells in this table must have apply a SPELL\_AURA\_PROC\_TRIGGER\_SPELL (42) aura. Any entries in this table will overwrite the existing proc settings in the spell's DBC entry.

**Table Structure**

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
| [AttributesMask][11]  | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [ProcsPerMinute][12]  | FLOAT    |            |     | NO   | 0       |        |         |
| [Chance][13]          | FLOAT    |            |     | NO   | 0       |        |         |
| [Cooldown][14]        | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [Charges][15]         | TINYINT  | UNSIGNED   |     | NO   | 0       |        |         |

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
[12]: #procsperminute
[13]: #chance
[14]: #cooldown
[15]: #charges

**Description of the fields**

### SpellId

The Spell ID that is capable to proc on an event. (Can use negative spellId for ranked spells)

### SchoolMask

This field contains a bitmask that controls on what types of spells the proc can be triggered. For example if an aura procs only when the unit it is casted upon is hit by shadow spells (spell 34914). To combine spell schools, just add the bit values.

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

This field controls what family name spells can proc the triggered spell.

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

This field controls what spells' family flags can proc the triggered spell.

### SpellFamilyMask1

`field-no-description|5`

### SpellFamilyMask2

`field-no-description|6`

### ProcFlags

If non-zero, used to override the original spell ProcFlags in DBC.

A bitmask controlling what events trigger the spell. To combine possible events, add the proc bits together.

**Example:** 32+64=96 (PROC\_FLAG\_TAKEN\_MELEE\_SPELL\_HIT + PROC\_FLAG\_SUCCESSFUL\_RANGED\_HIT)

| Event                                   | Flag     | Bit value  | Comment                                                      |
| --------------------------------------- | -------- | ---------- | ------------------------------------------------------------ |
| PROC_FLAG_NONE                          | 0        | 0x00000000 |                                                              |
| PROC_FLAG_KILLED                        | 1        | 0x00000001 | Killed by agressor                                           |
| PROC_FLAG_KILL_AND_GET_XP               | 2        | 0x00000002 | Kill that yields experience or honor                         |
| PROC_FLAG_SUCCESSFUL_MELEE_HIT          | 4        | 0x00000004 | Melee attack hit successful                                  |
| PROC_FLAG_TAKEN_MELEE_HIT               | 8        | 0x00000008 | Damage taken from melee hit                                  |
| PROC_FLAG_SUCCESSFUL_MELEE_SPELL_HIT    | 16       | 0x00000010 | Successful attack by spells that use a melee weapon          |
| PROC_FLAG_TAKEN_MELEE_SPELL_HIT         | 32       | 0x00000020 | Damage taken from spells that use a melee weapon             |
| PROC_FLAG_SUCCESSFUL_RANGED_HIT         | 64       | 0x00000040 | Ranged attack hit successful                                 |
| PROC_FLAG_TAKEN_RANGED_HIT              | 128      | 0x00000080 | Damage taken from ranged attack hit                          |
| PROC_FLAG_SUCCESSFUL_RANGED_SPELL_HIT   | 256      | 0x00000100 | Successful Ranged attack by spells that use a ranged weapon  |
| PROC_FLAG_TAKEN_RANGED_SPELL_HIT        | 512      | 0x00000200 | Damage taken from spells that use a ranged weapon            |
| PROC_FLAG_SUCCESSFUL_POSITIVE_AOE_HIT   | 1024     | 0x00000400 | AoE spell hit successful (not 100% sure if unused)           |
| PROC_FLAG_TAKEN_POSITIVE_AOE            | 2048     | 0x00000800 | Positive AoE spell hit taken (not 100% sure if unused)       |
| PROC_FLAG_SUCCESSFUL_AOE_SPELL_HIT      | 4096     | 0x00001000 | AoE damage spell hit successful (not 100% sure if unused)    |
| PROC_FLAG_TAKEN_AOE_SPELL_HIT           | 8192     | 0x00002000 | AoE damage spell hit taken (not 100% sure if unused)         |
| PROC_FLAG_SUCCESSFUL_POSITIVE_SPELL     | 16384    | 0x00004000 | Positive spell cast successful (by default only on healing)  |
| PROC_FLAG_TAKEN_POSITIVE_SPELL          | 32768    | 0x00008000 | Positive spell hit taken (by default only on healing)        |
| PROC_FLAG_SUCCESSFUL_NEGATIVE_SPELL_HIT | 65536    | 0x00010000 | Negative spell cast successful (by default only on damage)   |
| PROC_FLAG_TAKEN_NEGATIVE_SPELL_HIT      | 131072   | 0x00020000 | Negative spell hit taken (by default only on damage)         |
| PROC_FLAG_DONE_PERIODIC                 | 262144   | 0x00040000 | Periodic damage / healing done, determined from flags 14-17  |
| PROC_FLAG_TAKEN_PERIODIC                | 524288   | 0x00080000 | Periodic damage / healing taken, determined from flags 14-17 |
| PROC_FLAG_TAKEN_ANY_DAMAGE              | 1048576  | 0x00100000 | Any damage taken                                             |
| PROC_FLAG_ON_TRAP_ACTIVATION            | 2097152  | 0x00200000 | On trap activation                                           |
| PROC_FLAG_TAKEN_OFFHAND_HIT             | 4194304  | 0x00400000 | Off-hand melee attacks taken (not used)                      |
| PROC_FLAG_SUCCESSFUL_OFFHAND_HIT        | 8388608  | 0x00800000 | Successful off-hand melee attacks                            |
| PROC_FLAG_DEATH                         | 16777216 | 0x01000000 | Died in any way                                              |

### SpellTypeMask

Used to choose what types of spells may trigger the proc, to combine, just add the bit values.

| Event                       | Flag | Bit        | Comment              |
| --------------------------- | ---- | ---------- | -------------------- |
| PROC_SPELL_TYPE_NONE        | 0    | 0x00000000 |                      |
| PROC_SPELL_TYPE_DAMAGE      | 1    | 0x00000001 | only damaging spells |
| PROC_SPELL_TYPE_HEAL        | 2    | 0x00000002 | only healing spells  |
| PROC_SPELL_TYPE_NO_DMG_HEAL | 4    | 0x00000004 | all other spells     |
| PROC_SPELL_TYPE_MASK_ALL    | 7    | 0x00000007 | All masks combined   |

### SpellPhaseMask

At which phase may the spell trigger the proc, Normally one of them is used at the same time, but they might be combined too.

| Event                     | Flag | Bit        | Comment                                                     |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------- |
| PROC_SPELL_PHASE_NONE     | 0    | 0x00000000 |                                                             |
| PROC_SPELL_PHASE_CAST     | 1    | 0x00000001 | trigger when spell has just finished casting                |
| PROC_SPELL_PHASE_HIT      | 2    | 0x00000002 | trigger when the spell hits its target                      |
| PROC_SPELL_PHASE_FINISH   | 4    | 0x00000004 | trigger after spell has done all its effects on all targets |
| PROC_SPELL_PHASE_MASK_ALL | 7    | 0x00000007 | All masks combined                                          |

### HitMask

Used to add special conditions to spells, some spells might trigger only on critical strikes, for example.

| Event                   | Flag  | Bit        | Comment                          |
| ----------------------- | ----- | ---------- | -------------------------------- |
| PROC\_HIT\_NONE         | 0     | 0x00000000 | (special see footnote)           |
| PROC\_HIT\_NORMAL       | 1     | 0x00000001 | only non-critical hits           |
| PROC\_HIT\_CRITICAL     | 2     | 0x00000002 | only critical hits               |
| PROC\_HIT\_MISS         | 4     | 0x00000004 | self-explanatory                 |
| PROC\_HIT\_FULL\_RESIST | 8     | 0x00000008 | only on full resist (no partial) |
| PROC\_HIT\_DODGE        | 16    | 0x00000010 | self-explanatory                 |
| PROC\_HIT\_PARRY        | 32    | 0x00000020 | self-explanatory                 |
| PROC\_HIT\_BLOCK        | 64    | 0x00000040 | partial or full block            |
| PROC\_HIT\_EVADE        | 128   | 0x00000080 | self-explanatory                 |
| PROC\_HIT\_IMMUNE       | 256   | 0x00000100 | self-explanatory                 |
| PROC\_HIT\_DEFLECT      | 512   | 0x00000200 | self-explanatory                 |
| PROC\_HIT\_ABSORB       | 1024  | 0x00000400 | partial or full absorb           |
| PROC\_HIT\_REFLECT      | 2048  | 0x00000800 | self-explanatory                 |
| PROC\_HIT\_INTERRUPT    | 4096  | 0x00001000 | (not used atm)                   |
| PROC\_HIT\_FULL\_BLOCK  | 8192  | 0x00002000 | only on full block               |
| PROC\_HIT\_MASK\_ALL    | 12287 | 0x00002FFF | All masks combined               |

PROC\_HIT\_NONE will trigger on:

-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL, when trigger is TAKEN
-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL+PROC\_HIT\_ABSORB, when trigger is DONE

### AttributesMask

Adds special behaviour to the proc, spell might trigger proc only if these conditions are fullfilled

| Event                            | Flag | Bit       | Comment                                                                       |
| -------------------------------- | ---- | --------- | ----------------------------------------------------------------------------- |
| PROC\_ATTR\_REQ\_EXP\_OR\_HONOR  | 1    | 0x0000001 | requires proc target to give exp or honor                                     |
| PROC\_ATTR\_TRIGGERED\_CAN\_PROC | 2    | 0x0000002 | aura can proc even when spell is triggered by another                         |
| PROC\_ATTR\_REQ\_MANA\_COST      | 4    | 0x0000004 | requires triggering spell to have a mana cost                                 |
| PROC\_ATTR\_REQ\_SPELLMOD        | 8    | 0x0000008 | requires triggering spell to be affected by aura SpellId (only for mod drops) |
| PROC\_ATTR\_DISABLE\_EFF\_0      | 16   | 0x0000010 | explicitly disables aura proc effect 0                                        |
| PROC\_ATTR\_DISABLE\_EFF\_1      | 32   | 0x0000020 | explicitly disables aura proc effect 1                                        |
| PROC\_ATTR\_DISABLE\_EFF\_2      | 64   | 0x0000040 | explicitly disables aura proc effect 2                                        |
| PROC\_ATTR\_REDUCE\_PROC\_60     | 128  | 0x0000080 | aura has a reduced chance to proc if level of proc actor > 60                 |

### ProcsPerMinute

If non-zero, this field controls the times per minute that the spell should proc. You might not set both ProcsPerMinute and Chance. in that case ProcsPerMinute takes precedence.

### Chance

If non-zero, chance for spell to trigger. If both ProcsPerMinute and Chance are left in zero, takes ProcChance from DBC.

### Cooldown

Define hidden cooldowns on the spell, in milliseconds. Also known as the proc's internal cooldown, or ICD.

Value must be >=0. If the value does not meet the condition the SQL will fail on `spell_proc_chk_1`.

### Charges

If non-zero, overrides amount of aura charges available to proc. Else this value is taken from DBC.
