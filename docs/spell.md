---
redirect_from: "/Spell"
---

# Spell

[`Back-to:DBC`](dbc-index)

# **Spell.dbc**

This DBC contains most information on all spells.
These values are used by the core and a few spell\_\* tables.

**Version 3.3.5**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

## **Table Structure**

| Column | Field                      | Type   | spell\_dbc column                                                  | Comment                                                                                               |
| :----: | :------------------------- | :----- | :----------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| 0      | ID                         | uint32 | [ID](spell_dbc#id)                                                 |                                                                                                       |
| 1      | Category                   | uint32 | [Category](spell_dbc#category)                                     | ID in [SpellCategory.dbc](dbc-spellcategory)                                                          |
| 2      | DispelType                 | uint32 | [DispelType](spell_dbc#dispeltype)                                 | ID in [SpellDispelType.dbc](dbc-spelldispeltype)                                                      |
| 3      | Mechanic                   | uint32 | [Mechanic](spell_dbc#mechanic)                                     | ID in [SpellMechanic.dbc](dbc-spellmechanic)                                                          |
| 4      | Attributes                 | uint32 | [Attributes](spell_dbc#attributes)                                 |                                                                                                       |
| 5      | AttributesEx               | uint32 | [AttributesEx](spell_dbc#attributesex)                             |                                                                                                       |
| 6      | AttributesExB              | uint32 | [AttributesEx2](spell_dbc#attributesex2)                           |                                                                                                       |
| 7      | AttributesExC              | uint32 | [AttributesEx3](spell_dbc#attributesex3)                           |                                                                                                       |
| 8      | AttributesExD              | uint32 | [AttributesEx4](spell_dbc#attributesex4)                           |                                                                                                       |
| 9      | AttributesExE              | uint32 | [AttributesEx5](spell_dbc#attributesex5)                           |                                                                                                       |
| 10     | AttributesExF              | uint32 | [AttributesEx6](spell_dbc#attributesex6)                           |                                                                                                       |
| 11     | AttributesExG              | uint32 | [AttributesEx7](spell_dbc#attributesex7)                           |                                                                                                       |
| 12     | ShapeshiftMask_0           | uint32 | [ShapeshiftMask](spell_dbc#shapeshiftmask)                         | Bitmask of shapeshift forms (bit = ID - 1). See [SpellShapeshiftForm.dbc](dbc-spellshapeshiftform)    |
| 13     | ShapeshiftMask_1           | uint32 | [unk_320_2](spell_dbc#unk320)                                      |                                                                                                       |
| 14     | ShapeshiftExclude_0        | uint32 | [ShapeshiftExclude](spell_dbc#shapeshiftexclude)                   | Bitmask of shapeshift forms (bit = ID - 1). See [SpellShapeshiftForm.dbc](dbc-spellshapeshiftform)    |
| 15     | ShapeshiftExclude_1        | uint32 | [unk_320_3](spell_dbc#unk320)                                      |                                                                                                       |
| 16     | Targets                    | uint32 | [Targets](spell_dbc#targets)                                       |                                                                                                       |
| 17     | TargetCreatureType         | uint32 | [TargetCreatureType](spell_dbc#targetcreaturetype)                 | Bitmask of creature types (bit = ID - 1). See [CreatureType.dbc](dbc-creaturetype)                    |
| 18     | RequiresSpellFocus         | uint32 | [RequiresSpellFocus](spell_dbc#requiresspellfocus)                 | ID in [SpellFocusObject.dbc](dbc-spellfocusobject)                                                    |
| 19     | FacingCasterFlags          | uint32 | [FacingCasterFlags](spell_dbc#facingcasterflags)                   |                                                                                                       |
| 20     | CasterAuraState            | uint32 | [CasterAuraState](spell_dbc#casteraurastate)                       |                                                                                                       |
| 21     | TargetAuraState            | uint32 | [TargetAuraState](spell_dbc#targetaurastate)                       |                                                                                                       |
| 22     | ExcludeCasterAuraState     | uint32 | [ExcludeCasterAuraState](spell_dbc#excludecasteraurastate)         |                                                                                                       |
| 23     | ExcludeTargetAuraState     | uint32 | [ExcludeTargetAuraState](spell_dbc#excludetargetaurastate)         |                                                                                                       |
| 24     | CasterAuraSpell            | uint32 | [CasterAuraSpell](spell_dbc#casterauraspell)                       |                                                                                                       |
| 25     | TargetAuraSpell            | uint32 | [TargetAuraSpell](spell_dbc#targetauraspell)                       |                                                                                                       |
| 26     | ExcludeCasterAuraSpell     | uint32 | [ExcludeCasterAuraSpell](spell_dbc#excludecasterauraspell)         |                                                                                                       |
| 27     | ExcludeTargetAuraSpell     | uint32 | [ExcludeTargetAuraSpell](spell_dbc#excludetargetauraspell)         |                                                                                                       |
| 28     | CastingTimeIndex           | uint32 | [CastingTimeIndex](spell_dbc#castingtimeindex)                     | ID in [SpellCastTimes.dbc](dbc-spellcasttimes)                                                        |
| 29     | RecoveryTime               | uint32 | [RecoveryTime](spell_dbc#recoverytime)                             |                                                                                                       |
| 30     | CategoryRecoveryTime       | uint32 | [CategoryRecoveryTime](spell_dbc#categoryrecoverytime)             |                                                                                                       |
| 31     | InterruptFlags             | uint32 | [InterruptFlags](spell_dbc#interruptflags)                         |                                                                                                       |
| 32     | AuraInterruptFlags         | uint32 | [AuraInterruptFlags](spell_dbc#aurainterruptflags)                 |                                                                                                       |
| 33     | ChannelInterruptFlags      | uint32 | [ChannelInterruptFlags](spell_dbc#channelinterruptflags)           |                                                                                                       |
| 34     | ProcTypeMask               | uint32 | [ProcTypeMask](spell_dbc#proctypemask)                             |                                                                                                       |
| 35     | ProcChance                 | uint32 | [ProcChance](spell_dbc#procchance)                                 |                                                                                                       |
| 36     | ProcCharges                | uint32 | [ProcCharges](spell_dbc#proccharges)                               |                                                                                                       |
| 37     | MaxLevel                   | uint32 | [MaxLevel](spell_dbc#maxlevel)                                     |                                                                                                       |
| 38     | BaseLevel                  | uint32 | [BaseLevel](spell_dbc#baselevel)                                   |                                                                                                       |
| 39     | SpellLevel                 | uint32 | [SpellLevel](spell_dbc#spelllevel)                                 |                                                                                                       |
| 40     | DurationIndex              | uint32 | [DurationIndex](spell_dbc#durationindex)                           | ID in [SpellDuration.dbc](dbc-spellduration)                                                          |
| 41     | PowerType                  | int32  | [PowerType](spell_dbc#powertype)                                   |                                                                                                       |
| 42     | ManaCost                   | uint32 | [ManaCost](spell_dbc#manacost)                                     |                                                                                                       |
| 43     | ManaCostPerLevel           | uint32 | [ManaCostPerLevel](spell_dbc#manacostperlevel)                     |                                                                                                       |
| 44     | ManaPerSecond              | uint32 | [ManaPerSecond](spell_dbc#manapersecond)                           |                                                                                                       |
| 45     | ManaPerSecondPerLevel      | uint32 | [ManaPerSecondPerLevel](spell_dbc#manapersecondperlevel)           |                                                                                                       |
| 46     | RangeIndex                 | uint32 | [RangeIndex](spell_dbc#rangeindex)                                 | ID in [SpellRange.dbc](dbc-spellrange)                                                                |
| 47     | Speed                      | float  | [Speed](spell_dbc#speed)                                           |                                                                                                       |
| 48     | ModalNextSpell             | uint32 | [ModalNextSpell](spell_dbc#modalnextspell)                         |                                                                                                       |
| 49     | CumulativeAura             | uint32 | [CumulativeAura](spell_dbc#cumulativeaura)                         |                                                                                                       |
| 50     | Totem_0                    | uint32 | [Totem_1](spell_dbc#totem)                                         | ID in [Item.dbc](dbc-item)                                                                            |
| 51     | Totem_1                    | uint32 | [Totem_2](spell_dbc#totem)                                         | ID in [Item.dbc](dbc-item)                                                                            |
| 52     | Reagent_0                  | int32  | [Reagent_1](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item) (1 of the 837 values used here are not in that file)                       |
| 53     | Reagent_1                  | int32  | [Reagent_2](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item) (1 of the 500 values used here are not in that file)                       |
| 54     | Reagent_2                  | int32  | [Reagent_3](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item) (1 of the 346 values used here are not in that file)                       |
| 55     | Reagent_3                  | int32  | [Reagent_4](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item) (1 of the 217 values used here are not in that file)                       |
| 56     | Reagent_4                  | int32  | [Reagent_5](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item)                                                                            |
| 57     | Reagent_5                  | int32  | [Reagent_6](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item)                                                                            |
| 58     | Reagent_6                  | int32  | [Reagent_7](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item)                                                                            |
| 59     | Reagent_7                  | int32  | [Reagent_8](spell_dbc#reagent)                                     | ID in [Item.dbc](dbc-item)                                                                            |
| 60     | ReagentCount_0             | uint32 | [ReagentCount_1](spell_dbc#reagentcount)                           |                                                                                                       |
| 61     | ReagentCount_1             | uint32 | [ReagentCount_2](spell_dbc#reagentcount)                           |                                                                                                       |
| 62     | ReagentCount_2             | uint32 | [ReagentCount_3](spell_dbc#reagentcount)                           |                                                                                                       |
| 63     | ReagentCount_3             | uint32 | [ReagentCount_4](spell_dbc#reagentcount)                           |                                                                                                       |
| 64     | ReagentCount_4             | uint32 | [ReagentCount_5](spell_dbc#reagentcount)                           |                                                                                                       |
| 65     | ReagentCount_5             | uint32 | [ReagentCount_6](spell_dbc#reagentcount)                           |                                                                                                       |
| 66     | ReagentCount_6             | uint32 | [ReagentCount_7](spell_dbc#reagentcount)                           |                                                                                                       |
| 67     | ReagentCount_7             | uint32 | [ReagentCount_8](spell_dbc#reagentcount)                           |                                                                                                       |
| 68     | EquippedItemClass          | int32  | [EquippedItemClass](spell_dbc#equippeditemclass)                   | ID in [ItemSubClass.dbc](dbc-itemsubclass)                                                            |
| 69     | EquippedItemSubclass       | int32  | [EquippedItemSubclass](spell_dbc#equippeditemsubclass)             |                                                                                                       |
| 70     | EquippedItemInvTypes       | int32  | [EquippedItemInvTypes](spell_dbc#equippediteminvtypes)             |                                                                                                       |
| 71     | Effect_0                   | uint32 | [Effect_1](spell_dbc#effect)                                       |                                                                                                       |
| 72     | Effect_1                   | uint32 | [Effect_2](spell_dbc#effect)                                       |                                                                                                       |
| 73     | Effect_2                   | uint32 | [Effect_3](spell_dbc#effect)                                       |                                                                                                       |
| 74     | EffectDieSides_0           | int32  | [EffectDieSides_1](spell_dbc#effectdiesides)                       |                                                                                                       |
| 75     | EffectDieSides_1           | int32  | [EffectDieSides_2](spell_dbc#effectdiesides)                       |                                                                                                       |
| 76     | EffectDieSides_2           | int32  | [EffectDieSides_3](spell_dbc#effectdiesides)                       |                                                                                                       |
| 77     | EffectRealPointsPerLevel_0 | float  | [EffectRealPointsPerLevel_1](spell_dbc#effectrealpointsperlevel)   |                                                                                                       |
| 78     | EffectRealPointsPerLevel_1 | float  | [EffectRealPointsPerLevel_2](spell_dbc#effectrealpointsperlevel)   |                                                                                                       |
| 79     | EffectRealPointsPerLevel_2 | float  | [EffectRealPointsPerLevel_3](spell_dbc#effectrealpointsperlevel)   |                                                                                                       |
| 80     | EffectBasePoints_0         | int32  | [EffectBasePoints_1](spell_dbc#effectbasepoints)                   |                                                                                                       |
| 81     | EffectBasePoints_1         | int32  | [EffectBasePoints_2](spell_dbc#effectbasepoints)                   |                                                                                                       |
| 82     | EffectBasePoints_2         | int32  | [EffectBasePoints_3](spell_dbc#effectbasepoints)                   |                                                                                                       |
| 83     | EffectMechanic_0           | uint32 | [EffectMechanic_1](spell_dbc#effectmechanic)                       | ID in [SpellMechanic.dbc](dbc-spellmechanic)                                                          |
| 84     | EffectMechanic_1           | uint32 | [EffectMechanic_2](spell_dbc#effectmechanic)                       | ID in [SpellMechanic.dbc](dbc-spellmechanic)                                                          |
| 85     | EffectMechanic_2           | uint32 | [EffectMechanic_3](spell_dbc#effectmechanic)                       | ID in [SpellMechanic.dbc](dbc-spellmechanic)                                                          |
| 86     | EffectImplicitTargetA_0    | uint32 | [ImplicitTargetA_1](spell_dbc#implicittargeta)                     |                                                                                                       |
| 87     | EffectImplicitTargetA_1    | uint32 | [ImplicitTargetA_2](spell_dbc#implicittargeta)                     |                                                                                                       |
| 88     | EffectImplicitTargetA_2    | uint32 | [ImplicitTargetA_3](spell_dbc#implicittargeta)                     |                                                                                                       |
| 89     | EffectImplicitTargetB_0    | uint32 | [ImplicitTargetB_1](spell_dbc#implicittargetb)                     |                                                                                                       |
| 90     | EffectImplicitTargetB_1    | uint32 | [ImplicitTargetB_2](spell_dbc#implicittargetb)                     |                                                                                                       |
| 91     | EffectImplicitTargetB_2    | uint32 | [ImplicitTargetB_3](spell_dbc#implicittargetb)                     |                                                                                                       |
| 92     | EffectRadiusIndex_0        | uint32 | [EffectRadiusIndex_1](spell_dbc#effectradiusindex)                 | ID in [SpellRadius.dbc](dbc-spellradius)                                                              |
| 93     | EffectRadiusIndex_1        | uint32 | [EffectRadiusIndex_2](spell_dbc#effectradiusindex)                 | ID in [SpellRadius.dbc](dbc-spellradius)                                                              |
| 94     | EffectRadiusIndex_2        | uint32 | [EffectRadiusIndex_3](spell_dbc#effectradiusindex)                 | ID in [SpellRadius.dbc](dbc-spellradius)                                                              |
| 95     | EffectAura_0               | uint32 | [EffectAura_1](spell_dbc#effectaura)                               |                                                                                                       |
| 96     | EffectAura_1               | uint32 | [EffectAura_2](spell_dbc#effectaura)                               |                                                                                                       |
| 97     | EffectAura_2               | uint32 | [EffectAura_3](spell_dbc#effectaura)                               |                                                                                                       |
| 98     | EffectAuraPeriod_0         | uint32 | [EffectAuraPeriod_1](spell_dbc#effectauraperiod)                   |                                                                                                       |
| 99     | EffectAuraPeriod_1         | uint32 | [EffectAuraPeriod_2](spell_dbc#effectauraperiod)                   |                                                                                                       |
| 100    | EffectAuraPeriod_2         | uint32 | [EffectAuraPeriod_3](spell_dbc#effectauraperiod)                   |                                                                                                       |
| 101    | EffectAmplitude_0          | float  | [EffectMultipleValue_1](spell_dbc#effectmultiplevalue)             |                                                                                                       |
| 102    | EffectAmplitude_1          | float  | [EffectMultipleValue_2](spell_dbc#effectmultiplevalue)             |                                                                                                       |
| 103    | EffectAmplitude_2          | float  | [EffectMultipleValue_3](spell_dbc#effectmultiplevalue)             |                                                                                                       |
| 104    | EffectChainTargets_0       | uint32 | [EffectChainTargets_1](spell_dbc#effectchaintargets)               |                                                                                                       |
| 105    | EffectChainTargets_1       | uint32 | [EffectChainTargets_2](spell_dbc#effectchaintargets)               |                                                                                                       |
| 106    | EffectChainTargets_2       | uint32 | [EffectChainTargets_3](spell_dbc#effectchaintargets)               |                                                                                                       |
| 107    | EffectItemType_0           | uint32 | [EffectItemType_1](spell_dbc#effectitemtype)                       | ID in [Item.dbc](dbc-item) (37 of the 4264 values used here are not in that file)                     |
| 108    | EffectItemType_1           | uint32 | [EffectItemType_2](spell_dbc#effectitemtype)                       | ID in [Item.dbc](dbc-item) (6 of the 52 values used here are not in that file)                        |
| 109    | EffectItemType_2           | uint32 | [EffectItemType_3](spell_dbc#effectitemtype)                       |                                                                                                       |
| 110    | EffectMiscValue_0          | int32  | [EffectMiscValue_1](spell_dbc#effectmiscvalue)                     |                                                                                                       |
| 111    | EffectMiscValue_1          | int32  | [EffectMiscValue_2](spell_dbc#effectmiscvalue)                     |                                                                                                       |
| 112    | EffectMiscValue_2          | int32  | [EffectMiscValue_3](spell_dbc#effectmiscvalue)                     |                                                                                                       |
| 113    | EffectMiscValueB_0         | int32  | [EffectMiscValueB_1](spell_dbc#effectmiscvalueb)                   |                                                                                                       |
| 114    | EffectMiscValueB_1         | int32  | [EffectMiscValueB_2](spell_dbc#effectmiscvalueb)                   |                                                                                                       |
| 115    | EffectMiscValueB_2         | int32  | [EffectMiscValueB_3](spell_dbc#effectmiscvalueb)                   |                                                                                                       |
| 116    | EffectTriggerSpell_0       | int32  | [EffectTriggerSpell_1](spell_dbc#effecttriggerspell)               |                                                                                                       |
| 117    | EffectTriggerSpell_1       | int32  | [EffectTriggerSpell_2](spell_dbc#effecttriggerspell)               |                                                                                                       |
| 118    | EffectTriggerSpell_2       | int32  | [EffectTriggerSpell_3](spell_dbc#effecttriggerspell)               |                                                                                                       |
| 119    | EffectPointsPerCombo_0     | float  | [EffectPointsPerCombo_1](spell_dbc#effectpointspercombo)           |                                                                                                       |
| 120    | EffectPointsPerCombo_1     | float  | [EffectPointsPerCombo_2](spell_dbc#effectpointspercombo)           |                                                                                                       |
| 121    | EffectPointsPerCombo_2     | float  | [EffectPointsPerCombo_3](spell_dbc#effectpointspercombo)           |                                                                                                       |
| 122    | EffectSpellClassMask_A_0   | uint32 | [EffectSpellClassMaskA_1](spell_dbc#effectspellclassmaska)         |                                                                                                       |
| 123    | EffectSpellClassMask_A_1   | uint32 | [EffectSpellClassMaskA_2](spell_dbc#effectspellclassmaska)         |                                                                                                       |
| 124    | EffectSpellClassMask_A_2   | uint32 | [EffectSpellClassMaskA_3](spell_dbc#effectspellclassmaska)         |                                                                                                       |
| 125    | EffectSpellClassMask_B_0   | uint32 | [EffectSpellClassMaskB_1](spell_dbc#effectspellclassmaskb)         |                                                                                                       |
| 126    | EffectSpellClassMask_B_1   | uint32 | [EffectSpellClassMaskB_2](spell_dbc#effectspellclassmaskb)         |                                                                                                       |
| 127    | EffectSpellClassMask_B_2   | uint32 | [EffectSpellClassMaskB_3](spell_dbc#effectspellclassmaskb)         |                                                                                                       |
| 128    | EffectSpellClassMask_C_0   | uint32 | [EffectSpellClassMaskC_1](spell_dbc#effectspellclassmaskc)         |                                                                                                       |
| 129    | EffectSpellClassMask_C_1   | uint32 | [EffectSpellClassMaskC_2](spell_dbc#effectspellclassmaskc)         |                                                                                                       |
| 130    | EffectSpellClassMask_C_2   | uint32 | [EffectSpellClassMaskC_3](spell_dbc#effectspellclassmaskc)         |                                                                                                       |
| 131    | SpellVisualID_0            | uint32 | [SpellVisualID_1](spell_dbc#spellvisualid)                         | ID in [SpellVisual.dbc](dbc-spellvisual)                                                              |
| 132    | SpellVisualID_1            | uint32 | [SpellVisualID_2](spell_dbc#spellvisualid)                         | ID in [SpellVisual.dbc](dbc-spellvisual)                                                              |
| 133    | SpellIconID                | uint32 | [SpellIconID](spell_dbc#spelliconid)                               | ID in [SpellIcon.dbc](dbc-spellicon)                                                                  |
| 134    | ActiveIconID               | uint32 | [ActiveIconID](spell_dbc#activeiconid)                             | ID in [SpellIcon.dbc](dbc-spellicon)                                                                  |
| 135    | SpellPriority              | uint32 | [SpellPriority](spell_dbc#spellpriority)                           |                                                                                                       |
| 136    | Name_0                     | string | [Name_Lang_enUS](spell_dbc#namelang)                               | Assumed enUS                                                                                          |
| 137    | Name_1                     | string | [Name_Lang_enGB](spell_dbc#namelang)                               | Assumed enGB, not used in 3.3.5a                                                                      |
| 138    | Name_2                     | string | [Name_Lang_koKR](spell_dbc#namelang)                               | Assumed koKR                                                                                          |
| 139    | Name_3                     | string | [Name_Lang_frFR](spell_dbc#namelang)                               | Assumed frFR                                                                                          |
| 140    | Name_4                     | string | [Name_Lang_deDE](spell_dbc#namelang)                               | Assumed deDE                                                                                          |
| 141    | Name_5                     | string | [Name_Lang_enCN](spell_dbc#namelang)                               | Assumed enCN, not used in 3.3.5a                                                                      |
| 142    | Name_6                     | string | [Name_Lang_zhCN](spell_dbc#namelang)                               | Assumed zhCN                                                                                          |
| 143    | Name_7                     | string | [Name_Lang_enTW](spell_dbc#namelang)                               | Assumed enTW, not used in 3.3.5a                                                                      |
| 144    | Name_8                     | string | [Name_Lang_zhTW](spell_dbc#namelang)                               | Assumed zhTW                                                                                          |
| 145    | Name_9                     | string | [Name_Lang_esES](spell_dbc#namelang)                               | Assumed esES                                                                                          |
| 146    | Name_10                    | string | [Name_Lang_esMX](spell_dbc#namelang)                               | Assumed esMX                                                                                          |
| 147    | Name_11                    | string | [Name_Lang_ruRU](spell_dbc#namelang)                               | Assumed ruRU                                                                                          |
| 148    | Name_12                    | string | [Name_Lang_ptPT](spell_dbc#namelang)                               | Assumed ptPT, not used in 3.3.5a                                                                      |
| 149    | Name_13                    | string | [Name_Lang_ptBR](spell_dbc#namelang)                               | Assumed ptBR, not used in 3.3.5a                                                                      |
| 150    | Name_14                    | string | [Name_Lang_itIT](spell_dbc#namelang)                               | Assumed itIT, not used in 3.3.5a                                                                      |
| 151    | Name_15                    | string | [Name_Lang_Unk](spell_dbc#namelang)                                | Unknown language, unsure of the usage in 3.3.5a                                                       |
| 152    | Name_lang_mask             | uint32 | [Name_Lang_Mask](spell_dbc#namelang)                               | Assumed flags of the localized text                                                                   |
| 153    | NameSubtext_0              | string | [NameSubtext_Lang_enUS](spell_dbc#namesubtextlang)                 | Assumed enUS                                                                                          |
| 154    | NameSubtext_1              | string | [NameSubtext_Lang_enGB](spell_dbc#namesubtextlang)                 | Assumed enGB, not used in 3.3.5a                                                                      |
| 155    | NameSubtext_2              | string | [NameSubtext_Lang_koKR](spell_dbc#namesubtextlang)                 | Assumed koKR                                                                                          |
| 156    | NameSubtext_3              | string | [NameSubtext_Lang_frFR](spell_dbc#namesubtextlang)                 | Assumed frFR                                                                                          |
| 157    | NameSubtext_4              | string | [NameSubtext_Lang_deDE](spell_dbc#namesubtextlang)                 | Assumed deDE                                                                                          |
| 158    | NameSubtext_5              | string | [NameSubtext_Lang_enCN](spell_dbc#namesubtextlang)                 | Assumed enCN, not used in 3.3.5a                                                                      |
| 159    | NameSubtext_6              | string | [NameSubtext_Lang_zhCN](spell_dbc#namesubtextlang)                 | Assumed zhCN                                                                                          |
| 160    | NameSubtext_7              | string | [NameSubtext_Lang_enTW](spell_dbc#namesubtextlang)                 | Assumed enTW, not used in 3.3.5a                                                                      |
| 161    | NameSubtext_8              | string | [NameSubtext_Lang_zhTW](spell_dbc#namesubtextlang)                 | Assumed zhTW                                                                                          |
| 162    | NameSubtext_9              | string | [NameSubtext_Lang_esES](spell_dbc#namesubtextlang)                 | Assumed esES                                                                                          |
| 163    | NameSubtext_10             | string | [NameSubtext_Lang_esMX](spell_dbc#namesubtextlang)                 | Assumed esMX                                                                                          |
| 164    | NameSubtext_11             | string | [NameSubtext_Lang_ruRU](spell_dbc#namesubtextlang)                 | Assumed ruRU                                                                                          |
| 165    | NameSubtext_12             | string | [NameSubtext_Lang_ptPT](spell_dbc#namesubtextlang)                 | Assumed ptPT, not used in 3.3.5a                                                                      |
| 166    | NameSubtext_13             | string | [NameSubtext_Lang_ptBR](spell_dbc#namesubtextlang)                 | Assumed ptBR, not used in 3.3.5a                                                                      |
| 167    | NameSubtext_14             | string | [NameSubtext_Lang_itIT](spell_dbc#namesubtextlang)                 | Assumed itIT, not used in 3.3.5a                                                                      |
| 168    | NameSubtext_15             | string | [NameSubtext_Lang_Unk](spell_dbc#namesubtextlang)                  | Unknown language, unsure of the usage in 3.3.5a                                                       |
| 169    | NameSubtext_lang_mask      | uint32 | [NameSubtext_Lang_Mask](spell_dbc#namesubtextlang)                 | Assumed flags of the localized text                                                                   |
| 170    | Description_0              | string | [Description_Lang_enUS](spell_dbc#descriptionlang)                 | Assumed enUS                                                                                          |
| 171    | Description_1              | string | [Description_Lang_enGB](spell_dbc#descriptionlang)                 | Assumed enGB, not used in 3.3.5a                                                                      |
| 172    | Description_2              | string | [Description_Lang_koKR](spell_dbc#descriptionlang)                 | Assumed koKR                                                                                          |
| 173    | Description_3              | string | [Description_Lang_frFR](spell_dbc#descriptionlang)                 | Assumed frFR                                                                                          |
| 174    | Description_4              | string | [Description_Lang_deDE](spell_dbc#descriptionlang)                 | Assumed deDE                                                                                          |
| 175    | Description_5              | string | [Description_Lang_enCN](spell_dbc#descriptionlang)                 | Assumed enCN, not used in 3.3.5a                                                                      |
| 176    | Description_6              | string | [Description_Lang_zhCN](spell_dbc#descriptionlang)                 | Assumed zhCN                                                                                          |
| 177    | Description_7              | string | [Description_Lang_enTW](spell_dbc#descriptionlang)                 | Assumed enTW, not used in 3.3.5a                                                                      |
| 178    | Description_8              | string | [Description_Lang_zhTW](spell_dbc#descriptionlang)                 | Assumed zhTW                                                                                          |
| 179    | Description_9              | string | [Description_Lang_esES](spell_dbc#descriptionlang)                 | Assumed esES                                                                                          |
| 180    | Description_10             | string | [Description_Lang_esMX](spell_dbc#descriptionlang)                 | Assumed esMX                                                                                          |
| 181    | Description_11             | string | [Description_Lang_ruRU](spell_dbc#descriptionlang)                 | Assumed ruRU                                                                                          |
| 182    | Description_12             | string | [Description_Lang_ptPT](spell_dbc#descriptionlang)                 | Assumed ptPT, not used in 3.3.5a                                                                      |
| 183    | Description_13             | string | [Description_Lang_ptBR](spell_dbc#descriptionlang)                 | Assumed ptBR, not used in 3.3.5a                                                                      |
| 184    | Description_14             | string | [Description_Lang_itIT](spell_dbc#descriptionlang)                 | Assumed itIT, not used in 3.3.5a                                                                      |
| 185    | Description_15             | string | [Description_Lang_Unk](spell_dbc#descriptionlang)                  | Unknown language, unsure of the usage in 3.3.5a                                                       |
| 186    | Description_lang_mask      | uint32 | [Description_Lang_Mask](spell_dbc#descriptionlang)                 | Assumed flags of the localized text                                                                   |
| 187    | AuraDescription_0          | string | [AuraDescription_Lang_enUS](spell_dbc#auradescriptionlang)         | Assumed enUS                                                                                          |
| 188    | AuraDescription_1          | string | [AuraDescription_Lang_enGB](spell_dbc#auradescriptionlang)         | Assumed enGB, not used in 3.3.5a                                                                      |
| 189    | AuraDescription_2          | string | [AuraDescription_Lang_koKR](spell_dbc#auradescriptionlang)         | Assumed koKR                                                                                          |
| 190    | AuraDescription_3          | string | [AuraDescription_Lang_frFR](spell_dbc#auradescriptionlang)         | Assumed frFR                                                                                          |
| 191    | AuraDescription_4          | string | [AuraDescription_Lang_deDE](spell_dbc#auradescriptionlang)         | Assumed deDE                                                                                          |
| 192    | AuraDescription_5          | string | [AuraDescription_Lang_enCN](spell_dbc#auradescriptionlang)         | Assumed enCN, not used in 3.3.5a                                                                      |
| 193    | AuraDescription_6          | string | [AuraDescription_Lang_zhCN](spell_dbc#auradescriptionlang)         | Assumed zhCN                                                                                          |
| 194    | AuraDescription_7          | string | [AuraDescription_Lang_enTW](spell_dbc#auradescriptionlang)         | Assumed enTW, not used in 3.3.5a                                                                      |
| 195    | AuraDescription_8          | string | [AuraDescription_Lang_zhTW](spell_dbc#auradescriptionlang)         | Assumed zhTW                                                                                          |
| 196    | AuraDescription_9          | string | [AuraDescription_Lang_esES](spell_dbc#auradescriptionlang)         | Assumed esES                                                                                          |
| 197    | AuraDescription_10         | string | [AuraDescription_Lang_esMX](spell_dbc#auradescriptionlang)         | Assumed esMX                                                                                          |
| 198    | AuraDescription_11         | string | [AuraDescription_Lang_ruRU](spell_dbc#auradescriptionlang)         | Assumed ruRU                                                                                          |
| 199    | AuraDescription_12         | string | [AuraDescription_Lang_ptPT](spell_dbc#auradescriptionlang)         | Assumed ptPT, not used in 3.3.5a                                                                      |
| 200    | AuraDescription_13         | string | [AuraDescription_Lang_ptBR](spell_dbc#auradescriptionlang)         | Assumed ptBR, not used in 3.3.5a                                                                      |
| 201    | AuraDescription_14         | string | [AuraDescription_Lang_itIT](spell_dbc#auradescriptionlang)         | Assumed itIT, not used in 3.3.5a                                                                      |
| 202    | AuraDescription_15         | string | [AuraDescription_Lang_Unk](spell_dbc#auradescriptionlang)          | Unknown language, unsure of the usage in 3.3.5a                                                       |
| 203    | AuraDescription_lang_mask  | uint32 | [AuraDescription_Lang_Mask](spell_dbc#auradescriptionlang)         | Assumed flags of the localized text                                                                   |
| 204    | ManaCostPct                | uint32 | [ManaCostPct](spell_dbc#manacostpct)                               |                                                                                                       |
| 205    | StartRecoveryCategory      | uint32 | [StartRecoveryCategory](spell_dbc#startrecoverycategory)           | ID in [SpellCategory.dbc](dbc-spellcategory)                                                          |
| 206    | StartRecoveryTime          | uint32 | [StartRecoveryTime](spell_dbc#startrecoverytime)                   |                                                                                                       |
| 207    | MaxTargetLevel             | uint32 | [MaxTargetLevel](spell_dbc#maxtargetlevel)                         |                                                                                                       |
| 208    | SpellClassSet              | uint32 | [SpellClassSet](spell_dbc#spellclassset)                           |                                                                                                       |
| 209    | SpellClassMask_0           | uint32 | [SpellClassMask_1](spell_dbc#spellclassmask)                       |                                                                                                       |
| 210    | SpellClassMask_1           | uint32 | [SpellClassMask_2](spell_dbc#spellclassmask)                       |                                                                                                       |
| 211    | SpellClassMask_2           | uint32 | [SpellClassMask_3](spell_dbc#spellclassmask)                       |                                                                                                       |
| 212    | MaxTargets                 | uint32 | [MaxTargets](spell_dbc#maxtargets)                                 |                                                                                                       |
| 213    | DefenseType                | uint32 | [DefenseType](spell_dbc#defensetype)                               |                                                                                                       |
| 214    | PreventionType             | uint32 | [PreventionType](spell_dbc#preventiontype)                         |                                                                                                       |
| 215    | StanceBarOrder             | int32  | [StanceBarOrder](spell_dbc#stancebarorder)                         |                                                                                                       |
| 216    | EffectChainAmplitude_0     | float  | [EffectChainAmplitude_1](spell_dbc#effectchainamplitude)           |                                                                                                       |
| 217    | EffectChainAmplitude_1     | float  | [EffectChainAmplitude_2](spell_dbc#effectchainamplitude)           |                                                                                                       |
| 218    | EffectChainAmplitude_2     | float  | [EffectChainAmplitude_3](spell_dbc#effectchainamplitude)           |                                                                                                       |
| 219    | MinFactionID               | uint32 | [MinFactionID](spell_dbc#minfactionid)                             | ID in [Faction.dbc](faction)                                                                          |
| 220    | MinReputation              | uint32 | [MinReputation](spell_dbc#minreputation)                           |                                                                                                       |
| 221    | RequiredAuraVision         | uint32 | [RequiredAuraVision](spell_dbc#requiredauravision)                 |                                                                                                       |
| 222    | RequiredTotemCategoryID_0  | uint32 | [RequiredTotemCategoryID_1](spell_dbc#requiredtotemcategoryid)     | ID in [TotemCategory.dbc](totemcategory)                                                              |
| 223    | RequiredTotemCategoryID_1  | uint32 | [RequiredTotemCategoryID_2](spell_dbc#requiredtotemcategoryid)     | ID in [TotemCategory.dbc](totemcategory)                                                              |
| 224    | RequiredAreasID            | int32  | [RequiredAreasID](spell_dbc#requiredareasid)                       | ID in [AreaGroup.dbc](dbc-areagroup)                                                                  |
| 225    | SchoolMask                 | uint32 | [SchoolMask](spell_dbc#schoolmask)                                 |                                                                                                       |
| 226    | RuneCostID                 | uint32 | [RuneCostID](spell_dbc#runecostid)                                 | ID in [SpellRuneCost.dbc](dbc-spellrunecost)                                                          |
| 227    | SpellMissileID             | uint32 | [SpellMissileID](spell_dbc#spellmissileid)                         | ID in [SpellMissile.dbc](dbc-spellmissile) (1 of the 106 values used here are not in that file)       |
| 228    | PowerDisplayID             | int32  | [PowerDisplayID](spell_dbc#powerdisplayid)                         | ID in [PowerDisplay.dbc](dbc-powerdisplay)                                                            |
| 229    | EffectBonusCoefficient_0   | float  | [EffectBonusMultiplier_1](spell_dbc#effectbonusmultiplier)         |                                                                                                       |
| 230    | EffectBonusCoefficient_1   | float  | [EffectBonusMultiplier_2](spell_dbc#effectbonusmultiplier)         |                                                                                                       |
| 231    | EffectBonusCoefficient_2   | float  | [EffectBonusMultiplier_3](spell_dbc#effectbonusmultiplier)         |                                                                                                       |
| 232    | DescriptionVariablesID     | int32  | [SpellDescriptionVariableID](spell_dbc#spelldescriptionvariableid) | ID in [SpellDescriptionVariables.dbc](dbc-spelldescriptionvariables)                                  |
| 233    | Difficulty                 | uint32 | [SpellDifficultyID](spell_dbc#spelldifficultyid)                   | ID in [SpellDifficulty.dbc](dbc-spelldifficulty) (5 of the 582 values used here are not in that file) |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

## **Category**

| Value | Hex    | Flag          | Comment |
| :---- | :----: | :------------ | :------ |
| 0     | `0x00` | Default       |         |
| 1     | `0x01` | Summon guards |         |
| 2     | `0x02` | Entry         |         |
| 4     | `0x04` | Entry         |         |

## **powerType**

| ID  | Description |
| --- | ----------- |
| 0   | Mana        |
| 1   | Rage        |
| 2   | Focus       |
| 3   | Energy      |

## **RequiresSpellFocus**

Indicates that this spell needs a GO near (e.g. forges).
Required object has the type GAMEOBJECT\_TYPE\_SPELL\_FOCUS and data0 matches the RequiresSpellFocus value.
