# Spell Aura Reference

[`Back-to:Spell Effects Reference`](spell-effects-reference)

[`Back-to:spell_dbc`](spell_dbc)


### This page contains description regarding the usage of EffectMiscValue and other Spell Aura values.
### Contains only Spell Auras that have known usage of EffectMiscValue or other unconventional values.

**Version is : 3.3.5a**

# Spell Aura Names

SPELL_AURA_MOD_POSSESS = 2
- BasePoints: (+Die Points) Up to the level that can be charmed

SPELL_AURA_MOD_CHARM = 6
- BasePoints: (+Die Points) Up to the level that can be charmed

SPELL_AURA_MOD_THREAT = 10
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_DAMAGE_DONE = 13
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_DAMAGE_TAKEN = 14
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_STEALTH = 16
- EffectMiscValueA: Stealth Type (0 = General, 1 = Trap)

SPELL_AURA_MOD_STEALTH_DETECT = 17
- EffectMiscValueA: Stealth Type (0 = General, 1 = Trap)

SPELL_AURA_MOD_INVISIBILITY = 18
- EffectMiscValueA: [Invisibility Type](#invisibility-type)

SPELL_AURA_MOD_INVISIBILITY_DETECT = 19
- EffectMiscValueA: [Invisibility Type](#invisibility-type)

SPELL_AURA_OBS_MOD_POWER = 21
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_RESISTANCE = 22
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_PERIODIC_TRIGGER_SPELL = 23
- TriggerSpell: Spell ID
- Amplitude: The time in MS that the trigger will land.

SPELL_AURA_PERIODIC_ENERGIZE = 24
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_STAT = 29
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_MOD_SKILL = 30
- EffectMiscValueA: [Skill ID](skillline)

SPELL_AURA_MOD_INCREASE_ENERGY = 35
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_SHAPESHIFT = 36
- EffectMiscValueA: ID from SpellShapeshiftForm.dbc

SPELL_AURA_EFFECT_IMMUNITY = 37
- EffectMiscValueA: ID from [Spell Effect](spell-effects-reference) to become immune to.

SPELL_AURA_STATE_IMMUNITY = 38
- EffectMiscValueA: ID from Spell Auras

SPELL_AURA_SCHOOL_IMMUNITY = 39
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_DAMAGE_IMMUNITY = 40
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_DISPEL_IMMUNITY = 41
- EffectMiscValueA: [Dispel Type](#dispel-type)

SPELL_AURA_TRACK_CREATURES = 44
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_TRACK_RESOURCES = 45
- EffectMiscValueA: [Lock Type](#lock-type)

SPELL_AURA_TRANSFORM = 56
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_AURA_MOD_DAMAGE_DONE_CREATURE = 59
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_SCHOOL_ABSORB = 69
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_SPELL_CRIT_CHANCE_SCHOOL = 71
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_POWER_COST_SCHOOL_PCT = 72
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_POWER_COST_SCHOOL = 73
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_REFLECT_SPELLS_SCHOOL = 74
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_LANGUAGE = 75
- EffectMiscValueA: [Language ID](languages)

SPELL_AURA_MECHANIC_IMMUNITY = 77
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_MOUNTED = 78
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_AURA_MOD_DAMAGE_PERCENT_DONE = 79
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_PERCENT_STAT = 80
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_SPLIT_DAMAGE_PCT = 81
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_BASE_RESISTANCE = 83
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_POWER_REGEN = 85
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_DAMAGE_PERCENT_TAKEN = 87
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MANA_SHIELD = 97
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_SKILL_TALENT = 98
- EffectMiscValueA: [Skill ID](skillline)

SPELL_AURA_MOD_RESISTANCE_PCT = 101
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_MELEE_ATTACK_POWER_VERSUS = 102
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_ADD_FLAT_MODIFIER = 107
- EffectMiscValueA: [Modifier Type](#modifier-type)

SPELL_AURA_ADD_PCT_MODIFIER = 108
- EffectMiscValueA: [Modifier Type](#modifier-type)

SPELL_AURA_MOD_POWER_REGEN_PERCENT = 110
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_RANGED_DAMAGE_TAKEN = 113
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_RANGED_DAMAGE_TAKEN_PCT = 114
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_HEALING = 115
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_MECHANIC_RESISTANCE = 117
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_MOD_HEALING_PCT = 118
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_RANGED_ATTACK_POWER_VERSUS = 131
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_MOD_INCREASE_ENERGY_PERCENT = 132
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_MOD_HEALING_DONE = 135
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_HEALING_DONE_PERCENT = 136
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_TOTAL_STAT_PERCENTAGE = 137
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_FORCE_REACTION = 139
- EffectMiscValueA: ID from [faction.dbc](faction)

SPELL_AURA_MOD_BASE_RESISTANCE_PCT = 142
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_RESISTANCE_EXCLUSIVE = 143
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MECHANIC_IMMUNITY_MASK = 147
- EffectMiscValueA: [Creature Immunity](creature_template)

SPELL_AURA_SPLIT_DAMAGE_FLAT = 153
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_CRIT_DAMAGE_BONUS = 163
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_DAMAGE_DONE_VERSUS = 168
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_MOD_CRIT_PERCENT_VERSUS = 169
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_MOD_SPELL_DAMAGE_OF_STAT_PERCENT = 174
- EffectMiscValueA: [School Mask](#school-mask)
- EffectMiscValueB: [Stats Type](#stats-type)

SPELL_AURA_MOD_SPELL_HEALING_OF_STAT_PERCENT = 175
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_MOD_DEBUFF_RESISTANCE = 178
- EffectMiscValueA: [Dispel Type](#dispel-type)

SPELL_AURA_MOD_ATTACKER_SPELL_CRIT_CHANCE = 179
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_FLAT_SPELL_DAMAGE_VERSUS = 180
- EffectMiscValueA: [Creature Type](#creature-type)

SPELL_AURA_MOD_CRITICAL_THREAT = 183
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_ATTACKER_SPELL_HIT_CHANCE = 186
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_RATING = 189
- EffectMiscValueA: Rating Type

SPELL_AURA_MOD_FACTION_REPUTATION_GAIN = 190
- EffectMiscValueA: ID from [faction.dbc](faction)

SPELL_AURA_MOD_TARGET_ABSORB_SCHOOL = 194
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_TARGET_ABILITY_ABSORB_SCHOOL = 195
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_INCREASES_SPELL_PCT_TO_HIT = 199
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_SCHOOL_CRIT_DMG_TAKEN = 205
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_RANGED_ATTACK_POWER_OF_STAT_PERCENT = 212
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_MOD_MANA_REGEN_FROM_STAT = 219
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_MOD_RATING_FROM_STAT = 220
- EffectMiscValueA: Rating Type

SPELL_AURA_MOD_AOE_DAMAGE_AVOIDANCE = 229
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MECHANIC_DURATION_MOD = 232
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_CHANGE_MODEL_FOR_ALL_HUMANOIDS = 233
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_AURA_MECHANIC_DURATION_MOD_NOT_STACK = 234
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_MOD_FACTION = 243
- EffectMiscValueA: ID from [faction.dbc](faction)

SPELL_AURA_COMPREHEND_LANGUAGE = 244
- EffectMiscValueA: [Language ID](languages)

SPELL_AURA_MOD_AURA_DURATION_BY_DISPEL = 245
- EffectMiscValueA: [Dispel Type](#dispel-type)

SPELL_AURA_MOD_AURA_DURATION_BY_DISPEL_NOT_STACK = 246
- EffectMiscValueA: [Dispel Type](#dispel-type)

SPELL_AURA_CONVERT_RUNE = 249
- EffectMiscValueA: Rune Type to convert
- EffectMiscValueB: The converted new Rune

SPELL_AURA_MOD_MECHANIC_DAMAGE_TAKEN_PERCENT = 255
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_NO_REAGENT_USE = 256
- EffectMiscValueA: Some sort of a reagent type.

SPELL_AURA_MOD_HOT_PCT = 259
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_SCREEN_EFFECT = 260
- EffectMiscValueA: ID from screen ScreenEffect.dbc

SPELL_AURA_PHASE = 261
- EffectMiscValueA: Phase Mask

SPELL_AURA_MOD_IMMUNE_AURA_APPLY_SCHOOL = 267
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_ATTACK_POWER_OF_STAT_PERCENT = 268
- EffectMiscValueA: [Stats Type](#stats-type)

SPELL_AURA_MOD_IGNORE_TARGET_RESIST = 269
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_ABILITY_IGNORE_TARGET_RESIS
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_DAMAGE_FROM_CASTER = 271
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_X_RAY = 273
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_AURA_MOD_DAMAGE_DONE_FOR_MECHANIC = 276
- EffectMiscValueA: [Spell Mechanic](#spell-mechanic)

SPELL_AURA_OVERRIDE_SPELLS = 293
- EffectMiscValueA: ID from screen OverrideSpellData.dbc

SPELL_AURA_PREVENT_REGENERATE_POWER = 294
- EffectMiscValueA: [Power Type](#power-type)

SPELL_AURA_SET_VEHICLE_ID = 296
- EffectMiscValueA: ID from Vehicle.dbc

SPELL_AURA_SHARE_DAMAGE_PCT = 300
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_SCHOOL_HEAL_ABSORB = 301
- EffectMiscValueA: [School Mask](#school-mask)

SPELL_AURA_MOD_DAMAGE_DONE_VERSUS_AURASTATE = 303
- EffectMiscValueA: ID from AuraStateType (master/src/server/shared/SharedDefines.h)

SPELL_AURA_MOD_FAKE_INEBRIATE = 304
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_AURA_MOD_CREATURE_AOE_DAMAGE_AVOIDANCE = 310
- EffectMiscValueA: [School Mask](#school-mask)

### School Mask

| ID  | School   |
| --- | -------- |
| 1   | Physical |
| 2   | Holy     |
| 4   | Fire     |
| 8   | Nature   |
| 16  | Frost    |
| 32  | Shadow   |
| 64  | Arcane   |
| 127 | All      |

### Invisibility Type

| ID | Type                 |
| -- | -------------------- |
| 0  | INVISIBILITY_GENERAL |
| 1  | INVISIBILITY_UNK1    |
| 2  | INVISIBILITY_UNK2    |
| 3  | INVISIBILITY_TRAP    |
| 4  | INVISIBILITY_UNK4    |
| 5  | INVISIBILITY_UNK5    |
| 6  | INVISIBILITY_DRUNK   |
| 7  | INVISIBILITY_UNK7    |
| 8  | INVISIBILITY_UNK8    |
| 9  | INVISIBILITY_UNK9    |
| 10 | INVISIBILITY_UNK10   |
| 11 | INVISIBILITY_UNK11   |

### Power Type

| ID  | Type       |
| --- | ---------- |
| 0   | Mana       |
| 1   | Rage       |
| 2   | Focus      |
| 3   | Energy     |
| 4   | Happiness  |
| 5   | Rune       |
| 6   | Runic      |
| 7   | Max powers |
| 127 | All powers |
| -2  | HP         |

### Stats Type

| ID | Stat         |
| -- | ------------ |
| 0  | Strength     |
| 1  | Agility      |
| 2  | Stamina      |
| 3  | Intelligence |
| 4  | Spirit       |
| -1 | All          |

### Dispel Type

| ID | Type       | ID | Type         | ID | Type            |
| -- | ---------- | -- | ------------ | -- | --------------- |
| 0  | None       | 4  | Poison       | 8  | SPE_NPC_ONLY    |
| 1  | Magic      | 5  | Stealth      | 9  | Enrage          |
| 2  | Curse      | 6  | Invisibility | 10 | ZG Trinket      |
| 3  | Disease    | 7  | ALL          | 11 | Old Unseen      |

### Creature Type

| ID  | Type           |
| --- | -------------- |
| 0   | None           |
| 1   | Beast          |
| 2   | Dragonkin      |
| 3   | Demon          |
| 4   | Elemental      |
| 5   | Giant          |
| 6   | Undead         |
| 7   | Humanoid       |
| 8   | Critter        |
| 9   | Mechanical     |
| 10  | Not specified  |
| 11  | Totem          |
| 12  | Non-Combat Pet |
| 13  | Gas Cloud      |

### Lock Type

| ID | Type                          |
| -- | ----------------------------- |
| 1  | LOCKTYPE_PICKLOCK             |
| 2  | LOCKTYPE_HERBALISM            |
| 3  | LOCKTYPE_MINING               |
| 4  | LOCKTYPE_DISARM_TRAP          |
| 5  | LOCKTYPE_OPEN                 |
| 6  | LOCKTYPE_TREASURE             |
| 7  | LOCKTYPE_CALCIFIED_ELVEN_GEMS |
| 8  | LOCKTYPE_CLOSE                |
| 9  | LOCKTYPE_ARM_TRAP             |
| 10 | LOCKTYPE_QUICK_OPEN           |
| 11 | LOCKTYPE_QUICK_CLOSE          |
| 12 | LOCKTYPE_OPEN_TINKERING       |
| 13 | LOCKTYPE_OPEN_KNEELING        |
| 14 | LOCKTYPE_OPEN_ATTACKING       |
| 15 | LOCKTYPE_GAHZRIDIAN           |
| 16 | LOCKTYPE_BLASTING             |
| 17 | LOCKTYPE_SLOW_OPEN            |
| 18 | LOCKTYPE_SLOW_CLOSE           |
| 19 | LOCKTYPE_FISHING              |
| 20 | LOCKTYPE_INSCRIPTION          |
| 21 | LOCKTYPE_OPEN_FROM_VEHICLE    |

### Spell Mechanic

| ID | Mechanic   | ID | Mechanic   | ID | Mechanic        |
| -- | ---------- | -- | ---------- | -- | --------------- |
| 0  | None       | 11 | Snare      | 22 | Infected        |
| 1  | Charm      | 12 | Stun       | 23 | Turn            |
| 2  | Disorient  | 13 | Freeze     | 24 | Horror          |
| 3  | Disarm     | 14 | Knockout   | 25 | Invulnerability |
| 4  | Distract   | 15 | Bleed      | 26 | Interrupt       |
| 5  | Fear       | 16 | Bandage    | 27 | Daze            |
| 6  | Grip       | 17 | Polymorph  | 28 | Discovery       |
| 7  | Root       | 18 | Banish     | 29 | immunity shield |
| 8  | Slow       | 19 | Shield     | 30 | All powers      |
| 9  | Silence    | 20 | Shackle    | 31 | Sap             |
| 10 | Sleep      | 21 | Mount      | 31 | Enrage          |

### Modifier Type

| ID | Modifier    | ID | Modifier           | ID | Modifier                 |
| -- | ----------- | -- | ------------------ | -- | ------------------------ |
| 0  | damage      | 11 | CD                 | 22 | DoT                      |
| 1  | duration    | 12 | effect2            | 23 | effect3                  |
| 2  | threat      | 13 | ignore armor       | 24 | bonus multiplier         |
| 3  | effect1     | 14 | cost               | 25 | ---                      |
| 4  | charges     | 15 | crit damage bonus  | 26 | PPM                      |
| 5  | range       | 16 | resist miss chance | 27 | value multipler          |
| 6  | radius      | 17 | jump targets       | 28 | resist dispel chance     |
| 7  | crit chance | 18 | Chance of success  | 29 | crit damage bonus 2      |
| 8  | all effects | 19 | Amplitude          | 30 | pell cost refund on fail |
| 9  | No pushback | 20 | Dmg multiplier     |
| 10 | Cast Time   | 21 | GCD                |
