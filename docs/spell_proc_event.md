# spell_proc_event

[<-Back-to:World](database-world)

**The \`spell_proc_event\` table**

`table-no-description`

**Table Structure**

| Field                 | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Entry][1]            | MEDIUMINT | SIGNED     | PRI |      | 0       |       |         |
| [SchoolMask][2]       | TINYINT   | SIGNED     |     |      | 0       |       |         |
| [SpellFamilyName][3]  | SMALLINT  | UNSIGNED   |     |      | 0       |       |         |
| [SpellFamilyMask0][4] | INT       | UNSIGNED   |     |      | 0       |       |         |
| [SpellFamilyMask1][5] | INT       | UNSIGNED   |     |      | 0       |       |         |
| [SpellFamilyMask2][6] | INT       | UNSIGNED   |     |      | 0       |       |         |
| [procFlags][7]        | INT       | UNSIGNED   |     |      | 0       |       |         |
| [procEx][8]           | INT       | UNSIGNED   |     |      | 0       |       |         |
| [procPhase][9]        | INT       | UNSIGNED   |     |      | 0       |       |         |
| [ppmRate][10]         | FLOAT     | SIGNED     |     |      | 0       |       |         |
| [CustomChance][11]    | FLOAT     | SIGNED     |     |      | 0       |       |         |
| [Cooldown][12]        | INT       | UNSIGNED   |     |      | 0       |       |         |

[1]: #entry
[2]: #schoolmask
[3]: #spellfamilyname
[4]: #spellfamilymask0
[5]: #spellfamilymask1
[6]: #spellfamilymask2
[7]: #procflags
[8]: #procex
[9]: #procphase
[10]: #ppmrate
[11]: #customchance
[12]: #cooldown

**Description of the fields**

### Entry
The Spell ID that is capable of proc on an event. For ranked spells, use a negative Spell ID.

### SchoolMask
This field contains a bitmask that controls which types of spells the proc can be triggered. For example, if an aura procs only when the unit it is cast upon is hit by shadow spells (spell 34914).

| Flag                | Bit  | Hex  | Comment         |
| ------------------- | ---- | ---- | --------------- |
| SPELL_SCHOOL_NORMAL | 1    | 0x01 | Physical Damage |
| SPELL_SCHOOL_HOLY   | 2    | 0x02 | Holy Damage     |
| SPELL_FIRE          | 4    | 0x04 | Fire Damage     |
| SPEL_SCHOOL_NATURE  | 8    | 0x08 | Nature Damage   |
| SPELL_SCHOOL_FROST  | 16   | 0x10 | Frost Damage    |
| SPELL_SCHOOL_SHADOW | 32   | 0x20 | Shadow Damage   |
| SPELL_SCHOOL_ARCANE | 64   | 0x40 | Arcane Damage   |

### SpellFamilyName
This field controls what family name spells can proc the triggered spell.

| ID   | Family Name  |
| ---- | ------------ |
| 0    | Generic      |
| 3    | Mage         |
| 4    | Warrior      |
| 5    | Warlock      |
| 6    | Priest       |
| 7    | Druid        |
| 8    | Rogue        |
| 9    | Hunter       |
| 10   | Paladin      |
| 11   | Shaman       |
| 13   | Potion       |
| 15   | Death Knight |

### SpellFamilyMask0
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### SpellFamilyMask1
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### SpellFamilyMask2
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### procFlags
If non-zero, override the original spell ProcFlags in DBC.

A bitmask controls what events trigger the spell. To combine possible events, add the proc bits together.

| Flag                                      | Bit      | Hex        | Comment                                                                                                    |
| ----------------------------------------- | -------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| PROC_FLAG_NONE                            | 0        | 0x00000000 |                                                                                                            |
| PROC_FLAG_KILLED                          | 1        | 0x00000001 | Killed by aggressor                                                                                        |
| PROC_FLAG_KILL                            | 2        | 0x00000002 | Kill that yields experience or honor                                                                       |
| PROC_FLAG_DONE_MELEE_AUTO_ATTACK          | 4        | 0x00000004 | Successful melee attack hit                                                                                |
| PROC_FLAG_TAKEN_MELEE_AUTO_ATTACK         | 8        | 0x00000008 | Damage taken from melee hit                                                                                |
| PROC_FLAG_DONE_SPELL_MELEE_DMG_CLASS      | 16       | 0x00000010 | Successful attack by a spell that use a melee weapon                                                       |
| PROC_FLAG_TAKEN_SPELL_MELEE_DMG_CLASS     | 32       | 0x00000020 | Damage taken from a spell that use a melee weapon                                                          |
| PROC_FLAG_DONE_RANGED_AUTO_ATTACK         | 64       | 0x00000040 | Successful ranged attack hit                                                                               |
| PROC_FLAG_TAKEN_RANGED_AUTO_ATTACK        | 128      | 0x00000080 | Damage taken from ranged attack hit                                                                        |
| PROC_FLAG_DONE_SPELL_RANGED_DMG_CLASS     | 256      | 0x00000100 | Successful ranged attack by spells that use a ranged weapon                                                |
| PROC_FLAG_TAKEN_SPELL_RANGED_DMG_CLASS    | 512      | 0x00000200 | Damage taken from spells that use a ranged weapon                                                          |
| PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_POS   | 1024     | 0x00000400 | Done positive spell that has dmg class none                                                                |
| PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_POS  | 2048     | 0x00000800 | Taken positive spell that has dmg class none                                                               |
| PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_NEG   | 4096     | 0x00001000 | Done negative spell that has dmg class none                                                                |
| PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_NEG  | 8192     | 0x00002000 | Taken negative spell that has dmg class none                                                               |
| PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_POS  | 16384    | 0x00004000 | Done positive spell that has dmg class magic                                                               |
| PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_POS | 32768    | 0x00008000 | Taken positive spell that has dmg class magic                                                              |
| PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_NEG  | 65536    | 0x00010000 | Done negative spell that has dmg class magic                                                               |
| PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_NEG | 131072   | 0x00020000 | Taken negative spell that has dmg class magic                                                              |
| PROC_FLAG_DONE_PERIODIC                   | 262144   | 0x00040000 | Successful done periodic (default: Negative ; For positive add PROC_EX_PERIODIC_POSITIVE(Not Implemented)) |
| PROC_FLAG_TAKEN_PERIODIC                  | 524288   | 0x00080000 | Successful done periodic (default: Negative ; For positive add PROC_EX_PERIODIC_POSITIVE(Not Implemented)) |
| PROC_FLAG_TAKEN_DAMAGE                    | 1048576  | 0x00100000 | Taken any damage                                                                                           |
| PROC_FLAG_DONE_TRAP_ACTIVATION            | 2097152  | 0x00200000 | On trap activation                                                                                         |
| PROC_FLAG_DONE_MAINHAND_ATTACK            | 4194304  | 0x00400000 | Done main-hand melee attacks (spell and autoattack)                                                        |
| PROC_FLAG_DONE_OFFHAND_ATTACK             | 8388608  | 0x00800000 | Done off-hand melee attacks (spell and autoattack)                                                         |
| PROC_FLAG_DEATH                           | 16777216 | 0x01000000 | Died in any way                                                                                            |

### procEx
| Flag                        | Bit     | Hex       | Comment                                                                                |
| --------------------------- | ------- | --------- | -------------------------------------------------------------------------------------- |
| PROC_EX_NONE                | 0       | 0x0000000 | If none can trigger on Hit/Crit only (passive spells MUST defined by SpellFamily flag) |
| PROC_EX_NORMAL_HIT          | 1       | 0x0000001 |                                                                                        |
| PROC_EX_CRITICAL_HIT        | 2       | 0x0000002 |                                                                                        |
| PROC_EX_MISS                | 4       | 0x0000004 |                                                                                        |
| PROC_EX_RESIST              | 8       | 0x0000008 |                                                                                        |
| PROC_EX_DODGE               | 16      | 0x0000010 |                                                                                        |
| PROC_EX_PARRY               | 32      | 0x0000020 |                                                                                        |
| PROC_EX_BLOCK               | 64      | 0x0000040 |                                                                                        |
| PROC_EX_EVADE               | 128     | 0x0000080 |                                                                                        |
| PROC_EX_IMMUNE              | 256     | 0x0000100 |                                                                                        |
| PROC_EX_DEFLECT             | 512     | 0x0000200 |                                                                                        |
| PROC_EX_ABSORB              | 1024    | 0x0000400 |                                                                                        |
| PROC_EX_REFLECT             | 2048    | 0x0000800 |                                                                                        |
| PROC_EX_INTERRUPT           | 4096    | 0x0001000 | Melee hit result can be Interrupt (not used)                                           |
| PROC_EX_FULL_BLOCK          | 8192    | 0x0002000 | Block all attack damage                                                                |
| PROC_EX_RESERVED2           | 16384   | 0x0004000 |                                                                                        |
| PROC_EX_NOT_ACTIVE_SPELL    | 32768   | 0x0008000 | Spell mustn't do damage/heal to proc                                                   |
| PROC_EX_EX_TRIGGER_ALWAYS   | 65536   | 0x0010000 | If set trigger always no matter of hit result                                          |
| PROC_EX_EX_ONE_TIME_TRIGGER | 131072  | 0x0020000 | If set trigger always but only one time (not implemented yet)                          |
| PROC_EX_ONLY_ACTIVE_SPELL   | 262144  | 0x0040000 | Spell has to do damage/heal to proc                                                    |
| PROC_EX_NO_OVERHEAL         | 524288  | 0x0080000 | Proc if heal did some work                                                             |
| PROC_EX_NO_AURA_REFRESH     | 1048576 | 0x0100000 | Proc if aura was not refreshed                                                         |
| PROC_EX_ONLY_FIRST_TICK     | 2097152 | 0x0200000 | Proc only on first tick (in case of periodic spells)                                   |

### procPhase
A bitmask for matching phase of a spellcast on which proc occurs.

| Flag                    | Bit  | Hex       | Comment |
| ----------------------- | ---- | --------- | ------- |
| PROC_SPELL_PHASE_NONE   | 0    | 0x0000000 |         |
| PROC_SPELL_PHASE_CAST   | 1    | 0x0000001 |         |
| PROC_SPELL_PHASE_HIT    | 2    | 0x0000002 |         |
| PROC_SPELL_PHASE_FINISH | 4    | 0x0000004 |         |

### ppmRate
Proc per minute. If 0 the value will be taken from DBC.

ppmRate is a rate and therefore will not be guaranteed to prox X amount of times per minute. ppm is calculated by this formula
```
((WeaponSpeed * PPM) / 600.0f);   // result is chance in percents (probability = Speed_in_sec * (PPM / 60))
```

### CustomChance
If non-zero, chance for the spell to trigger.

### Cooldown
Internal Cooldown (ICD) in milliseconds.
