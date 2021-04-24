# spell\_dbc

[<-Back-to:World](database-world.md)

**The \`spell\_dbc\` table**

This table contains data regarding serverside spells which are not to be found in Client DBC files as well as **overrides** of the DBC that are meant to improve or fix any spell.

If you want to add more overrides, please first extract the needed SQL spell row using the [node-dbc-reader](https://github.com/wowgaming/node-dbc-reader) then you can use a `UPDATE` query to change the fields that you need to override.

Fixes for this table should always contain:

1) the `INSERT IGNORE` query adding the original spell from the DBC
2) the `UPDATE` query containing the desired overrides

**Structure**

| Field                         | Type        | Attributes | Key | Null | Default | Extra | Comment |
|-------------------------------|-------------|------------|-----|------|---------|-------|---------|
| Id                            | int(10)     | unsigned   | PRI | NO   | NULL    |       |         |
| Dispel                        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| Mechanic                      | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| Attributes                    | int(10)     | unsigned   |     | NO   | 0       |       |         |
| AttributesEx                  | int(10)     | unsigned   |     | NO   | 0       |       |         |
| AttributesEx2                 | int(10)     | unsigned   |     | NO   | 0       |       |         |
| AttributesEx3                 | int(10)     | unsigned   |     | NO   | 0       |       |         |
| AttributesEx4                 | int(10)     | unsigned   |     | NO   | 0       |       |         |
| AttributesEx5                 | int(10)     | unsigned   |     | NO   | 0       |       |         |
| Stances                       | int(10)     | unsigned   |     | NO   | 0       |       |         |
| StancesNot                    | int(10)     | unsigned   |     | NO   | 0       |       |         |
| Targets                       | int(10)     | unsigned   |     | NO   | 0       |       |         |
| CastingTimeIndex              | tinyint(3)  | unsigned   |     | NO   | 1       |       |         |
| AuraInterruptFlags            | int(10)     | unsigned   |     | NO   | 0       |       |         |
| ProcFlags                     | int(10)     | unsigned   |     | NO   | 0       |       |         |
| ProcChance                    | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| ProcCharges                   | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| MaxLevel                      | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| BaseLevel                     | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| SpellLevel                    | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| DurationIndex                 | smallint(5) | unsigned   |     | NO   | 0       |       |         |
| RangeIndex                    | tinyint(3)  | unsigned   |     | NO   | 1       |       |         |
| StackAmount                   | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EquippedItemClass             | int(11)     | signed     |     | NO   | -1      |       |         |
| EquippedItemSubClassMask      | int(11)     | signed     |     | NO   | 0       |       |         |
| EquippedItemInventoryTypeMask | int(11)     | signed     |     | NO   | 0       |       |         |
| Effect1                       | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| Effect2                       | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| Effect3                       | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectDieSides1               | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectDieSides2               | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectDieSides3               | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel1     | float       | signed     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel2     | float       | signed     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel3     | float       | signed     |     | NO   | 0       |       |         |
| EffectBasePoints1             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectBasePoints2             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectBasePoints3             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMechanic1               | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectMechanic2               | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectMechanic3               | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetA1        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetA2        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetA3        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetB1        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetB2        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectImplicitTargetB3        | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectRadiusIndex1            | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectRadiusIndex2            | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectRadiusIndex3            | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| EffectApplyAuraName1          | smallint(5) | unsigned   |     | NO   | 0       |       |         |
| EffectApplyAuraName2          | smallint(5) | unsigned   |     | NO   | 0       |       |         |
| EffectApplyAuraName3          | smallint(5) | unsigned   |     | NO   | 0       |       |         |
| EffectAmplitude1              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectAmplitude2              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectAmplitude3              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMultipleValue1          | float       | signed     |     | NO   | 0       |       |         |
| EffectMultipleValue2          | float       | signed     |     | NO   | 0       |       |         |
| EffectMultipleValue3          | float       | signed     |     | NO   | 0       |       |         |
| EffectMiscValue1              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMiscValue2              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMiscValue3              | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMiscValueB1             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMiscValueB2             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectMiscValueB3             | int(11)     | signed     |     | NO   | 0       |       |         |
| EffectTriggerSpell1           | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectTriggerSpell2           | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectTriggerSpell3           | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA1        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA2        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA3        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB1        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB2        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB3        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC1        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC2        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC3        | int(10)     | unsigned   |     | NO   | 0       |       |         |
| MaxTargetLevel                | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| SpellFamilyName               | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| SpellFamilyFlags1             | int(10)     | unsigned   |     | NO   | 0       |       |         |
| SpellFamilyFlags2             | int(10)     | unsigned   |     | NO   | 0       |       |         |
| SpellFamilyFlags3             | int(10)     | unsigned   |     | NO   | 0       |       |         |
| MaxAffectedTargets            | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| DmgClass                      | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| PreventionType                | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| DmgMultiplier1                | float       | signed     |     | NO   | 0       |       |         |
| DmgMultiplier2                | float       | signed     |     | NO   | 0       |       |         |
| DmgMultiplier3                | float       | signed     |     | NO   | 0       |       |         |
| AreaGroupId                   | int(11)     | signed     |     | NO   | 0       |       |         |
| SchoolMask                    | int(10)     | unsigned   |     | NO   | 0       |       |         |
| Comment                       | text        | signed     |     | NO   | NULL    |       |         |

**Description of the fields**

### Id

The id of the Spell.

### Dispel

`field-no-description|2`

### Mechanic

`field-no-description|3`

### Attributes

`field-no-description|4`

### AttributesEx

`field-no-description|5`

### Stances

`field-no-description|6`

### StancesNot

`field-no-description|7`

### Targets

`field-no-description|8`

### CastingTimeIndex

`field-no-description|9`

### AuraInterruptFlags

`field-no-description|10`

### ProcFlags

`field-no-description|11`

### ProcChance

`field-no-description|12`

### ProcCharges

`field-no-description|13`

### MaxLevel

`field-no-description|14`

### BaseLevel

`field-no-description|15`

### SpellLevel

`field-no-description|16`

### DurationIndex

`field-no-description|17`

### RangeIndex

`field-no-description|18`

### StackAmount

`field-no-description|19`

### EquippedItemClass

`field-no-description|20`

### EquippedItemSubClassMask

`field-no-description|21`

### EquippedItemInventoryTypeMask

`field-no-description|22`

### Effect

Effect1, Effect2 and Effect3. Effect\_ID of the Spell\_Effect. A Spell can only have up to three Spell\_Effects.

### EffectDieSides

`field-no-description|24`

### EffectRealPointsPerLevel

`field-no-description|25`

### EffectBasePoints

`field-no-description|26`

### EffectMechanic

`field-no-description|27`

### EffectImplicitTargetA

`field-no-description|28`

### EffectImplicitTargetB

`field-no-description|29`

### EffectRadiusIndex

`field-no-description|30`

### EffectApplyAuraName

`field-no-description|31`

### EffectAmplitude

`field-no-description|32`

### EffectMultipleValue

`field-no-description|33`

### EffectMiscValue

`field-no-description|34`

### EffectMiscValueB

`field-no-description|35`

### EffectTriggerSpell

`field-no-description|36`

### EffectSpellClassMaskA

`field-no-description|37`

### EffectSpellClassMaskB

`field-no-description|38`

### EffectSpellClassMaskC

`field-no-description|39`

### MaxTargetLevel

`field-no-description|40`

### SpellFamilyName

`field-no-description|41`

### SpellFamilyFlags

`field-no-description|42`

### MaxAffectedTarget

`field-no-description|43`

### DmgClass

`field-no-description|44`

### PreventionType

`field-no-description|45`

### DmgMultiplier

`field-no-description|46`

### AreaGroupId

`field-no-description|47`

### SchoolMask

`field-no-description|48`

### Comment

`field-no-description|49`

**SPELL\_EFFECT\_ID**

Effect\_IDs of [Effect1, Effect2 and/or Effect3](#spell_dbc-Effect).

| Effect_ID | Spell_Effect                   | Description                                                                                                                             |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0         | EffectNULL                     | NULL                                                                                                                                    |
| 1         | EffectInstaKill                | SPELL_EFFECT_INSTAKILL                                                                                                                  |
| 2         | EffectSchoolDMG                | SPELL_EFFECT_SCHOOL_DAMAGE                                                                                                              |
| 3         | EffectDummy                    | SPELL_EFFECT_DUMMY                                                                                                                      |
| 4         | EffectUnused                   | SPELL_EFFECT_PORTAL_TELEPORT unused                                                                                                     |
| 5         | EffectTeleportUnits            | SPELL_EFFECT_TELEPORT_UNITS                                                                                                             |
| 6         | EffectApplyAura                | SPELL_EFFECT_APPLY_AURA                                                                                                                 |
| 7         | EffectEnvirinmentalDMG         | SPELL_EFFECT_ENVIRONMENTAL_DAMAGE                                                                                                       |
| 8         | EffectPowerDrain               | SPELL_EFFECT_POWER_DRAIN                                                                                                                |
| 9         | EffectHealthLeech              | SPELL_EFFECT_HEALTH_LEECH                                                                                                               |
| 10        | EffectHeal                     | SPELL_EFFECT_HEAL                                                                                                                       |
| 11        | EffectBind                     | SPELL_EFFECT_BIND                                                                                                                       |
| 12        | EffectNULL                     | SPELL_EFFECT_PORTAL                                                                                                                     |
| 13        | EffectUnused                   | SPELL_EFFECT_RITUAL_BASE unused                                                                                                         |
| 14        | EffectUnused                   | SPELL_EFFECT_RITUAL_SPECIALIZE unused                                                                                                   |
| 15        | EffectUnused                   | SPELL_EFFECT_RITUAL_ACTIVATE_PORTAL unused                                                                                              |
| 16        | EffectQuestComplete            | SPELL_EFFECT_QUEST_COMPLETE                                                                                                             |
| 17        | EffectWeaponDmg                | SPELL_EFFECT_WEAPON_DAMAGE_NOSCHOOL                                                                                                     |
| 18        | EffectResurrect                | SPELL_EFFECT_RESURRECT                                                                                                                  |
| 19        | EffectAddExtraAttacks          | SPELL_EFFECT_ADD_EXTRA_ATTACKS                                                                                                          |
| 20        | EffectUnused                   | SPELL_EFFECT_DODGE one spell: Dodge                                                                                                     |
| 21        | EffectUnused                   | SPELL_EFFECT_EVADE one spell: Evade (DND)                                                                                               |
| 22        | EffectParry                    | SPELL_EFFECT_PARRY                                                                                                                      |
| 23        | EffectBlock                    | SPELL_EFFECT_BLOCK one spell: Block                                                                                                     |
| 24        | EffectCreateItem               | SPELL_EFFECT_CREATE_ITEM                                                                                                                |
| 25        | EffectUnused                   | SPELL_EFFECT_WEAPON                                                                                                                     |
| 26        | EffectUnused                   | SPELL_EFFECT_DEFENSE one spell: Defense                                                                                                 |
| 27        | EffectPersistentAA             | SPELL_EFFECT_PERSISTENT_AREA_AURA                                                                                                       |
| 28        | EffectSummonType               | SPELL_EFFECT_SUMMON                                                                                                                     |
| 29        | EffectLeap                     | SPELL_EFFECT_LEAP                                                                                                                       |
| 30        | EffectEnergize                 | SPELL_EFFECT_ENERGIZE                                                                                                                   |
| 31        | EffectWeaponDmg                | SPELL_EFFECT_WEAPON_PERCENT_DAMAGE                                                                                                      |
| 32        | EffectTriggerMissileSpell      | SPELL_EFFECT_TRIGGER_MISSILE                                                                                                            |
| 33        | EffectOpenLock                 | SPELL_EFFECT_OPEN_LOCK                                                                                                                  |
| 34        | EffectSummonChangeItem         | SPELL_EFFECT_SUMMON_CHANGE_ITEM                                                                                                         |
| 35        | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_PARTY                                                                                                      |
| 36        | EffectLearnSpell               | SPELL_EFFECT_LEARN_SPELL                                                                                                                |
| 37        | EffectUnused                   | SPELL_EFFECT_SPELL_DEFENSE one spell: SPELLDEFENSE (DND)                                                                                |
| 38        | EffectDispel                   | SPELL_EFFECT_DISPEL                                                                                                                     |
| 39        | EffectUnused                   | SPELL_EFFECT_LANGUAGE                                                                                                                   |
| 40        | EffectDualWield                | SPELL_EFFECT_DUAL_WIELD                                                                                                                 |
| 41        | EffectJump                     | SPELL_EFFECT_JUMP                                                                                                                       |
| 42        | EffectJumpDest                 | SPELL_EFFECT_JUMP_DEST                                                                                                                  |
| 43        | EffectTeleUnitsFaceCaster      | SPELL_EFFECT_TELEPORT_UNITS_FACE_CASTER                                                                                                 |
| 44        | EffectLearnSkill               | SPELL_EFFECT_SKILL_STEP                                                                                                                 |
| 45        | EffectAddHonor                 | SPELL_EFFECT_ADD_HONOR                                                                                                                  |
| 46        | EffectUnused                   | SPELL_EFFECT_SPAWN clientside, unit appears as if it was just spawned                                                                   |
| 47        | EffectTradeSkill               | SPELL_EFFECT_TRADE_SKILL                                                                                                                |
| 48        | EffectUnused                   | SPELL_EFFECT_STEALTH one spell: Base Stealth                                                                                            |
| 49        | EffectUnused                   | SPELL_EFFECT_DETECT one spell: Detect                                                                                                   |
| 50        | EffectTransmitted              | SPELL_EFFECT_TRANS_DOOR                                                                                                                 |
| 51        | EffectUnused                   | SPELL_EFFECT_FORCE_CRITICAL_HIT unused                                                                                                  |
| 52        | EffectUnused                   | SPELL_EFFECT_GUARANTEE_HIT one spell: zzOLDCritical Shot                                                                                |
| 53        | EffectEnchantItemPerm          | SPELL_EFFECT_ENCHANT_ITEM                                                                                                               |
| 54        | EffectEnchantItemTmp           | SPELL_EFFECT_ENCHANT_ITEM_TEMPORARY                                                                                                     |
| 55        | EffectTameCreature             | SPELL_EFFECT_TAMECREATURE                                                                                                               |
| 56        | EffectSummonPet                | SPELL_EFFECT_SUMMON_PET                                                                                                                 |
| 57        | EffectLearnPetSpell            | SPELL_EFFECT_LEARN_PET_SPELL                                                                                                            |
| 58        | EffectWeaponDmg                | SPELL_EFFECT_WEAPON_DAMAGE                                                                                                              |
| 59        | EffectCreateRandomItem         | SPELL_EFFECT_CREATE_RANDOM_ITEM create item base at spell specific loot                                                                 |
| 60        | EffectProficiency              | SPELL_EFFECT_PROFICIENCY                                                                                                                |
| 61        | EffectSendEvent                | SPELL_EFFECT_SEND_EVENT                                                                                                                 |
| 62        | EffectPowerBurn                | SPELL_EFFECT_POWER_BURN                                                                                                                 |
| 63        | EffectThreat                   | SPELL_EFFECT_THREAT                                                                                                                     |
| 64        | EffectTriggerSpell             | SPELL_EFFECT_TRIGGER_SPELL                                                                                                              |
| 65        | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_RAID                                                                                                       |
| 66        | EffectRechargeManaGem          | SPELL_EFFECT_CREATE_MANA_GEM (possibly recharge it, misc - is item ID)                                                                  |
| 67        | EffectHealMaxHealth            | SPELL_EFFECT_HEAL_MAX_HEALTH                                                                                                            |
| 68        | EffectInterruptCast            | SPELL_EFFECT_INTERRUPT_CAST                                                                                                             |
| 69        | EffectDistract                 | SPELL_EFFECT_DISTRACT                                                                                                                   |
| 70        | EffectPull                     | SPELL_EFFECT_PULL one spell: Distract Move                                                                                              |
| 71        | EffectPickPocket               | SPELL_EFFECT_PICKPOCKET                                                                                                                 |
| 72        | EffectAddFarsight              | SPELL_EFFECT_ADD_FARSIGHT                                                                                                               |
| 73        | EffectUntrainTalents           | SPELL_EFFECT_UNTRAIN_TALENTS                                                                                                            |
| 74        | EffectApplyGlyph               | SPELL_EFFECT_APPLY_GLYPH                                                                                                                |
| 75        | EffectHealMechanical           | SPELL_EFFECT_HEAL_MECHANICAL one spell: Mechanical Patch Kit                                                                            |
| 76        | EffectSummonObjectWild         | SPELL_EFFECT_SUMMON_OBJECT_WILD                                                                                                         |
| 77        | EffectScriptEffect             | SPELL_EFFECT_SCRIPT_EFFECT                                                                                                              |
| 78        | EffectUnused                   | SPELL_EFFECT_ATTACK                                                                                                                     |
| 79        | EffectSanctuary                | SPELL_EFFECT_SANCTUARY                                                                                                                  |
| 80        | EffectAddComboPoints           | SPELL_EFFECT_ADD_COMBO_POINTS                                                                                                           |
| 81        | EffectUnused                   | SPELL_EFFECT_CREATE_HOUSE one spell: Create House (TEST)                                                                                |
| 82        | EffectNULL                     | SPELL_EFFECT_BIND_SIGHT                                                                                                                 |
| 83        | EffectDuel                     | SPELL_EFFECT_DUEL                                                                                                                       |
| 84        | EffectStuck                    | SPELL_EFFECT_STUCK                                                                                                                      |
| 85        | EffectSummonPlayer             | SPELL_EFFECT_SUMMON_PLAYER                                                                                                              |
| 86        | EffectActivateObject           | SPELL_EFFECT_ACTIVATE_OBJECT                                                                                                            |
| 87        | EffectWMODamage                | SPELL_EFFECT_WMO_DAMAGE                                                                                                                 |
| 88        | EffectWMORepair                | SPELL_EFFECT_WMO_REPAIR                                                                                                                 |
| 89        | EffectWMOChange                | SPELL_EFFECT_WMO_CHANGE // 0 intact // 1 damaged // 2 destroyed // 3 rebuilding                                                         |
| 90        | EffectKillCreditPersonal       | SPELL_EFFECT_KILL_CREDIT Kill credit but only for single person                                                                         |
| 91        | EffectUnused                   | SPELL_EFFECT_THREAT_ALL one spell: zzOLDBrainwash                                                                                       |
| 92        | EffectEnchantHeldItem          | SPELL_EFFECT_ENCHANT_HELD_ITEM                                                                                                          |
| 93        | EffectForceDeselect            | SPELL_EFFECT_FORCE_DESELECT                                                                                                             |
| 94        | EffectSelfResurrect            | SPELL_EFFECT_SELF_RESURRECT                                                                                                             |
| 95        | EffectSkinning                 | SPELL_EFFECT_SKINNING                                                                                                                   |
| 96        | EffectCharge                   | SPELL_EFFECT_CHARGE                                                                                                                     |
| 97        | EffectCastButtons              | SPELL_EFFECT_CAST_BUTTON (totem bar since 3.2.2a)                                                                                       |
| 98        | EffectKnockBack                | SPELL_EFFECT_KNOCK_BACK                                                                                                                 |
| 99        | EffectDisEnchant               | SPELL_EFFECT_DISENCHANT                                                                                                                 |
| 100       | EffectInebriate                | SPELL_EFFECT_INEBRIATE                                                                                                                  |
| 101       | EffectFeedPet                  | SPELL_EFFECT_FEED_PET                                                                                                                   |
| 102       | EffectDismissPet               | SPELL_EFFECT_DISMISS_PET                                                                                                                |
| 103       | EffectReputation               | SPELL_EFFECT_REPUTATION                                                                                                                 |
| 104       | EffectSummonObject             | SPELL_EFFECT_SUMMON_OBJECT_SLOT1                                                                                                        |
| 105       | EffectSummonObject             | SPELL_EFFECT_SUMMON_OBJECT_SLOT2                                                                                                        |
| 106       | EffectSummonObject             | SPELL_EFFECT_SUMMON_OBJECT_SLOT3                                                                                                        |
| 107       | EffectSummonObject             | SPELL_EFFECT_SUMMON_OBJECT_SLOT4                                                                                                        |
| 108       | EffectDispelMechanic           | SPELL_EFFECT_DISPEL_MECHANIC                                                                                                            |
| 109       | EffectSummonDeadPet            | SPELL_EFFECT_SUMMON_DEAD_PET                                                                                                            |
| 110       | EffectDestroyAllTotems         | SPELL_EFFECT_DESTROY_ALL_TOTEMS                                                                                                         |
| 111       | EffectDurabilityDamage         | SPELL_EFFECT_DURABILITY_DAMAGE                                                                                                          |
| 112       | EffectUnused                   | SPELL_EFFECT_112                                                                                                                        |
| 113       | EffectResurrectNew             | SPELL_EFFECT_RESURRECT_NEW                                                                                                              |
| 114       | EffectTaunt                    | SPELL_EFFECT_ATTACK_ME                                                                                                                  |
| 115       | EffectDurabilityDamagePCT      | SPELL_EFFECT_DURABILITY_DAMAGE_PCT                                                                                                      |
| 116       | EffectSkinPlayerCorpse         | SPELL_EFFECT_SKIN_PLAYER_CORPSE one spell: Remove Insignia, bg usage, required special corpse flags...                                  |
| 117       | EffectSpiritHeal               | SPELL_EFFECT_SPIRIT_HEAL one spell: Spirit Heal                                                                                         |
| 118       | EffectSkill                    | SPELL_EFFECT_SKILL professions and more                                                                                                 |
| 119       | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_PET                                                                                                        |
| 120       | EffectUnused                   | SPELL_EFFECT_TELEPORT_GRAVEYARD one spell: Graveyard Teleport Test                                                                      |
| 121       | EffectWeaponDmg                | SPELL_EFFECT_NORMALIZED_WEAPON_DMG                                                                                                      |
| 122       | EffectUnused                   | SPELL_EFFECT_122 unused                                                                                                                 |
| 123       | EffectSendTaxi                 | SPELL_EFFECT_SEND_TAXI taxi/flight related (misc value is taxi path id)                                                                 |
| 124       | EffectPullTowards              | SPELL_EFFECT_PULL_TOWARDS                                                                                                               |
| 125       | EffectModifyThreatPercent      | SPELL_EFFECT_MODIFY_THREAT_PERCENT                                                                                                      |
| 126       | EffectStealBeneficialBuff      | SPELL_EFFECT_STEAL_BENEFICIAL_BUFF spell steal effect?                                                                                  |
| 127       | EffectProspecting              | SPELL_EFFECT_PROSPECTING Prospecting spell                                                                                              |
| 128       | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_FRIEND                                                                                                     |
| 129       | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_ENEMY                                                                                                      |
| 130       | EffectRedirectThreat           | SPELL_EFFECT_REDIRECT_THREAT                                                                                                            |
| 131       | EffectPlayerNotification       | SPELL_EFFECT_PLAYER_NOTIFICATION                                                                                                        |
| 132       | EffectPlayMusic                | SPELL_EFFECT_PLAY_MUSIC sound id in misc value (SoundEntries.dbc)                                                                       |
| 133       | EffectUnlearnSpecialization    | SPELL_EFFECT_UNLEARN_SPECIALIZATION unlearn profession specialization                                                                   |
| 134       | EffectKillCredit               | SPELL_EFFECT_KILL_CREDIT misc value is creature entry                                                                                   |
| 135       | EffectNULL                     | SPELL_EFFECT_CALL_PET                                                                                                                   |
| 136       | EffectHealPct                  | SPELL_EFFECT_HEAL_PCT                                                                                                                   |
| 137       | EffectEnergizePct              | SPELL_EFFECT_ENERGIZE_PCT                                                                                                               |
| 138       | EffectLeapBack                 | SPELL_EFFECT_LEAP_BACK Leap back                                                                                                        |
| 139       | EffectQuestClear               | SPELL_EFFECT_CLEAR_QUEST Reset quest status (miscValue - quest ID)                                                                      |
| 140       | EffectForceCast                | SPELL_EFFECT_FORCE_CAST                                                                                                                 |
| 141       | EffectForceCastWithValue       | SPELL_EFFECT_FORCE_CAST_WITH_VALUE                                                                                                      |
| 142       | EffectTriggerSpellWithValue    | SPELL_EFFECT_TRIGGER_SPELL_WITH_VALUE                                                                                                   |
| 143       | EffectApplyAreaAura            | SPELL_EFFECT_APPLY_AREA_AURA_OWNER                                                                                                      |
| 144       | EffectKnockBack                | SPELL_EFFECT_KNOCK_BACK_DEST                                                                                                            |
| 145       | EffectPullTowards              | SPELL_EFFECT_PULL_TOWARDS_DEST Black Hole Effect                                                                                        |
| 146       | EffectActivateRune             | SPELL_EFFECT_ACTIVATE_RUNE                                                                                                              |
| 147       | EffectQuestFail                | SPELL_EFFECT_QUEST_FAIL quest fail                                                                                                      |
| 148       | EffectUnused                   | SPELL_EFFECT_148 1 spell - 43509                                                                                                        |
| 149       | EffectChargeDest               | SPELL_EFFECT_CHARGE_DEST                                                                                                                |
| 150       | EffectQuestStart               | SPELL_EFFECT_QUEST_START                                                                                                                |
| 151       | EffectTriggerRitualOfSummoning | SPELL_EFFECT_TRIGGER_SPELL_2                                                                                                            |
| 152       | EffectNULL                     | SPELL_EFFECT_152 summon Refer-a-Friend                                                                                                  |
| 153       | EffectCreateTamedPet           | SPELL_EFFECT_CREATE_TAMED_PET misc value is creature entry                                                                              |
| 154       | EffectDiscoverTaxi             | SPELL_EFFECT_DISCOVER_TAXI                                                                                                              |
| 155       | EffectTitanGrip                | SPELL_EFFECT_TITAN_GRIP Allows you to equip two-handed axes, maces and swords in one hand, but you attack $49152s1% slower than normal. |
| 156       | EffectEnchantItemPrismatic     | SPELL_EFFECT_ENCHANT_ITEM_PRISMATIC                                                                                                     |
| 157       | EffectCreateItem2              | SPELL_EFFECT_CREATE_ITEM_2 create item or create item template and replace by some randon spell loot item                               |
| 158       | EffectMilling                  | SPELL_EFFECT_MILLING milling                                                                                                            |
| 159       | EffectRenamePet                | SPELL_EFFECT_ALLOW_RENAME_PET allow rename pet once again                                                                               |
| 160       | EffectNULL                     | SPELL_EFFECT_160 1 spell - 45534                                                                                                        |
| 161       | EffectSpecCount                | SPELL_EFFECT_TALENT_SPEC_COUNT second talent spec (learn/revert)                                                                        |
| 162       | EffectActivateSpec             | SPELL_EFFECT_TALENT_SPEC_SELECT activate primary/secondary spec                                                                         |
| 163       | EffectNULL                     | unused                                                                                                                                  |
| 164       | EffectRemoveAura               | SPELL_EFFECT_REMOVE_AURA                                                                                                                |
