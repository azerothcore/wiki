# spell\_dbc

[<-Back-to:World](database-world)

**The \`spell\_dbc\` table**

This table has the same columns as Spell.dbc. The core loads it after the DBC file: a row adds a spell that is not in Spell.dbc, for example a serverside spell, or replaces the spell with the same [ID](#id).

The core reads every column in order, so a row must have a value for all of them, even the columns the core does not use. An empty text column keeps the text from the DBC file.

**Table: spell\_dbc's Structure**

| Field                                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                                 | INT          |          | NO   | PRI | 0       |       |         |
| [Category](#category)                                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [DispelType](#dispeltype)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Mechanic](#mechanic)                                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Attributes](#attributes)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx](#attributesex)                             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx2](#attributesex2)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx3](#attributesex3)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx4](#attributesex4)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx5](#attributesex5)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx6](#attributesex6)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AttributesEx7](#attributesex7)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ShapeshiftMask](#shapeshiftmask)                         | BIGINT       | UNSIGNED | NO   |     | 0       |       |         |
| [unk_320_2](#unk320)                                      | INT          |          | NO   |     | 0       |       |         |
| [ShapeshiftExclude](#shapeshiftexclude)                   | BIGINT       | UNSIGNED | NO   |     | 0       |       |         |
| [unk_320_3](#unk320)                                      | INT          |          | NO   |     | 0       |       |         |
| [Targets](#targets)                                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [TargetCreatureType](#targetcreaturetype)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RequiresSpellFocus](#requiresspellfocus)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [FacingCasterFlags](#facingcasterflags)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CasterAuraState](#casteraurastate)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [TargetAuraState](#targetaurastate)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ExcludeCasterAuraState](#excludecasteraurastate)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ExcludeTargetAuraState](#excludetargetaurastate)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CasterAuraSpell](#casterauraspell)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [TargetAuraSpell](#targetauraspell)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ExcludeCasterAuraSpell](#excludecasterauraspell)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ExcludeTargetAuraSpell](#excludetargetauraspell)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CastingTimeIndex](#castingtimeindex)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RecoveryTime](#recoverytime)                             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CategoryRecoveryTime](#categoryrecoverytime)             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [InterruptFlags](#interruptflags)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AuraInterruptFlags](#aurainterruptflags)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ChannelInterruptFlags](#channelinterruptflags)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ProcTypeMask](#proctypemask)                             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ProcChance](#procchance)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ProcCharges](#proccharges)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [MaxLevel](#maxlevel)                                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [BaseLevel](#baselevel)                                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellLevel](#spelllevel)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [DurationIndex](#durationindex)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [PowerType](#powertype)                                   | INT          |          | NO   |     | 0       |       |         |
| [ManaCost](#manacost)                                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ManaCostPerLevel](#manacostperlevel)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ManaPerSecond](#manapersecond)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ManaPerSecondPerLevel](#manapersecondperlevel)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RangeIndex](#rangeindex)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Speed](#speed)                                           | FLOAT        |          | NO   |     | 0       |       |         |
| [ModalNextSpell](#modalnextspell)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CumulativeAura](#cumulativeaura)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Totem_1](#totem)                                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Totem_2](#totem)                                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Reagent_1](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_2](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_3](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_4](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_5](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_6](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_7](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [Reagent_8](#reagent)                                     | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_1](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_2](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_3](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_4](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_5](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_6](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_7](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [ReagentCount_8](#reagentcount)                           | INT          |          | NO   |     | 0       |       |         |
| [EquippedItemClass](#equippeditemclass)                   | INT          |          | NO   |     | 0       |       |         |
| [EquippedItemSubclass](#equippeditemsubclass)             | INT          |          | NO   |     | 0       |       |         |
| [EquippedItemInvTypes](#equippediteminvtypes)             | INT          |          | NO   |     | 0       |       |         |
| [Effect_1](#effect)                                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Effect_2](#effect)                                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Effect_3](#effect)                                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectDieSides_1](#effectdiesides)                       | INT          |          | NO   |     | 0       |       |         |
| [EffectDieSides_2](#effectdiesides)                       | INT          |          | NO   |     | 0       |       |         |
| [EffectDieSides_3](#effectdiesides)                       | INT          |          | NO   |     | 0       |       |         |
| [EffectRealPointsPerLevel_1](#effectrealpointsperlevel)   | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectRealPointsPerLevel_2](#effectrealpointsperlevel)   | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectRealPointsPerLevel_3](#effectrealpointsperlevel)   | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectBasePoints_1](#effectbasepoints)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectBasePoints_2](#effectbasepoints)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectBasePoints_3](#effectbasepoints)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectMechanic_1](#effectmechanic)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectMechanic_2](#effectmechanic)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectMechanic_3](#effectmechanic)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetA_1](#implicittargeta)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetA_2](#implicittargeta)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetA_3](#implicittargeta)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetB_1](#implicittargetb)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetB_2](#implicittargetb)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ImplicitTargetB_3](#implicittargetb)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectRadiusIndex_1](#effectradiusindex)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectRadiusIndex_2](#effectradiusindex)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectRadiusIndex_3](#effectradiusindex)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAura_1](#effectaura)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAura_2](#effectaura)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAura_3](#effectaura)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAuraPeriod_1](#effectauraperiod)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAuraPeriod_2](#effectauraperiod)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectAuraPeriod_3](#effectauraperiod)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectMultipleValue_1](#effectmultiplevalue)             | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectMultipleValue_2](#effectmultiplevalue)             | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectMultipleValue_3](#effectmultiplevalue)             | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectChainTargets_1](#effectchaintargets)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectChainTargets_2](#effectchaintargets)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectChainTargets_3](#effectchaintargets)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectItemType_1](#effectitemtype)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectItemType_2](#effectitemtype)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectItemType_3](#effectitemtype)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectMiscValue_1](#effectmiscvalue)                     | INT          |          | NO   |     | 0       |       |         |
| [EffectMiscValue_2](#effectmiscvalue)                     | INT          |          | NO   |     | 0       |       |         |
| [EffectMiscValue_3](#effectmiscvalue)                     | INT          |          | NO   |     | 0       |       |         |
| [EffectMiscValueB_1](#effectmiscvalueb)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectMiscValueB_2](#effectmiscvalueb)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectMiscValueB_3](#effectmiscvalueb)                   | INT          |          | NO   |     | 0       |       |         |
| [EffectTriggerSpell_1](#effecttriggerspell)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectTriggerSpell_2](#effecttriggerspell)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectTriggerSpell_3](#effecttriggerspell)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectPointsPerCombo_1](#effectpointspercombo)           | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectPointsPerCombo_2](#effectpointspercombo)           | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectPointsPerCombo_3](#effectpointspercombo)           | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectSpellClassMaskA_1](#effectspellclassmaska)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskA_2](#effectspellclassmaska)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskA_3](#effectspellclassmaska)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskB_1](#effectspellclassmaskb)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskB_2](#effectspellclassmaskb)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskB_3](#effectspellclassmaskb)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskC_1](#effectspellclassmaskc)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskC_2](#effectspellclassmaskc)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectSpellClassMaskC_3](#effectspellclassmaskc)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellVisualID_1](#spellvisualid)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellVisualID_2](#spellvisualid)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellIconID](#spelliconid)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ActiveIconID](#activeiconid)                             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellPriority](#spellpriority)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)                               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)                                | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NameSubtext_Lang_enUS](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_enGB](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_koKR](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_frFR](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_deDE](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_enCN](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_zhCN](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_enTW](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_zhTW](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_esES](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_esMX](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_ruRU](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_ptPT](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_ptBR](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_itIT](#namesubtextlang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_Unk](#namesubtextlang)                  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [NameSubtext_Lang_Mask](#namesubtextlang)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Description_Lang_enUS](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_enGB](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_koKR](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_frFR](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_deDE](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_enCN](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhCN](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_enTW](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhTW](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_esES](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_esMX](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_ruRU](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptPT](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptBR](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_itIT](#descriptionlang)                 | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_Unk](#descriptionlang)                  | TEXT         |          | YES  |     | NULL    |       |         |
| [Description_Lang_Mask](#descriptionlang)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AuraDescription_Lang_enUS](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_enGB](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_koKR](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_frFR](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_deDE](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_enCN](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_zhCN](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_enTW](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_zhTW](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_esES](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_esMX](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_ruRU](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_ptPT](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_ptBR](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_itIT](#auradescriptionlang)         | VARCHAR(550) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_Unk](#auradescriptionlang)          | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AuraDescription_Lang_Mask](#auradescriptionlang)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ManaCostPct](#manacostpct)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [StartRecoveryCategory](#startrecoverycategory)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [StartRecoveryTime](#startrecoverytime)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [MaxTargetLevel](#maxtargetlevel)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellClassSet](#spellclassset)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellClassMask_1](#spellclassmask)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellClassMask_2](#spellclassmask)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellClassMask_3](#spellclassmask)                       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [MaxTargets](#maxtargets)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [DefenseType](#defensetype)                               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [PreventionType](#preventiontype)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [StanceBarOrder](#stancebarorder)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EffectChainAmplitude_1](#effectchainamplitude)           | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectChainAmplitude_2](#effectchainamplitude)           | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectChainAmplitude_3](#effectchainamplitude)           | FLOAT        |          | NO   |     | 0       |       |         |
| [MinFactionID](#minfactionid)                             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [MinReputation](#minreputation)                           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RequiredAuraVision](#requiredauravision)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RequiredTotemCategoryID_1](#requiredtotemcategoryid)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RequiredTotemCategoryID_2](#requiredtotemcategoryid)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RequiredAreasID](#requiredareasid)                       | INT          |          | NO   |     | 0       |       |         |
| [SchoolMask](#schoolmask)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RuneCostID](#runecostid)                                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellMissileID](#spellmissileid)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [PowerDisplayID](#powerdisplayid)                         | INT          |          | NO   |     | 0       |       |         |
| [EffectBonusMultiplier_1](#effectbonusmultiplier)         | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectBonusMultiplier_2](#effectbonusmultiplier)         | FLOAT        |          | NO   |     | 0       |       |         |
| [EffectBonusMultiplier_3](#effectbonusmultiplier)         | FLOAT        |          | NO   |     | 0       |       |         |
| [SpellDescriptionVariableID](#spelldescriptionvariableid) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellDifficultyID](#spelldifficultyid)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

Columns that end in `_1`, `_2` or `_3` hold one value per spell effect, and are described together. The core loads the columns that are not marked "Not used by the core", the others only need to be filled in so the row matches the layout of Spell.dbc.

### ID

The ID of the spell. A row with the same ID as a spell in Spell.dbc replaces that spell.

### Category

ID from SpellCategory.dbc. Spells in the same category share a cooldown, see [CategoryRecoveryTime](#categoryrecoverytime).

### DispelType

The dispel type of the spell, which sets what can dispel it. See [Dispel Type](spell-aura-reference#dispel-type).

### Mechanic

The mechanic of the spell, for example stun or root. Used for immunities and diminishing returns. See [Spell Mechanic](spell-aura-reference#spell-mechanic).

### Attributes

Flags from the `SpellAttr0` enum (`SPELL_ATTR0_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx

