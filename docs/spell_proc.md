# spell\_proc

[<-Back-to:World](database-world)

**The \`spell\_proc\` table**

This table holds information on what events (or procs) certain spells are activated. All spells in this table must have apply a SPELL\_AURA\_PROC\_TRIGGER\_SPELL (42) aura. Any entries in this table will overwrite the existing proc settings in the spell's DBC entry.

**Table: spell\_proc's Structure**

| Field                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [SpellId][1]             | INT      | SIGNED     | PRI | NO   | 0       |       |         |
| [SchoolMask][2]          | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellFamilyName][3]     | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellFamilyMask0][4]    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellFamilyMask1][5]    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellFamilyMask2][6]    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [ProcFlags][7]           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellTypeMask][8]       | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [SpellPhaseMask][9]      | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [HitMask][10]            | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [AttributesMask][11]     | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [DisableEffectsMask][12] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [ProcsPerMinute][13]     | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [Chance][14]             | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [Cooldown][15]           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [Charges][16]            | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |

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

**Description of the table's fields**

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

Second 32 bits of the spell family mask. See [SpellFamilyMask0](#spellfamilymask0).

### SpellFamilyMask2

Third 32 bits of the spell family mask. See [SpellFamilyMask0](#spellfamilymask0).

### ProcFlags

If non-zero, used to override the original spell ProcFlags in DBC.

A bitmask controlling what events trigger the spell. To combine possible events, add the proc bits together.

**Example:** 32+64=96 (PROC\_FLAG\_TAKEN\_SPELL\_MELEE\_DMG\_CLASS + PROC\_FLAG\_DONE\_RANGED\_AUTO\_ATTACK)

| Event                                     | Flag     | Bit value  | Comment                                                           |
| ----------------------------------------- | -------- | ---------- | ----------------------------------------------------------------- |
| PROC_FLAG_NONE                            | 0        | 0x00000000 |                                                                   |
| PROC_FLAG_KILLED                          | 1        | 0x00000001 | Killed by an aggressor                                            |
| PROC_FLAG_KILL                            | 2        | 0x00000002 | Killed a target, in most cases one that gives experience or honor |
| PROC_FLAG_DONE_MELEE_AUTO_ATTACK          | 4        | 0x00000004 | Done a melee auto attack                                          |
| PROC_FLAG_TAKEN_MELEE_AUTO_ATTACK         | 8        | 0x00000008 | Taken a melee auto attack                                         |
| PROC_FLAG_DONE_SPELL_MELEE_DMG_CLASS      | 16       | 0x00000010 | Done an attack with a spell of the melee damage class             |
| PROC_FLAG_TAKEN_SPELL_MELEE_DMG_CLASS     | 32       | 0x00000020 | Taken an attack from a spell of the melee damage class            |
| PROC_FLAG_DONE_RANGED_AUTO_ATTACK         | 64       | 0x00000040 | Done a ranged auto attack                                         |
| PROC_FLAG_TAKEN_RANGED_AUTO_ATTACK        | 128      | 0x00000080 | Taken a ranged auto attack                                        |
| PROC_FLAG_DONE_SPELL_RANGED_DMG_CLASS     | 256      | 0x00000100 | Done an attack with a spell of the ranged damage class            |
| PROC_FLAG_TAKEN_SPELL_RANGED_DMG_CLASS    | 512      | 0x00000200 | Taken an attack from a spell of the ranged damage class           |
| PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_POS   | 1024     | 0x00000400 | Done a positive spell of damage class none                        |
| PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_POS  | 2048     | 0x00000800 | Taken a positive spell of damage class none                       |
| PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_NEG   | 4096     | 0x00001000 | Done a negative spell of damage class none                        |
| PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_NEG  | 8192     | 0x00002000 | Taken a negative spell of damage class none                       |
| PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_POS  | 16384    | 0x00004000 | Done a positive spell of the magic damage class                   |
| PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_POS | 32768    | 0x00008000 | Taken a positive spell of the magic damage class                  |
| PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_NEG  | 65536    | 0x00010000 | Done a negative spell of the magic damage class                   |
| PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_NEG | 131072   | 0x00020000 | Taken a negative spell of the magic damage class                  |
| PROC_FLAG_DONE_PERIODIC                   | 262144   | 0x00040000 | Done periodic damage or healing                                   |
| PROC_FLAG_TAKEN_PERIODIC                  | 524288   | 0x00080000 | Taken periodic damage or healing                                  |
| PROC_FLAG_TAKEN_DAMAGE                    | 1048576  | 0x00100000 | Taken any damage                                                  |
| PROC_FLAG_DONE_TRAP_ACTIVATION            | 2097152  | 0x00200000 | On trap activation                                                |
| PROC_FLAG_DONE_MAINHAND_ATTACK            | 4194304  | 0x00400000 | Done a main-hand melee attack, spell or auto attack               |
| PROC_FLAG_DONE_OFFHAND_ATTACK             | 8388608  | 0x00800000 | Done an off-hand melee attack, spell or auto attack               |
| PROC_FLAG_DEATH                           | 16777216 | 0x01000000 | Died in any way                                                   |

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

Adds special behaviour to the proc, spell might trigger proc only if these conditions are fulfilled.

| Event                                   | Flag | Bit       | Comment                                                                                  |
| --------------------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------- |
| PROC\_ATTR\_REQ\_EXP\_OR\_HONOR         | 1    | 0x0000001 | requires proc target to give exp or honor for aura proc                                  |
| PROC\_ATTR\_TRIGGERED\_CAN\_PROC        | 2    | 0x0000002 | aura can proc even with triggered spells                                                 |
| PROC\_ATTR\_REQ\_MANA\_COST             | 4    | 0x0000004 | requires triggering spell to have a mana cost for aura proc                              |
| PROC\_ATTR\_REQ\_SPELLMOD               | 8    | 0x0000008 | requires triggering spell to be affected by proccing aura to drop charges                |
| PROC\_ATTR\_USE\_STACKS\_FOR\_CHARGES   | 16   | 0x0000010 | consuming proc drops a stack from proccing aura instead of charge                        |
| PROC\_ATTR\_REDUCE\_PROC\_60            | 128  | 0x0000080 | aura should have a reduced chance to proc if level of proc actor > 60                    |
| PROC\_ATTR\_CANT\_PROC\_FROM\_ITEM\_CAST| 256  | 0x0000100 | do not allow aura proc if proc is caused by a spell casted by item                       |

### DisableEffectsMask

Bitmask to explicitly disable specific aura effects from triggering the proc. This allows fine-grained control over which effects of a multi-effect aura can proc.

| Effect | Flag | Comment                                |
| ------ | ---- | -------------------------------------- |
| 0      | 1    | Disables aura proc effect 0            |
| 1      | 2    | Disables aura proc effect 1            |
| 2      | 4    | Disables aura proc effect 2            |

### ProcsPerMinute

If non-zero, this field controls the times per minute that the spell should proc. You might not set both ProcsPerMinute and Chance. in that case ProcsPerMinute takes precedence.

### Chance

If non-zero, chance for spell to trigger. If both ProcsPerMinute and Chance are left in zero, takes ProcChance from DBC.

### Cooldown

Define hidden cooldowns on the spell, in milliseconds. Also known as the proc's internal cooldown, or ICD.

Value must be >=0. If the value does not meet the condition the SQL will fail on `spell_proc_chk_1`.

### Charges

If non-zero, overrides amount of aura charges available to proc. Else this value is taken from DBC.
