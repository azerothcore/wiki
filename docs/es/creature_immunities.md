# creature_immunities

[<-Volver a: World](database-world)

**Tabla `creature_immunities`**

Esta tabla centraliza las inmunidades de criaturas y hechizos. `creature_template.CreatureImmunitiesId` apunta a una entrada de esta tabla. Los hechizos también pueden referenciar una entrada de `creature_immunities` mediante el Aura Id 147 (`SPELL_AURA_MECHANIC_IMMUNITY_MASK`), donde `misc` almacena el id referenciado.

**Estructura**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | MEDIUMINT | UNSIGNED | PRI | NO | 0 | | Identificador |
| [SchoolMask](#schoolmask) | TINYINT | UNSIGNED | | NO | 0 | | Bitmask de escuelas de hechizo |
| [DispelTypeMask](#dispeltypemask) | SMALLINT | UNSIGNED | | NO | 0 | | Máscara de tipo de disipación |
| [MechanicsMask](#mechanicsmask) | BIGINT | UNSIGNED | | NO | 0 | | Bitmask de inmunidades a mecánicas |
| [Effects](#effects) | MEDIUMTEXT | | | NO | (NULL) | | Ids de efectos o lista bloqueada por esta entrada |
| [Auras](#auras) | MEDIUMTEXT | | | NO | (NULL) | | Ids de auras o lista bloqueada por esta entrada |
| [ImmuneAoE](#immuneaoe) | TINYINT(1) | | | NO | 0 | | Bloquea hechizos de área (booleano) |
| [ImmuneChain](#immunechain) | TINYINT(1) | | | NO | 0 | | Bloquea efectos en cadena (booleano) |
| [Comment](#comment) | MEDIUMTEXT | | | NO | (NULL) | | Descripción de texto libre |

**Descripción de los campos**

### ID

- Los valores positivos suelen provenir de hechizos que confirman la presencia de una inmunidad. (Aura Id 147 `SPELL_AURA_MECHANIC_IMMUNITY_MASK`)
- Los valores negativos son inmunidades personalizadas definidas por el motor/core.


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

Máscara completa (todas las escuelas) = `1+2+4+8+16+32+64 = 127`

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

`DISPEL_ALL_MASK` (máscara común para eliminar las escuelas dañinas típicas) es la combinación de los bits magic/curse/disease/poison:

Valor numérico: `2 | 4 | 8 | 16 = 30`

### MechanicsMask

| Value | Name | Notes |
| -----:| ---- | ----- |
| 0x1 | CHARM |
| 0x2 | DISORIENTED |
| 0x4 | DISARM |
| 0x8 | DISTRACT |
| 0x10 | FEAR |
| 0x20 | GRIP | Death Grip y efectos similares |
| 0x40 | ROOT |
| 0x80 | SLOW_ATTACK |
| 0x100 | SILENCE |
| 0x200 | SLEEP |
| 0x400 | SNARE |
| 0x800 | STUN |
| 0x1000 | FREEZE |
| 0x2000 | KNOCKOUT | Efectos de incapacitación (p. ej. Repentance) |
| 0x4000 | BLEED |
| 0x8000 | BANDAGE | Mecánicas relacionadas con curación |
| 0x10000 | POLYMORPH |
| 0x20000 | BANISH |
| 0x40000 | SHIELD |
| 0x80000 | SHACKLE | Solo Shackle Undead |
| 0x100000 | MOUNT |
| 0x200000 | INFECTED | p. ej. Frost Fever, Blood Plague |
| 0x400000 | TURN | p. ej. Turn Evil |
| 0x800000 | HORROR | p. ej. Death Coil |
| 0x1000000 | INVULNERABILITY | Solo Forbearance, Nether Protection, Diplomatic Immunity |
| 0x2000000 | INTERRUPT |
| 0x4000000 | DAZE |
| 0x8000000 | DISCOVERY | Efectos de creación de objetos |
| 0x10000000 | IMMUNE_SHIELD | Divine Shield, Ice Block, Hand of Protection |
| 0x20000000 | SAPPED |
| 0x40000000 | ENRAGED |

### Effects

Consulta la [referencia de efectos de hechizo](spell-effects-reference)

### Auras

Consulta la [referencia de auras de hechizo](spell-aura-reference)

### ImmuneAoE

anteriormente
- `creature_flags.extra` `+4194304` AVOID_AOE - ignorado por ataques de área (para el npc del icc blood prince council - Dark Nucleus)`

**Ejemplos**

- NO_TAUNT `creature_flags.extra` `+256` : efectos ATTACK_ME `114` y auras MOD_TAUNT `11`
- IMMUNITY_KNOCKBACK `creature_flags.extra` `+1073741824` : efectos EFFECT_KNOCK_BACK, EFFECT_KNOCK_BACK_DEST, EFFECT_PULL_TOWARDS, EFFECT_PULL_TOWARDS_DEST `98,124,144,145`