Flags from the `SpellAttr1` enum (`SPELL_ATTR1_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx2

Flags from the `SpellAttr2` enum (`SPELL_ATTR2_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx3

Flags from the `SpellAttr3` enum (`SPELL_ATTR3_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx4

Flags from the `SpellAttr4` enum (`SPELL_ATTR4_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx5

Flags from the `SpellAttr5` enum (`SPELL_ATTR5_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx6

Flags from the `SpellAttr6` enum (`SPELL_ATTR6_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### AttributesEx7

Flags from the `SpellAttr7` enum (`SPELL_ATTR7_*`) in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h).

### ShapeshiftMask

Bitmask of the shapeshift forms the caster must be in to cast the spell. Each form sets the bit `1 << (form - 1)`, with the form IDs from SpellShapeshiftForm.dbc.

### unk\_320

`unk_320_2` and `unk_320_3`. Not used by the core.

### ShapeshiftExclude

Bitmask of the shapeshift forms the caster can not be in to cast the spell. Uses the same bits as [ShapeshiftMask](#shapeshiftmask).

### Targets

Flags for the kinds of targets the spell can be cast on (`TARGET_FLAG_*` in [`SpellInfo.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Spells/SpellInfo.h)), for example a unit, an item or a location.

### TargetCreatureType

Bitmask of the creature types the spell can target. Each type sets the bit `1 << (type - 1)`, see [Creature Type](spell-aura-reference#creature-type). 0 means any type.

### RequiresSpellFocus

ID from SpellFocusObject.dbc. The caster must be near a gameobject of this spell focus type, for example an anvil or a forge.

### FacingCasterFlags

If 1, a player caster must face the target to cast the spell.

### CasterAuraState

Aura state (`AURA_STATE_*` in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h)) the caster must have to cast the spell.

### TargetAuraState

Aura state the target must have.

### ExcludeCasterAuraState

Aura state the caster must not have.

### ExcludeTargetAuraState

Aura state the target must not have.

### CasterAuraSpell

ID of a spell whose aura the caster must have.

### TargetAuraSpell

ID of a spell whose aura the target must have.

### ExcludeCasterAuraSpell

ID of a spell whose aura the caster must not have.

### ExcludeTargetAuraSpell

ID of a spell whose aura the target must not have.

### CastingTimeIndex

ID from SpellCastTimes.dbc, which sets the cast time. 1 is an instant cast.

### RecoveryTime

Cooldown of the spell in milliseconds.

### CategoryRecoveryTime

Cooldown in milliseconds that is started for all spells in the same [Category](#category).

### InterruptFlags

Flags for what interrupts the cast (`SPELL_INTERRUPT_FLAG_*` in [`SpellDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Spells/SpellDefines.h)), for example movement or taking damage.

### AuraInterruptFlags

Flags for what removes the aura from the target (`AURA_INTERRUPT_FLAG_*` in [`SpellDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Spells/SpellDefines.h)).

### ChannelInterruptFlags

Flags for what interrupts a channeled spell. Uses the same values as [AuraInterruptFlags](#aurainterruptflags).

### ProcTypeMask

Flags for the events that make the aura proc. See [spell\_proc.ProcFlags](spell_proc#procflags).

### ProcChance

Chance in percent that the aura procs.

### ProcCharges

Number of times the aura can proc before it is removed. 0 means no limit.

### MaxLevel

Level after which the spell stops getting stronger from the caster's level.

### BaseLevel

Level the spell's level-based values start from.

### SpellLevel

Level the spell is learned at.

### DurationIndex

ID from SpellDuration.dbc, which sets the duration of the aura.

### PowerType

The power the spell costs. See [Power Type](spell-aura-reference#power-type).

### ManaCost

Flat power cost of the spell.

### ManaCostPerLevel

Power cost added per level of the caster.

### ManaPerSecond

Power drained per second while the spell is channeled.

### ManaPerSecondPerLevel

Power drained per second per level of the caster.

### RangeIndex

ID from SpellRange.dbc, which sets the range of the spell.

### Speed

Travel speed of the spell's missile in yards per second. 0 means the spell hits instantly.

### ModalNextSpell

Not used by the core.

### CumulativeAura

Maximum number of stacks of the aura.

### Totem

`Totem_1` and `Totem_2`. Item IDs of tools the caster must have in their bags to cast the spell.

### Reagent

`Reagent_1` to `Reagent_8`. Item IDs of reagents the spell uses.

### ReagentCount

`ReagentCount_1` to `ReagentCount_8`. Number of each [Reagent](#reagent) the spell uses.

### EquippedItemClass

Item class the caster must have equipped, see [item\_template.class](item_template#class). -1 means no item is needed.

### EquippedItemSubclass

Bitmask of the item subclasses of [EquippedItemClass](#equippeditemclass) that are allowed. Each subclass sets the bit `1 << subclass`.

### EquippedItemInvTypes

Bitmask of the inventory types that are allowed, see [item\_template.InventoryType](item_template#inventorytype). Each type sets the bit `1 << type`.

### Effect

The effect of each of the three spell effects. See [Spell Effects Reference](spell-effects-reference).

### EffectDieSides

Random value added to [EffectBasePoints](#effectbasepoints). The effect's value is between BasePoints + 1 and BasePoints + DieSides.

### EffectRealPointsPerLevel

Value added to the effect per level of the caster above [BaseLevel](#baselevel), up to [MaxLevel](#maxlevel).

### EffectBasePoints

The base value of the effect. The actual value is one higher, see [EffectDieSides](#effectdiesides).

### EffectMechanic

Mechanic of the effect. Overrides the spell's [Mechanic](#mechanic) for this effect.

### ImplicitTargetA

Target type of the effect (`TARGET_*` in [`SharedDefines.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/SharedDefines.h)), for example the caster or the selected target.

### ImplicitTargetB

Second target type of the effect, for example the units in an area around the target selected by [ImplicitTargetA](#implicittargeta).

### EffectRadiusIndex

ID from SpellRadius.dbc, which sets the radius of area effects.

### EffectAura

The aura applied by an Apply Aura effect. See [Spell Aura Reference](spell-aura-reference).

### EffectAuraPeriod

Time in milliseconds between the ticks of a periodic aura.

### EffectMultipleValue

Multiplier for effects that convert a value, for example the health gained per point of mana drained.

### EffectChainTargets

Number of targets a chain effect can jump to.

### EffectItemType

Item ID created by a Create Item effect.

### EffectMiscValue

Extra value used by the effect or aura, for example a creature entry or a school mask. See [Spell Effects Reference](spell-effects-reference) and [Spell Aura Reference](spell-aura-reference).

### EffectMiscValueB

Second extra value used by the effect or aura.

### EffectTriggerSpell

ID of a spell the effect triggers.

### EffectPointsPerCombo

Value added to the effect per combo point.

### EffectSpellClassMaskA

First 32 bits of the spell family mask the effect affects. Together with [EffectSpellClassMaskB](#effectspellclassmaskb) and [EffectSpellClassMaskC](#effectspellclassmaskc) it selects the spells of the same [SpellClassSet](#spellclassset) that an aura modifies.

### EffectSpellClassMaskB

Second 32 bits of the spell family mask. See [EffectSpellClassMaskA](#effectspellclassmaska).

### EffectSpellClassMaskC

Third 32 bits of the spell family mask. See [EffectSpellClassMaskA](#effectspellclassmaska).

### SpellVisualID

`SpellVisualID_1` and `SpellVisualID_2`. IDs from SpellVisual.dbc for the visual effects of the spell.

### SpellIconID

ID from SpellIcon.dbc for the icon of the spell.

### ActiveIconID

ID from SpellIcon.dbc for the icon shown while the spell is active.

### SpellPriority

Not used by the core.

### Name\_Lang

`Name_Lang_enUS` to `Name_Lang_Unk` and `Name_Lang_Mask`. The name of the spell. The mask is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### NameSubtext\_Lang

`NameSubtext_Lang_enUS` to `NameSubtext_Lang_Unk` and `NameSubtext_Lang_Mask`. The rank text of the spell, for example "Rank 1". The mask is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `NameSubtext_Lang_enUS` = enUS, `NameSubtext_Lang_enGB` = koKR, `NameSubtext_Lang_koKR` = frFR, `NameSubtext_Lang_frFR` = deDE, `NameSubtext_Lang_deDE` = zhCN, `NameSubtext_Lang_enCN` = zhTW, `NameSubtext_Lang_zhCN` = esES, `NameSubtext_Lang_enTW` = esMX, `NameSubtext_Lang_zhTW` = ruRU. The remaining text columns, `NameSubtext_Lang_esES` to `NameSubtext_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Description\_Lang

`Description_Lang_enUS` to `Description_Lang_Unk` and `Description_Lang_Mask`. The description of the spell. Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.

### AuraDescription\_Lang

`AuraDescription_Lang_enUS` to `AuraDescription_Lang_Unk` and `AuraDescription_Lang_Mask`. The tooltip of the aura. Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `AuraDescription_Lang_enUS` = enUS, `AuraDescription_Lang_enGB` = koKR, `AuraDescription_Lang_koKR` = frFR, `AuraDescription_Lang_frFR` = deDE, `AuraDescription_Lang_deDE` = zhCN, `AuraDescription_Lang_enCN` = zhTW, `AuraDescription_Lang_zhCN` = esES, `AuraDescription_Lang_enTW` = esMX, `AuraDescription_Lang_zhTW` = ruRU. The remaining text columns, `AuraDescription_Lang_esES` to `AuraDescription_Lang_Unk`, are not supported in 3.3.5a and are not used.

### ManaCostPct

Power cost in percent of the caster's base power. Used instead of [ManaCost](#manacost) if set.

### StartRecoveryCategory

Global cooldown category of the spell. 133 is the normal global cooldown.

### StartRecoveryTime

Global cooldown the spell starts, in milliseconds.

### MaxTargetLevel

Highest level a target can have to be affected by the spell. 0 means no limit.

### SpellClassSet

The spell family, usually the class the spell belongs to. See [spell\_proc.SpellFamilyName](spell_proc#spellfamilyname).

### SpellClassMask

`SpellClassMask_1` to `SpellClassMask_3`. The 96 bit spell family mask of the spell. Auras use it together with [SpellClassSet](#spellclassset) to select the spells they modify, see [EffectSpellClassMaskA](#effectspellclassmaska).

### MaxTargets

Maximum number of targets the spell can hit. 0 means no limit.

### DefenseType

| Value | Damage class                  |
| ----- | ----------------------------- |
| 0     | None                          |
| 1     | Magic                         |
| 2     | Melee                         |
| 3     | Ranged                        |

Sets how the spell hits, for example whether it can be dodged or resisted.

### PreventionType

| Value | Prevention type                                   |
| ----- | ------------------------------------------------- |
| 0     | None                                              |
| 1     | Silence. The spell can not be cast while silenced. |
| 2     | Pacify. The spell can not be cast while pacified. |

### StanceBarOrder

Not used by the core.

### EffectChainAmplitude

Multiplier applied to the effect's value each time a chain effect jumps to the next target.

### MinFactionID

Not used by the core.

### MinReputation

Not used by the core.

### RequiredAuraVision

Not used by the core.

### RequiredTotemCategoryID

`RequiredTotemCategoryID_1` and `RequiredTotemCategoryID_2`. IDs from TotemCategory.dbc of tools the caster must have, for example a Blacksmith Hammer.

### RequiredAreasID

ID from AreaGroup.dbc. The spell can only be cast in these areas. 0 means anywhere.

### SchoolMask

The school of the spell. See [School Mask](spell-aura-reference#school-mask).

### RuneCostID

ID from SpellRuneCost.dbc, which sets the rune cost of Death Knight spells.

### SpellMissileID

Not used by the core.

### PowerDisplayID

Not used by the core.

### EffectBonusMultiplier

Multiplier for the bonus the effect gets from spell power or attack power.

### SpellDescriptionVariableID

Not used by the core.

### SpellDifficultyID

Not used by the core. Spell difficulties are set in [spelldifficulty\_dbc](spelldifficulty_dbc).
