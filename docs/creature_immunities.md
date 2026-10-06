# creature\_immunities

[<-Back-to:World](database-world)

**The \`creature\_immunities\` table**

This table centralises creature and spell immunities. `creature_template.CreatureImmunitiesId` points to an entry in this table. Spells may also reference a `creature_immunities` entry via Aura Id 147 (`SPELL_AURA_MECHANIC_IMMUNITY_MASK`) where `misc` stores the referenced id.

**Table: creature\_immunities's Structure**

| Field                             | Type       |     | Null | Key | Default | Extra | Comment                                  |
| :-------------------------------- | :--------- | :-- | :--: | :-: | :-----: | :---: | :--------------------------------------- |
| [ID](#id)                         | INT        |     | NO   | PRI |         |       | Identifier                               |
| [SchoolMask](#schoolmask)         | TINYINT    |     | NO   |     | 0       |       | Bitmask of spell schools                 |
| [DispelTypeMask](#dispeltypemask) | SMALLINT   |     | NO   |     | 0       |       | Dispel-type mask                         |
| [MechanicsMask](#mechanicsmask)   | BIGINT     |     | NO   |     | 0       |       | Bitmask of mechanic immunities           |
| [Effects](#effects)               | MEDIUMTEXT |     | NO   |     |         |       | Effect ids or list blocked by this entry |
| [Auras](#auras)                   | MEDIUMTEXT |     | NO   |     |         |       | Aura ids or list blocked by this entry   |
| [ImmuneAoE](#immuneaoe)           | TINYINT(1) |     | NO   |     | 0       |       | Blocks area of effect spells (boolean)   |
| [ImmuneChain](#immunechain)       | TINYINT(1) |     | NO   |     | 0       |       | Blocks chain effects (boolean)           |
| [Comment](#comment)               | MEDIUMTEXT |     | NO   |     |         |       | Free-text description                    |

**Description of the table's fields**

### ID

- Positive references typically come from spells confirming presence of an immunity. (Aura Id 147 `SPELL_AURA_MECHANIC_IMMUNITY_MASK`)
- Negative values are custom engine/core-set immunities.


### SchoolMask

| Value | Hex    | Flag                | Comment |
| :---- | :----: | :------------------ | :------ |
| 1     | `0x01` | SPELL_SCHOOL_NORMAL |         |
| 2     | `0x02` | SPELL_SCHOOL_HOLY   |         |
| 4     | `0x04` | SPELL_SCHOOL_FIRE   |         |
| 8     | `0x08` | SPELL_SCHOOL_NATURE |         |
| 16    | `0x10` | SPELL_SCHOOL_FROST  |         |
| 32    | `0x20` | SPELL_SCHOOL_SHADOW |         |
| 64    | `0x40` | SPELL_SCHOOL_ARCANE |         |

Full mask (all schools) = `1+2+4+8+16+32+64 = 127`

### DispelTypeMask

| Value | Hex      | Flag                | Comment |
| :---- | :------: | :------------------ | :------ |
| 1     | `0x0001` | DISPEL_NONE         |         |
| 2     | `0x0002` | DISPEL_MAGIC        |         |
| 4     | `0x0004` | DISPEL_CURSE        |         |
| 8     | `0x0008` | DISPEL_DISEASE      |         |
| 16    | `0x0010` | DISPEL_POISON       |         |
| 32    | `0x0020` | DISPEL_STEALTH      |         |
| 64    | `0x0040` | DISPEL_INVISIBILITY |         |
| 128   | `0x0080` | DISPEL_ALL          |         |
| 256   | `0x0100` | DISPEL_SPE_NPC_ONLY |         |
| 512   | `0x0200` | DISPEL_ENRAGE       |         |
| 1024  | `0x0400` | DISPEL_ZG_TICKET    |         |
| 2048  | `0x0800` | DESPEL_OLD_UNUSED   |         |

`DISPEL_ALL_MASK` (common mask for removing typical harmful schools) is the combination of the magic/curse/disease/poison bits:

Numeric value: `2 | 4 | 8 | 16 = 30`

### MechanicsMask

| Value      | Hex          | Flag            | Comment                                                  |
| :--------- | :----------: | :-------------- | :------------------------------------------------------- |
| 1          | `0x00000001` | CHARM           |                                                          |
| 2          | `0x00000002` | DISORIENTED     |                                                          |
| 4          | `0x00000004` | DISARM          |                                                          |
| 8          | `0x00000008` | DISTRACT        |                                                          |
| 16         | `0x00000010` | FEAR            |                                                          |
| 32         | `0x00000020` | GRIP            | Death Grip and similar effects                           |
| 64         | `0x00000040` | ROOT            |                                                          |
| 128        | `0x00000080` | SLOW_ATTACK     |                                                          |
| 256        | `0x00000100` | SILENCE         |                                                          |
| 512        | `0x00000200` | SLEEP           |                                                          |
| 1024       | `0x00000400` | SNARE           |                                                          |
| 2048       | `0x00000800` | STUN            |                                                          |
| 4096       | `0x00001000` | FREEZE          |                                                          |
| 8192       | `0x00002000` | KNOCKOUT        | Incapacitate effects (e.g. Repentance)                   |
| 16384      | `0x00004000` | BLEED           |                                                          |
| 32768      | `0x00008000` | BANDAGE         | Healing-related mechanics                                |
| 65536      | `0x00010000` | POLYMORPH       |                                                          |
| 131072     | `0x00020000` | BANISH          |                                                          |
| 262144     | `0x00040000` | SHIELD          |                                                          |
| 524288     | `0x00080000` | SHACKLE         | Shackle Undead only                                      |
| 1048576    | `0x00100000` | MOUNT           |                                                          |
| 2097152    | `0x00200000` | INFECTED        | e.g. Frost Fever, Blood Plague                           |
| 4194304    | `0x00400000` | TURN            | e.g. Turn Evil                                           |
| 8388608    | `0x00800000` | HORROR          | e.g. Death Coil                                          |
| 16777216   | `0x01000000` | INVULNERABILITY | Forbearance, Nether Protection, Diplomatic Immunity only |
| 33554432   | `0x02000000` | INTERRUPT       |                                                          |
| 67108864   | `0x04000000` | DAZE            |                                                          |
| 134217728  | `0x08000000` | DISCOVERY       | Create item effects                                      |
| 268435456  | `0x10000000` | IMMUNE_SHIELD   | Divine Shield, Ice Block, Hand of Protection             |
| 536870912  | `0x20000000` | SAPPED          |                                                          |
| 1073741824 | `0x40000000` | ENRAGED         |                                                          |

### Effects

See [spell effects reference](spell-effects-reference)

### Auras

See [spell aura reference](spell-aura-reference)

### ImmuneAoE

If 1, the creature can not be hit by area of effect spells. The `CREATURE_FLAG_EXTRA_AVOID_AOE` flag (`+4194304`) in [creature\_template.flags\_extra](creature_template#flagsextra) has the same effect.

### ImmuneChain

If 1, the creature can not be hit by chain effects that jump from another target, like Chain Lightning.

### Comment

A description of the entry. Not used by the core.

**Examples**

Old [flags\_extra](creature_template#flagsextra) values and the Effects and Auras that replace them:

- NO_TAUNT `creature_flags.extra` `+256` : Effects ATTACK_ME `114` and MOD_TAUNT Auras `11`
- IMMUNITY_KNOCKBACK `creature_flags.extra` `+1073741824` : EFFECT_KNOCK_BACK, EFFECT_KNOCK_BACK_DEST, EFFECT_PULL_TOWARDS, EFFECT_PULL_TOWARDS_DEST Effects `98,124,144,145`
