---
redirect_from: "/Spell-Effects-Reference"
---

[<-Back-to:spell_dbc](spell_dbc.md)

## Related Information

SPELL_EFFECT_SUMMON (28)
- EffectMiscValueB: [Summon Properties](dbc-summon-properties.md)

SPELL_EFFECT_APPLY_AURA (6)
- EffectAura: [Spell Aura](spell-aura-reference.md)

# Spell Effects Reference

SPELL_EFFECT_INSTAKILL = 1

SPELL_EFFECT_SCHOOL_DAMAGE = 2
- BasePoints: Base damage
- Multiple: Damage multiplier

SPELL_EFFECT_DUMMY = 3
- BasePoints: Anything

SPELL_EFFECT_PORTAL_TELEPORT = 4

SPELL_EFFECT_TELEPORT_UNITS = 5
- TargetB: teleport location

SPELL_EFFECT_APPLY_AURA = 6
- BasePoints: Value of aura (depends on Aura ID)
- EffectAura: [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_ENVIRONMENTAL_DAMAGE = 7
- BasePoints: Base damage

SPELL_EFFECT_POWER_DRAIN = 8
- BasePoints: Base drain
- Multiple: Drain multiplier

SPELL_EFFECT_HEALTH_LEECH = 9
- BasePoints: Base drain 
- Multiple: Drain multiplier
- TargetB: If used, TargetA is healed

SPELL_EFFECT_HEAL = 10
- BasePoints: Base heal
- Multiple: Heal multiplier
- TargetB: If used, TargetA is healed

SPELL_EFFECT_BIND = 11
- BasePoints: Unknown
- EffectMiscValueA: Area ID (Death Gate only)

SPELL_EFFECT_PORTAL = 12
- TargetA: Teleport Destination
- TargetB: Targets

SPELL_EFFECT_RITUAL_BASE = 13 // Unused

SPELL_EFFECT_RITUAL_SPECIALIZE = 14 // Unused

SPELL_EFFECT_RITUAL_ACTIVATE_PORTAL = 15 // Unused

SPELL_EFFECT_QUEST_COMPLETE = 16
- EffectMiscValueA: Quest ID
- TargetB: Additional Targets (Used by 30790)

SPELL_EFFECT_WEAPON_DAMAGE_NOSCHOOL = 17
- BasePoints: Base damage

SPELL_EFFECT_RESURRECT = 18
- BasePoints: Percentage (%) of restored health and mana
- TargetB: Additional Targets (Used by 29820, mass revive)

SPELL_EFFECT_ADD_EXTRA_ATTACKS = 19
- BasePoints: Number of extra melee attacks

SPELL_EFFECT_DODGE = 20

SPELL_EFFECT_EVADE = 21

SPELL_EFFECT_PARRY = 22

SPELL_EFFECT_BLOCK = 23

SPELL_EFFECT_CREATE_ITEM = 24
- BasePoints: Number of items
- EffectItemType: Item ID

SPELL_EFFECT_WEAPON = 25

SPELL_EFFECT_DEFENSE = 26

SPELL_EFFECT_PERSISTENT_AREA_AURA = 27
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_SUMMON = 28
- BasePoints: Number of summons
- EffectMiscValueA: Creature ID
- EffectMiscValueB: [Summon Properties](dbc-summon-properties.md)
- Radius: Spawn range

SPELL_EFFECT_LEAP = 29
- TargetA: Target
- TargetB: Destination
- Radius: Blink/leap distance

SPELL_EFFECT_ENERGIZE = 30
- BasePoints: Amount
- TargetB: Additional Targets
- EffectMiscValueA: Power Type

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

SPELL_EFFECT_WEAPON_PERCENT_DAMAGE = 31
- BasePoints: Percentage base damage

SPELL_EFFECT_TRIGGER_MISSILE = 32
- TriggerSpell: Spell ID

SPELL_EFFECT_OPEN_LOCK = 33
- BasePoints: Required lockpicking skill level

SPELL_EFFECT_SUMMON_CHANGE_ITEM = 34 // Weapons like Benedictions
EffectItemType: New ItemID

SPELL_EFFECT_APPLY_AREA_AURA_PARTY = 35
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_LEARN_SPELL = 36
- TriggerSpell: Spell ID

SPELL_EFFECT_SPELL_DEFENSE = 37

SPELL_EFFECT_DISPEL = 38
- BasePoints: Number of spells to dispell
- EffectMiscValueA: Dispel Type

| ID | Type       | ID | Type         | ID | Type            |
| -- | ---------- | -- | ------------ | -- | --------------- |
| 0  | None       | 4  | Poison       | 8  | SPE_NPC_ONLY    |
| 1  | Magic      | 5  | Stealth      | 9  | Enrage          |
| 2  | Curse      | 6  | Invisibility | 10 | ZG Trinket      |
| 3  | Disease    | 7  | ALL          | 11 | Old Unseen      |

SPELL_EFFECT_LANGUAGE = 39
- EffectMiscValueA: [Language ID](languages.md)

SPELL_EFFECT_DUAL_WIELD = 40

SPELL_EFFECT_JUMP = 41
- Multiple: Unknown
- EffectMiscValueA: Speed XY or speed Z
- EffectMiscValueB: Speed XY or speed Z

SPELL_EFFECT_JUMP_DEST = 42
- Multiple: Unknown
- EffectMiscValueA: Speed XY or speed Z
- EffectMiscValueB: Speed XY or speed Z

SPELL_EFFECT_TELEPORT_UNITS_FACE_CASTER = 43
- BasePoints: Number of units to teleport

SPELL_EFFECT_SKILL_STEP = 44
- BasePoints: Unknown
- EffectMiscValueA: [Skill ID](skillline.md)

SPELL_EFFECT_ADD_HONOR = 45
- BasePoints: Honor points to reward

SPELL_EFFECT_SPAWN = 46

SPELL_EFFECT_TRADE_SKILL = 47

SPELL_EFFECT_STEALTH = 48

SPELL_EFFECT_DETECT = 49

SPELL_EFFECT_TRANS_DOOR = 50
- EffectMiscValueA: gameobject_template ID
- gameobject_template's Data0 is the spell that is linked to the destination of the teleport when clicked.
- Data0 entry = spell_target_position table

SPELL_EFFECT_FORCE_CRITICAL_HIT = 51 // Unused

SPELL_EFFECT_GUARANTEE_HIT = 52 // Unused

SPELL_EFFECT_ENCHANT_ITEM = 53
- EffectItemType: Item ID (Scrolls/Inscription)
- EffectMiscValueA: ID from SpellItemEnchantment.dbc
- EffectMiscValueA: 14 = armor, 15 = weapon, tied to EffectItemType.

SPELL_EFFECT_ENCHANT_ITEM_TEMPORARY = 54
- EffectMiscValueA: ID from SpellItemEnchantment.dbc

SPELL_EFFECT_TAMECREATURE = 55

SPELL_EFFECT_SUMMON_PET = 56
- Multiple: Relative to Caster level (e.g a value of -3 will be caster level -3) Does not currently work.
- EffectMiscValueA: Creature ID

SPELL_EFFECT_LEARN_PET_SPELL = 57
- TriggerSpell: Spell ID

SPELL_EFFECT_WEAPON_DAMAGE = 58
- BasePoints: Additional damage
- TargetB: Additional Targets
- Chain Target: Additional Targets

SPELL_EFFECT_CREATE_RANDOM_ITEM = 59
- EffectMiscValueA: Unknown

SPELL_EFFECT_PROFICIENCY = 60

SPELL_EFFECT_SEND_EVENT = 61
- EffectMiscValueA: Calls for an event from acevent_scripts table.\
(Most are missmatched, but there are few that are correct.)

SPELL_EFFECT_POWER_BURN = 62
- BasePoints: Amount of mana to burn
- TargetB: Additional Targets
- Multiple: conversion % to dmg (e.g if 0.5, for 1 mana burned, deal 0.5 damage)
- Chain Target: Additional Targets

SPELL_EFFECT_THREAT = 63
- BasePoints: Amount of threat to add/remove

SPELL_EFFECT_TRIGGER_SPELL = 64
- TriggerSpell: Spell ID

SPELL_EFFECT_APPLY_AREA_AURA_RAID = 65
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)
- EffectMiscValueA: Unknown

