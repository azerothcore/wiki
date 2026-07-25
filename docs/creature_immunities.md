# creature_immunities

[<-Back-to:World](database-world)

**The `creature_immunities` table**

This table centralises creature and spell immunities. `creature_template.CreatureImmunitiesId` points to an entry in this table. Spells may also reference a `creature_immunities` entry via Aura Id 147 (`SPELL_AURA_MECHANIC_IMMUNITY_MASK`) where `misc` stores the referenced id.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | MEDIUMINT | UNSIGNED | PRI | NO | 0 | | Identifier |
| [SchoolMask](#schoolmask) | TINYINT | UNSIGNED | | NO | 0 | | Bitmask of spell schools |
| [DispelTypeMask](#dispeltypemask) | SMALLINT | UNSIGNED | | NO | 0 | | Dispel-type mask |
| [MechanicsMask](#mechanicsmask) | BIGINT | UNSIGNED | | NO | 0 | | Bitmask of mechanic immunities |
| [Effects](#effects) | MEDIUMTEXT | | | NO | (NULL) | | Effect ids or list blocked by this entry |
| [Auras](#auras) | MEDIUMTEXT | | | NO | (NULL) | | Aura ids or list blocked by this entry |
| [ImmuneAoE](#immuneaoe) | TINYINT(1) | | | NO | 0 | | Blocks area of effect spells (boolean) |
| [ImmuneChain](#immunechain) | TINYINT(1) | | | NO | 0 | | Blocks chain effects (boolean) |
| [Comment](#comment) | MEDIUMTEXT | | | NO | (NULL) | | Free-text description |

**Description of the fields**

### ID

- Positive references typically come from spells confirming presence of an immunity. (Aura Id 147 `SPELL_AURA_MECHANIC_IMMUNITY_MASK`)
- Negative values are custom engine/core-set immunities.


### SchoolMask

| Value | Name |
| -----:| ---- |
| 1 | SPELL_SCHOOL_NORMAL |
| 2 | SPELL_SCHOOL_HOLY |
| 4 | SPELL_SCHOOL_FIRE |
| 8 | SPELL_SCHOOL_NATURE |
| 16 | SPELL_SCHOOL_FROST |
| 32 | SPELL_SCHOOL_SHADOW |
| 64 | SPELL_SCHOOL_ARCANE |

Full mask (all schools) = `1+2+4+8+16+32+64 = 127`

### DispelTypeMask

| Value | Name |
| -----:| ---- |
| 1 | DISPEL_NONE |
| 2 | DISPEL_MAGIC |
| 4 | DISPEL_CURSE |
| 8 | DISPEL_DISEASE |
| 16 | DISPEL_POISON |
| 32 | DISPEL_STEALTH |
| 64 | DISPEL_INVISIBILITY |
| 128 | DISPEL_ALL |
| 256 | DISPEL_SPE_NPC_ONLY |
| 512 | DISPEL_ENRAGE |
| 1024 | DISPEL_ZG_TICKET |
| 2048 | DESPEL_OLD_UNUSED |

`DISPEL_ALL_MASK` (common mask for removing typical harmful schools) is the combination of the magic/curse/disease/poison bits:

Numeric value: `2 | 4 | 8 | 16 = 30`

### MechanicsMask

| Value | Name | Notes |
| -----:| ---- | ----- |
| 0x1 | CHARM |
| 0x2 | DISORIENTED |
| 0x4 | DISARM |
| 0x8 | DISTRACT |
| 0x10 | FEAR |
| 0x20 | GRIP | Death Grip and similar effects |
| 0x40 | ROOT |
| 0x80 | SLOW_ATTACK |
| 0x100 | SILENCE |
| 0x200 | SLEEP |
| 0x400 | SNARE |
| 0x800 | STUN |
| 0x1000 | FREEZE |
| 0x2000 | KNOCKOUT | Incapacitate effects (e.g. Repentance) |
| 0x4000 | BLEED |
| 0x8000 | BANDAGE | Healing-related mechanics |
| 0x10000 | POLYMORPH |
| 0x20000 | BANISH |
| 0x40000 | SHIELD |
| 0x80000 | SHACKLE | Shackle Undead only |
| 0x100000 | MOUNT |
| 0x200000 | INFECTED | e.g. Frost Fever, Blood Plague |
| 0x400000 | TURN | e.g. Turn Evil |
| 0x800000 | HORROR | e.g. Death Coil |
| 0x1000000 | INVULNERABILITY | Forbearance, Nether Protection, Diplomatic Immunity only |
| 0x2000000 | INTERRUPT |
| 0x4000000 | DAZE |
| 0x8000000 | DISCOVERY | Create item effects |
| 0x10000000 | IMMUNE_SHIELD | Divine Shield, Ice Block, Hand of Protection |
| 0x20000000 | SAPPED |
| 0x40000000 | ENRAGED |

### Effects

See [spell effects reference](spell-effects-reference)

### Auras

See [spell aura reference](spell-aura-reference)

### ImmuneAoE

previously 
- `creature_flags.extra` `+4194304` AVOID_AOE - ignored by aoe attacks (for icc blood prince council npc - Dark Nucleus)`

**Examples**

- NO_TAUNT `creature_flags.extra` `+256` : Effects ATTACK_ME `114` and MOD_TAUNT Auras `11`
- IMMUNITY_KNOCKBACK `creature_flags.extra` `+1073741824` : EFFECT_KNOCK_BACK, EFFECT_KNOCK_BACK_DEST, EFFECT_PULL_TOWARDS, EFFECT_PULL_TOWARDS_DEST Effects `98,124,144,145`
