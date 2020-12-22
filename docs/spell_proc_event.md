# spell_proc_event

[<-Back-to:World](database-world.md)

**The \`spell_proc_event\` table**

**Structure**

Column | Type | Description
:--- | :--- | :---
Entry | mediumint(8) | 
SchoolMask | tinyint(4) | 
SpellFamilyName | smallint(5) unsigned | 
SpellFamilyMask0 | int(10) unsigned | 
SpellFamilyMask1 | int(10) unsigned | 
SpellFamilyMask2 | int(10) unsigned | 
ProcFlags | int(10) unsigned | 
ProcEx | int(10) unsigned | 
PpmRate | float | 
CustomChance | float | 
Cooldown | int(10) unsigned | 

**Description of the fields**

### Entry
The Spell ID that is capable to proc on an event. (Can use negative spellId for ranked spells)

### SchoolMask
This field contains a bitmask that controls on what types of spells the proc can be triggered. For example if an aura procs only when the unit it is casted upon is hit by shadow spells (spell 34914). To combine spell schools, just add the bit values.

Name | Bit | Hex | Comment
:--- | :--- | :--- | :--- 
SPELL_SCHOOL_NORMAL | 1 | 0x01 | Physical Damage
SPELL_SCHOOL_HOLY | 2 | 0x02 | Holy Damage
SPELL_FIRE | 4 | 0x04 | Fire Damage
SPEL_SCHOOL_NATURE | 8 | 0x08 | Nature Damage
SPELL_SCHOOL_FROST | 16 | 0x10 | Frost Damage
SPELL_SCHOOL_SHADOW | 32 | 0x20 | Shadow Damage
SPELL_SCHOOL_ARCANE | 64 | 0x40 | Arcane Damage

### SpellFamilyName
This fireld controls what family name spells can proc the triggered spell.
ID | Family Name
:--- | :---
0 | Generic
3 | Mage
4 | Warrior
5 | Warlock
6 | Priest
7 | Druid
8 | Rogue
9 | Hunter
10 | Paladin
11 | Shaman
13 | Potion
15 | Death Knight

### SpellFamilyMask0
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### SpellFamilyMask1
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### SpellFamilyMask2
This field controls what spells' family flags can proc the triggered spell (you can find SpellFamilyFlags of some spell, using SpellWork).

### ProcFlags
If non-zero, used to override the original spell ProcFlags in DBC.

A bitmask controlling what events trigger the spell. To combine possible events, add the proc bits together.

Event | Bit | Hex | Comment
:--- | :--- | :--- | :--- 
PROC_FLAG_NONE | 0 | 0x00000000 |
PROC_FLAG_KILLED | 1 | 0x00000001 | Killed by aggressor
PROC_FLAG_KILL | 2 | 0x00000002 | Kill that yields experience or honor
PROC_FLAG_DONE_MELEE_AUTO_ATTACK | 4 | 0x00000004 | Successful melee attack hit 
PROC_FLAG_TAKEN_MELEE_AUTO_ATTACK | 8 | 0x00000008 | Damage taken from melee hit
PROC_FLAG_DONE_SPELL_MELEE_DMG_CLASS | 16 | 0x00000010 | Successful attack by a spell that use a melee weapon
PROC_FLAG_TAKEN_SPELL_MELEE_DMG_CLASS | 32 | 0x00000020 | Damage taken from a spell that use a melee weapon
PROC_FLAG_DONE_RANGED_AUTO_ATTACK | 64 | 0x00000040 | Successful ranged attack hit
PROC_FLAG_TAKEN_RANGED_AUTO_ATTACK | 128 | 0x00000080 | Damage taken from ranged attack hit
PROC_FLAG_DONE_SPELL_RANGED_DMG_CLASS | 256 | 0x00000100 | Successful ranged attack by spells that use a ranged weapon
PROC_FLAG_TAKEN_SPELL_RANGED_DMG_CLASS | 512 | 0x00000200 | Damage taken from spells that use a ranged weapon
PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_POS | 1024 | 0x00000400 | Done positive spell that has dmg class none
PROC_FLAG_TAKEN_SPELL_NONE_DMG_CLASS_POS | 2048 | 0x00000800 | Taken positive spell that has dmg class none
PROC_FLAG_DONE_SPELL_NONE_DMG_CLASS_NEG | 4096 | 0x00001000 | Done negative spell that has dmg class none