SPELL_EFFECT_CREATE_MANA_GEM = 66
- BasePoints: Number to refill
- EffectItemType: Item to create/refill

SPELL_EFFECT_HEAL_MAX_HEALTH = 67

SPELL_EFFECT_INTERRUPT_CAST = 68
- EffectMechanic: Interupted

SPELL_EFFECT_DISTRACT = 69
- BasePoints: Duration in seconds.

SPELL_EFFECT_PULL = 70

SPELL_EFFECT_PICKPOCKET = 71

SPELL_EFFECT_ADD_FARSIGHT = 72

SPELL_EFFECT_UNTRAIN_TALENTS = 73

SPELL_EFFECT_APPLY_GLYPH = 74
- EffectMiscValueA: ID from GlyphProperties.dbc

SPELL_EFFECT_HEAL_MECHANICAL = 75
- BasePoints: Amount

SPELL_EFFECT_SUMMON_OBJECT_WILD = 76
- EffectMiscValueA: gameobject_template ID

SPELL_EFFECT_SCRIPT_EFFECT = 77 Assigned to a [Core Script](/wiki/core-scripts#spell-scripts) in the DB.

SPELL_EFFECT_ATTACK = 78

SPELL_EFFECT_SANCTUARY = 79

SPELL_EFFECT_ADD_COMBO_POINTS = 80
- BasePoints: Number of combo points to add

SPELL_EFFECT_CREATE_HOUSE = 81

SPELL_EFFECT_BIND_SIGHT = 82

SPELL_EFFECT_DUEL = 83
- EffectMiscValueA: gameobject_template ID (Duel Flag)

SPELL_EFFECT_STUCK = 84

SPELL_EFFECT_SUMMON_PLAYER = 85

SPELL_EFFECT_ACTIVATE_OBJECT = 86
- EffectMiscValueA: Unknown

SPELL_EFFECT_GAMEOBJECT_DAMAGE = 87
- BasePoints: Base damage

SPELL_EFFECT_GAMEOBJECT_REPAIR = 88

SPELL_EFFECT_GAMEOBJECT_SET_DESTRUCTION_STATE = 89
- EffectMiscValueA: State

| ID | State       |
| -- | ---------- |
| 0  | Intact     |
| 1  | Damaged    |
| 2  | Destroyed  |
| 3  | Rebuilding |

SPELL_EFFECT_KILL_CREDIT = 90
- EffectMiscValueA: Creature ID

SPELL_EFFECT_THREAT_ALL = 91 // Unused

SPELL_EFFECT_ENCHANT_HELD_ITEM = 92
- EffectMiscValueA: ID from SpellItemEnchantment.dbc

SPELL_EFFECT_FORCE_DESELECT = 93

SPELL_EFFECT_SELF_RESURRECT = 94
- BasePoints: Positive = %, Negative = Flat Value
- EffectMiscValueA: Mana (Flat Value)

SPELL_EFFECT_SKINNING = 95

SPELL_EFFECT_CHARGE = 96

SPELL_EFFECT_CAST_BUTTON = 97 (Totem bar since 3.2.2a)
- EffectMiscValueA: Totem combinations = 0,4,8
- EffectMiscValueB: Unknown (Always 4), possibly totem amount

SPELL_EFFECT_KNOCK_BACK = 98
- BasePoints: Distance
- EffectMiscValueA: Distance

SPELL_EFFECT_DISENCHANT = 99

SPELL_EFFECT_INEBRIATE = 100
- BasePoints: Drunk power

SPELL_EFFECT_FEED_PET = 101
- BasePoints: Happiness Amount
- TriggerSpell: Spell ID

SPELL_EFFECT_DISMISS_PET = 102

SPELL_EFFECT_REPUTATION = 103
- BasePoints: Reputation  Amount
- EffectMiscValueA: ID from [faction.dbc](faction.md)

SPELL_EFFECT_SUMMON_OBJECT_SLOT1 = 104
- EffectMiscValueA: gameobject_template ID 

SPELL_EFFECT_SUMMON_OBJECT_SLOT2 = 105
- EffectMiscValueA: gameobject_template ID 

SPELL_EFFECT_SUMMON_OBJECT_SLOT3 = 106
- EffectMiscValueA: gameobject_template ID 

SPELL_EFFECT_SUMMON_OBJECT_SLOT4 = 107 // Unused

SPELL_EFFECT_DISPEL_MECHANIC = 108
- EffectMiscValueA: Dispel Type

| ID | Type       | ID | Type       | ID | Type            |
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

SPELL_EFFECT_RESURRECT_PET = 109
- BasePoints: % base health to heal

SPELL_EFFECT_DESTROY_ALL_TOTEMS = 110
- BasePoints: % mana refund

SPELL_EFFECT_DURABILITY_DAMAGE = 111
- BasePoints: Positive = Durability damage, Negative = Durability restore
- EffectMiscValueA: Unknown

SPELL_EFFECT_112 = 112 // Unused

SPELL_EFFECT_RESURRECT_NEW = 113
- BasePoints: Health to restore (Flat Value)
- EffectMiscValueA: Mana (Flat Value)

SPELL_EFFECT_ATTACK_ME = 114

SPELL_EFFECT_DURABILITY_DAMAGE_PCT = 115
- BasePoints: Durability damage %
- EffectMiscValueA: Unknown

SPELL_EFFECT_SKIN_PLAYER_CORPSE = 116

SPELL_EFFECT_SPIRIT_HEAL = 117
- BasePoints: Health %

SPELL_EFFECT_SKILL = 118
- BasePoints: Unknown
- EffectMiscValueA: [Skill ID](skillline.md)

SPELL_EFFECT_APPLY_AREA_AURA_PET = 119
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_TELEPORT_GRAVEYARD = 120

SPELL_EFFECT_NORMALIZED_WEAPON_DMG = 121
- BasePoints: Base damage
- Chain Target: Additional Targets

SPELL_EFFECT_122 = 122 // Unused

SPELL_EFFECT_SEND_TAXI = 123
- EffectMiscValueA: ID from TaxiPath.dbc

SPELL_EFFECT_PULL_TOWARDS = 124
- EffectMiscValueA: Speed of pull

SPELL_EFFECT_MODIFY_THREAT_PERCENT = 125
- BasePoints: Threat %

SPELL_EFFECT_STEAL_BENEFICIAL_BUFF = 126
- BasePoints: Number of buffs to steal

SPELL_EFFECT_PROSPECTING = 127

SPELL_EFFECT_APPLY_AREA_AURA_FRIEND = 128
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_APPLY_AREA_AURA_ENEMY = 129
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_REDIRECT_THREAT = 130
- BasePoints: % Threat to redirect
- TargetB: Unit to redirect threat to 

SPELL_EFFECT_PLAY_SOUND = 131
- EffectMiscValueA: ID from SoundEntries.dbc

SPELL_EFFECT_PLAY_MUSIC = 132
- EffectMiscValueA: ID from SoundEntries.dbc

SPELL_EFFECT_UNLEARN_SPECIALIZATION = 133
- TriggerSpell: Spell ID

SPELL_EFFECT_KILL_CREDIT2 = 134
- EffectMiscValueA: Creature ID

SPELL_EFFECT_CALL_PET = 135

SPELL_EFFECT_HEAL_PCT = 136
- BasePoints: % Heal

SPELL_EFFECT_ENERGIZE_PCT = 137
- BasePoints: % to restore
- EffectMiscValueA: Power Type (Same as EFFECT 30)

SPELL_EFFECT_LEAP_BACK = 138
- BasePoints: Distance
- EffectMiscValueA: Distance

SPELL_EFFECT_CLEAR_QUEST = 139
- BasePoints: 2nd quest ID to clear (e.g Spell ID 56518)
- EffectMiscValueA: Quest ID

SPELL_EFFECT_FORCE_CAST = 140
- TriggerSpell: Spell ID

SPELL_EFFECT_FORCE_CAST_WITH_VALUE = 141
- BasePoints: Value for the TriggerSpell 
- TriggerSpell: Spell ID

SPELL_EFFECT_TRIGGER_SPELL_WITH_VALUE = 142
- BasePoints: Value for the TriggerSpell 
- TriggerSpell: Spell ID

SPELL_EFFECT_APPLY_AREA_AURA_OWNER = 143
- BasePoints: Depends on [Spell Aura](spell-aura-reference.md)

SPELL_EFFECT_KNOCK_BACK_DEST = 144
- BasePoints: Distance
- TargetB: Destionation
- EffectMiscValueA: Distance

SPELL_EFFECT_PULL_TOWARDS_DEST = 145 (Black Hole Effect)
- EffectMiscValueA: Distance

SPELL_EFFECT_ACTIVATE_RUNE = 146
- BasePoints: Number of runes to activate (1 or 2)
- EffectMiscValueA: Rune Type

SPELL_EFFECT_QUEST_FAIL = 147
- EffectMiscValueA: Quest ID

SPELL_EFFECT_TRIGGER_MISSILE_SPELL_WITH_VALUE = 148
- BasePoints: Value
- TriggerSpell: Spell ID

SPELL_EFFECT_CHARGE_DEST = 149

SPELL_EFFECT_QUEST_START = 150
- EffectMiscValueA: Quest ID

SPELL_EFFECT_TRIGGER_SPELL_2 = 151
- TriggerSpell: Spell ID

SPELL_EFFECT_SUMMON_RAF_FRIEND = 152
- TriggerSpell: Spell ID (Summon)

SPELL_EFFECT_CREATE_TAMED_PET = 153
- EffectMiscValueA: Creature ID

SPELL_EFFECT_DISCOVER_TAXI = 154
- EffectMiscValueA: ID from TaxiNodes.dbc

SPELL_EFFECT_TITAN_GRIP = 155
- EffectMiscValueA: Spell ID

SPELL_EFFECT_ENCHANT_ITEM_PRISMATIC = 156

SPELL_EFFECT_CREATE_ITEM_2 = 157
- EffectItemType: Item ID to transform
- EffectMiscValueA: Unknown

SPELL_EFFECT_MILLING = 158
- BasePoints: Number of herbs to mill.

SPELL_EFFECT_ALLOW_RENAME_PET = 159

SPELL_EFFECT_160 = 160

SPELL_EFFECT_TALENT_SPEC_COUNT = 161
- BasePoints: Number of active talent specs

SPELL_EFFECT_TALENT_SPEC_SELECT = 162
- BasePoints: Talent spec ID to activate

SPELL_EFFECT_163 = 163 // Unused

SPELL_EFFECT_REMOVE_AURA = 164
- BasePoints:  Spell ID to remove 2
- TriggerSpell: Spell ID to remove
