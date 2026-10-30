# spell\_proc

[<-Back-to:World](database-world)

**The \`spell\_proc\` table**

This table holds information on what events (or procs) certain spells are activated. All spells in this table must have apply a SPELL\_AURA\_PROC\_TRIGGER\_SPELL (42) aura. Any entries in this table will overwrite the existing proc settings in the spell's DBC entry.

**Table: spell\_proc's Structure**

| Field                                     | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [SpellId](#spellid)                       | INT      |          | NO   | PRI | 0       |       |         |
| [SchoolMask](#schoolmask)                 | TINYINT  | UNSIGNED | NO   |     | 0       |       |         |
| [SpellFamilyName](#spellfamilyname)       | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [SpellFamilyMask0](#spellfamilymask0)     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [SpellFamilyMask1](#spellfamilymask1)     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [SpellFamilyMask2](#spellfamilymask2)     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [ProcFlags](#procflags)                   | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [SpellTypeMask](#spelltypemask)           | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [SpellPhaseMask](#spellphasemask)         | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [HitMask](#hitmask)                       | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesMask](#attributesmask)         | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [DisableEffectsMask](#disableeffectsmask) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [ProcsPerMinute](#procsperminute)         | FLOAT    |          | NO   |     | 0       |       |         |
| [Chance](#chance)                         | FLOAT    |          | NO   |     | 0       |       |         |
| [Cooldown](#cooldown)                     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [Charges](#charges)                       | TINYINT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### SpellId

The Spell ID that is capable to proc on an event. (Can use negative spellId for ranked spells)

### SchoolMask

This field contains a bitmask that controls on what types of spells the proc can be triggered. For example if an aura procs only when the unit it is casted upon is hit by shadow spells (spell 34914). To combine spell schools, just add the bit values.

| Value | Hex    | Flag     | School ID |
| :---- | :----: | :------- | :-------- |
| 1     | `0x01` | Physical | 0         |
| 2     | `0x02` | Holy     | 1         |
| 4     | `0x04` | Fire     | 2         |
| 8     | `0x08` | Nature   | 3         |
| 16    | `0x10` | Frost    | 4         |
| 32    | `0x20` | Shadow   | 5         |
| 64    | `0x40` | Arcane   | 6         |

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

| Value    | Hex          | Flag                                      | Comment                                                           |
| :------- | :----------: | :---------------------------------------- | :---------------------------------------------------------------- |
| 0        | `0x00000000` | PROC_FLAG_NONE                            | No flag                                                           |
| 1        | `0x00000001` | PROC_FLAG_KILLED                          | Killed by an aggressor                                            |
| 2        | `0x00000002` | PROC_FLAG_KILL                            | Killed a target, in most cases one that gives experience or honor |
| 4        | `0x00000004` | PROC_FLAG_DONE_MELEE_AUTO_ATTACK          | Done a melee auto attack                                          |
| 8        | `0x00000008` | PROC_FLAG_TAKEN_MELEE_AUTO_ATTACK         | Taken a melee auto attack                                         |
| 16       | `0x00000010` | PROC_FLAG_DONE_SPELL_MELEE_DMG_CLASS      | Done an attack with a spell of the melee damage class             |
| 32       | `0x00000020` | PROC_FLAG_TAKEN_SPELL_MELEE_DMG_CLASS     | Taken an attack from a spell of the melee damage class            |
| 64       | `0x00000040` | PROC_FLAG_DONE_RANGED_AUTO_ATTACK         | Done a ranged auto attack                                         |
| 128      | `0x00000080` | PROC_FLAG_TAKEN_RANGED_AUTO_ATTACK        | Taken a ranged auto attack                                        |
| 256      | `0x00000100` | PROC_FLAG_DONE_SPELL_RANGED_DMG_CLASS     | Done an attack with a spell of the ranged damage class            |
| 512      | `0x00000200` | PROC_FLAG_TAKEN_SPELL_RANGED_DMG_CLASS    | Taken an attack from a spell of the ranged damage class           |
| 1024     | `0x00000400` | PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_POS   | Done a positive spell of damage class none                        |
| 2048     | `0x00000800` | PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_POS  | Taken a positive spell of damage class none                       |
| 4096     | `0x00001000` | PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_NEG   | Done a negative spell of damage class none                        |
| 8192     | `0x00002000` | PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_NEG  | Taken a negative spell of damage class none                       |
| 16384    | `0x00004000` | PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_POS  | Done a positive spell of the magic damage class                   |
| 32768    | `0x00008000` | PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_POS | Taken a positive spell of the magic damage class                  |
| 65536    | `0x00010000` | PROC_FLAG_DONE_SPELL_MAGIC_DMG_CLASS_NEG  | Done a negative spell of the magic damage class                   |
| 131072   | `0x00020000` | PROC_FLAG_TAKEN_SPELL_MAGIC_DMG_CLASS_NEG | Taken a negative spell of the magic damage class                  |
| 262144   | `0x00040000` | PROC_FLAG_DONE_PERIODIC                   | Done periodic damage or healing                                   |
| 524288   | `0x00080000` | PROC_FLAG_TAKEN_PERIODIC                  | Taken periodic damage or healing                                  |
| 1048576  | `0x00100000` | PROC_FLAG_TAKEN_DAMAGE                    | Taken any damage                                                  |
| 2097152  | `0x00200000` | PROC_FLAG_DONE_TRAP_ACTIVATION            | On trap activation                                                |
| 4194304  | `0x00400000` | PROC_FLAG_DONE_MAINHAND_ATTACK            | Done a main-hand melee attack, spell or auto attack               |
| 8388608  | `0x00800000` | PROC_FLAG_DONE_OFFHAND_ATTACK             | Done an off-hand melee attack, spell or auto attack               |
| 16777216 | `0x01000000` | PROC_FLAG_DEATH                           | Died in any way                                                   |

### SpellTypeMask

Used to choose what types of spells may trigger the proc, to combine, just add the bit values.

| Value | Hex          | Flag                        | Comment              |
| :---- | :----------: | :-------------------------- | :------------------- |
| 0     | `0x00000000` | PROC_SPELL_TYPE_NONE        | No flag              |
| 1     | `0x00000001` | PROC_SPELL_TYPE_DAMAGE      | only damaging spells |
| 2     | `0x00000002` | PROC_SPELL_TYPE_HEAL        | only healing spells  |
| 4     | `0x00000004` | PROC_SPELL_TYPE_NO_DMG_HEAL | all other spells     |
| 7     | `0x00000007` | PROC_SPELL_TYPE_MASK_ALL    | All masks combined   |

### SpellPhaseMask

At which phase may the spell trigger the proc, Normally one of them is used at the same time, but they might be combined too.

| Value | Hex          | Flag                      | Comment                                                     |
| :---- | :----------: | :------------------------ | :---------------------------------------------------------- |
| 0     | `0x00000000` | PROC_SPELL_PHASE_NONE     | No flag                                                     |
| 1     | `0x00000001` | PROC_SPELL_PHASE_CAST     | trigger when spell has just finished casting                |
| 2     | `0x00000002` | PROC_SPELL_PHASE_HIT      | trigger when the spell hits its target                      |
| 4     | `0x00000004` | PROC_SPELL_PHASE_FINISH   | trigger after spell has done all its effects on all targets |
| 7     | `0x00000007` | PROC_SPELL_PHASE_MASK_ALL | All masks combined                                          |

### HitMask

Used to add special conditions to spells, some spells might trigger only on critical strikes, for example.

| Value | Hex      | Flag                    | Comment                          |
| :---- | :------: | :---------------------- | :------------------------------- |
| 0     | `0x0000` | PROC\_HIT\_NONE         | (special see footnote)           |
| 1     | `0x0001` | PROC\_HIT\_NORMAL       | only non-critical hits           |
| 2     | `0x0002` | PROC\_HIT\_CRITICAL     | only critical hits               |
| 4     | `0x0004` | PROC\_HIT\_MISS         | self-explanatory                 |
| 8     | `0x0008` | PROC\_HIT\_FULL\_RESIST | only on full resist (no partial) |
| 16    | `0x0010` | PROC\_HIT\_DODGE        | self-explanatory                 |
| 32    | `0x0020` | PROC\_HIT\_PARRY        | self-explanatory                 |
| 64    | `0x0040` | PROC\_HIT\_BLOCK        | partial or full block            |
| 128   | `0x0080` | PROC\_HIT\_EVADE        | self-explanatory                 |
| 256   | `0x0100` | PROC\_HIT\_IMMUNE       | self-explanatory                 |
| 512   | `0x0200` | PROC\_HIT\_DEFLECT      | self-explanatory                 |
| 1024  | `0x0400` | PROC\_HIT\_ABSORB       | partial or full absorb           |
| 2048  | `0x0800` | PROC\_HIT\_REFLECT      | self-explanatory                 |
| 4096  | `0x1000` | PROC\_HIT\_INTERRUPT    | (not used atm)                   |
| 8192  | `0x2000` | PROC\_HIT\_FULL\_BLOCK  | only on full block               |
| 12287 | `0x2FFF` | PROC\_HIT\_MASK\_ALL    | All masks combined               |

PROC\_HIT\_NONE will trigger on:

-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL, when trigger is TAKEN
-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL+PROC\_HIT\_ABSORB, when trigger is DONE

### AttributesMask

Adds special behaviour to the proc, spell might trigger proc only if these conditions are fulfilled.

| Value | Hex      | Flag                                     | Comment                                                                   |
| :---- | :------: | :--------------------------------------- | :------------------------------------------------------------------------ |
| 1     | `0x0001` | PROC\_ATTR\_REQ\_EXP\_OR\_HONOR          | requires proc target to give exp or honor for aura proc                   |
| 2     | `0x0002` | PROC\_ATTR\_TRIGGERED\_CAN\_PROC         | aura can proc even with triggered spells                                  |
| 4     | `0x0004` | PROC\_ATTR\_REQ\_MANA\_COST              | requires triggering spell to have a mana cost for aura proc               |
| 8     | `0x0008` | PROC\_ATTR\_REQ\_SPELLMOD                | requires triggering spell to be affected by proccing aura to drop charges |
| 16    | `0x0010` | PROC\_ATTR\_USE\_STACKS\_FOR\_CHARGES    | consuming proc drops a stack from proccing aura instead of charge         |
| 128   | `0x0080` | PROC\_ATTR\_REDUCE\_PROC\_60             | aura should have a reduced chance to proc if level of proc actor > 60     |
| 256   | `0x0100` | PROC\_ATTR\_CANT\_PROC\_FROM\_ITEM\_CAST | do not allow aura proc if proc is caused by a spell casted by item        |

### DisableEffectsMask

Bitmask to explicitly disable specific aura effects from triggering the proc. This allows fine-grained control over which effects of a multi-effect aura can proc.

| Value | Hex    | Flag                        | Effect |
| :---- | :----: | :-------------------------- | :----- |
| 1     | `0x01` | Disables aura proc effect 0 | 0      |
| 2     | `0x02` | Disables aura proc effect 1 | 1      |
| 4     | `0x04` | Disables aura proc effect 2 | 2      |

### ProcsPerMinute

If non-zero, this field controls the times per minute that the spell should proc. You might not set both ProcsPerMinute and Chance. in that case ProcsPerMinute takes precedence.

### Chance

If non-zero, chance for spell to trigger. If both ProcsPerMinute and Chance are left in zero, takes ProcChance from DBC.

### Cooldown

Define hidden cooldowns on the spell, in milliseconds. Also known as the proc's internal cooldown, or ICD.

Value must be >=0. If the value does not meet the condition the SQL will fail on `spell_proc_chk_1`.

### Charges

If non-zero, overrides amount of aura charges available to proc. Else this value is taken from DBC.
