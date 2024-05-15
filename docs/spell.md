---
redirect_from: "/Spell"
---

# Spell

[`Back-to:DBC`](dbc-index.md)

# **Spell.dbc**

This DBC contains most information on all spells.
These values are used by the core and a few spell\_\* tables.

**Version 3.3.5**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## **Structure**

| ID  | Name                          | Type   |
|-----|-------------------------------|--------|
| 0   | Entry                         | uint   |
| 1   | Category                      | uint   |
| 2   | Dispel                        | uint   |
| 3   | Mechanic                      | uint   |
| 4   | Attributes                    | uint   |
| 5   | AttributesEx                  | uint   |
| 6   | AttributesEx2                 | uint   |
| 7   | AttributesEx3                 | uint   |
| 8   | AttributesEx4                 | uint   |
| 9   | AttributesEx5                 | uint   |
| 10  | AttributesEx6                 | uint   |
| 11  | AttributesEx7                 | uint   |
| 12  | Stances                       | uint   |
| 13  | unk_320_2                     | uint   |
| 14  | StancesNot                    | uint   |
| 15  | unk_320_3                     | uint   |
| 16  | Targets                       | uint   |
| 17  | TargetCreatureType            | uint   |
| 18  | requiresSpellFocus            | uint   |
| 19  | FacingCasterFlags             | uint   |
| 20  | CasterAuraState               | uint   |
| 21  | TargetAuraState               | uint   |
| 22  | CasterAuraStateNot            | uint   |
| 23  | TargetAuraStateNot            | uint   |
| 24  | casterAuraSpell               | uint   |
| 25  | targetAuraSpell               | uint   |
| 26  | excludeCasterAuraSpell        | uint   |
| 27  | excludeTargetAuraSpell        | uint   |
| 28  | CastingTimeIndex              | uint   |
| 29  | RecoveryTime                  | uint   |
| 30  | CategoryRecoveryTime          | uint   |
| 31  | InterruptFlags                | uint   |
| 32  | AuraInterruptFlags            | uint   |
| 33  | ChannelInterruptFlags         | uint   |
| 34  | procFlags                     | uint   |
| 35  | procChance                    | uint   |
| 36  | procCharges                   | uint   |
| 37  | maxLevel                      | uint   |
| 38  | baseLevel                     | uint   |
| 39  | spellLevel                    | uint   |
| 40  | DurationIndex                 | uint   |
| 41  | powerType                     | uint   |
| 42  | manaCost                      | uint   |
| 43  | manaCostPerlevel              | uint   |
| 44  | manaPerSecond                 | uint   |
| 45  | manaPerSecondPerLevel         | uint   |
| 46  | rangeIndex                    | uint   |
| 47  | speed                         | float  |
| 48  | modalNextSpell                | uint   |
| 49  | StackAmount                   | uint   |
| 50  | Totem1                        | uint   |
| 51  | Totem2                        | uint   |
| 52  | Reagent1                      | int    |
| 53  | Reagent2                      | int    |
| 54  | Reagent3                      | int    |
| 55  | Reagent4                      | int    |
| 56  | Reagent5                      | int    |
| 57  | Reagent6                      | int    |
| 58  | Reagent7                      | int    |
| 59  | Reagent8                      | int    |
| 60  | ReagentCount1                 | uint   |
| 61  | ReagentCount2                 | uint   |
| 62  | ReagentCount3                 | uint   |
| 63  | ReagentCount4                 | uint   |
| 64  | ReagentCount5                 | uint   |
| 65  | ReagentCount6                 | uint   |
| 66  | ReagentCount7                 | uint   |
| 67  | ReagentCount8                 | uint   |
| 68  | EquippedItemClass             | int    |
| 69  | EquippedItemSubClassMask      | int    |
| 70  | EquippedItemInventoryTypeMask | int    |
| 71  | Effect1                       | uint   |
| 72  | Effect2                       | uint   |
| 73  | Effect3                       | uint   |
| 74  | EffectDieSides1               | int    |
| 75  | EffectDieSides2               | int    |
| 76  | EffectDieSides3               | int    |
| 77  | EffectRealPointsPerLevel1     | float  |
| 78  | EffectRealPointsPerLevel2     | float  |
| 79  | EffectRealPointsPerLevel3     | float  |
| 80  | EffectBasePoints1             | int    |
| 81  | EffectBasePoints2             | int    |
| 82  | EffectBasePoints3             | int    |
| 83  | EffectMechanic1               | uint   |
| 84  | EffectMechanic2               | uint   |
| 85  | EffectMechanic3               | uint   |
| 86  | EffectImplicitTargetA1        | uint   |
| 87  | EffectImplicitTargetA2        | uint   |
| 88  | EffectImplicitTargetA3        | uint   |
| 89  | EffectImplicitTargetB1        | uint   |
| 90  | EffectImplicitTargetB2        | uint   |
| 91  | EffectImplicitTargetB3        | uint   |
| 92  | EffectRadiusIndex1            | uint   |
| 93  | EffectRadiusIndex2            | uint   |
| 94  | EffectRadiusIndex3            | uint   |
| 95  | EffectApplyAuraName1          | uint   |
| 96  | EffectApplyAuraName2          | uint   |
| 97  | EffectApplyAuraName3          | uint   |
| 98  | EffectAmplitude1              | uint   |
| 99  | EffectAmplitude2              | uint   |
| 100 | EffectAmplitude3              | uint   |
| 101 | EffectValueMultiplier1        | float  |
| 102 | EffectValueMultiplier2        | float  |
| 103 | EffectValueMultiplier3        | float  |
| 104 | EffectChainTarget1            | uint   |
| 105 | EffectChainTarget2            | uint   |
| 106 | EffectChainTarget3            | uint   |
| 107 | EffectItemType1               | uint   |
| 108 | EffectItemType2               | uint   |
| 109 | EffectItemType3               | uint   |
| 110 | EffectMiscValue1              | int    |
| 111 | EffectMiscValue2              | int    |
| 112 | EffectMiscValue3              | int    |
| 113 | EffectMiscValueB1             | int    |
| 114 | EffectMiscValueB2             | int    |
| 115 | EffectMiscValueB3             | int    |
| 116 | EffectTriggerSpell1           | uint   |
| 117 | EffectTriggerSpell2           | uint   |
| 118 | EffectTriggerSpell3           | uint   |
| 119 | EffectPointsPerComboPoint1    | float  |
| 120 | EffectPointsPerComboPoint2    | float  |
| 121 | EffectPointsPerComboPoint3    | float  |
| 122 | EffectSpellClassMask1         | flag96 |
| 123 | EffectSpellClassMask2         | flag96 |
| 124 | EffectSpellClassMask3         | flag96 |
| 125 | EffectSpellClassMask4         | flag96 |
| 126 | EffectSpellClassMask5         | flag96 |
| 127 | EffectSpellClassMask6         | flag96 |
| 128 | EffectSpellClassMask7         | flag96 |
| 129 | EffectSpellClassMask8         | flag96 |
| 130 | EffectSpellClassMask9         | flag96 |
| 131 | SpellVisual1                  | uint   |
| 132 | SpellVisual2                  | uint   |
| 133 | SpellIconID                   | uint   |
| 134 | activeIconID                  | uint   |
| 135 | spellPriority                 | uint   |
| 136 | SpellName_0                   | string |
| 137 | SpellName_1                   | string |
| 138 | SpellName_2                   | string |
| 139 | SpellName_3                   | string |
| 140 | SpellName_4                   | string |
| 141 | SpellName_5                   | string |
| 142 | SpellName_6                   | string |
| 143 | SpellName_7                   | string |
| 144 | SpellName_8                   | string |
| 145 | SpellName_9                   | string |
| 146 | SpellName_10                  | string |
| 147 | SpellName_11                  | string |
| 148 | SpellName_12                  | string |
| 149 | SpellName_13                  | string |
| 150 | SpellName_14                  | string |
| 151 | SpellName_15                  | string |
| 152 | SpellNameFlag                 | uint   |
| 153 | Rank_0                        | string |
| 154 | Rank_1                        | string |
| 155 | Rank_2                        | string |
| 156 | Rank_3                        | string |
| 157 | Rank_4                        | string |
| 158 | Rank_5                        | string |
| 159 | Rank_6                        | string |
| 160 | Rank_7                        | string |
| 161 | Rank_8                        | string |
| 162 | Rank_9                        | string |
| 163 | Rank_10                       | string |
| 164 | Rank_11                       | string |
| 165 | Rank_12                       | string |
| 166 | Rank_13                       | string |
| 167 | Rank_14                       | string |
| 168 | Rank_15                       | string |
| 169 | RankFlags                     | uint   |
| 170 | Description_0                 | string |
| 171 | Description_1                 | string |
| 172 | Description_2                 | string |
| 173 | Description_3                 | string |
| 174 | Description_4                 | string |
| 175 | Description_5                 | string |
| 176 | Description_6                 | string |
| 177 | Description_7                 | string |
| 178 | Description_8                 | string |
| 179 | Description_9                 | string |
| 180 | Description_10                | string |
| 181 | Description_11                | string |
| 182 | Description_12                | string |
| 183 | Description_13                | string |
| 184 | Description_14                | string |
| 185 | Description_15                | string |
| 186 | DescriptionFlags              | uint   |
| 187 | ToolTip_0                     | string |
| 188 | ToolTip_1                     | string |
| 189 | ToolTip_2                     | string |
| 190 | ToolTip_3                     | string |
| 191 | ToolTip_4                     | string |
| 192 | ToolTip_5                     | string |
| 193 | ToolTip_6                     | string |
| 194 | ToolTip_7                     | string |
| 195 | ToolTip_8                     | string |
| 196 | ToolTip_9                     | string |
| 197 | ToolTip_10                    | string |
| 198 | ToolTip_11                    | string |
| 199 | ToolTip_12                    | string |
| 200 | ToolTip_13                    | string |
| 201 | ToolTip_14                    | string |
| 202 | ToolTip_15                    | string |
| 203 | ToolTipFlags                  | uint   |
| 204 | ManaCostPercentage            | uint   |
| 205 | StartRecoveryCategory         | uint   |
| 206 | StartRecoveryTime             | uint   |
| 207 | MaxTargetLevel                | uint   |
| 208 | SpellFamilyName               | uint   |
| 209 | SpellFamilyFlagsLow           | flag96 |
| 210 | SpellFamilyFlagsHigh          | flag96 |
| 211 | SpellFamilyFlags2             | flag96 |
| 212 | MaxAffectedTargets            | uint   |
| 213 | DmgClass                      | uint   |
| 214 | PreventionType                | uint   |
| 215 | StanceBarOrder                | uint   |
| 216 | EffectDamageMultiplier1       | float  |
| 217 | EffectDamageMultiplier2       | float  |
| 218 | EffectDamageMultiplier3       | float  |
| 219 | MinFactionId                  | uint   |
| 220 | MinReputation                 | uint   |
| 221 | RequiredAuraVision            | uint   |
| 222 | TotemCategory1                | uint   |
| 223 | TotemCategory2                | uint   |
| 224 | AreaGroupId                   | int    |
| 225 | SchoolMask                    | uint   |
| 226 | runeCostID                    | uint   |
| 227 | spellMissileID                | uint   |
| 228 | PowerDisplayId                | uint   |
| 229 | EffectBonusMultiplier1        | float  |
| 230 | EffectBonusMultiplier2        | float  |
| 231 | EffectBonusMultiplier3        | float  |
| 232 | spellDescriptionVariableID    | uint   |
| 233 | SpellDifficultyId             | uint   |

## **Category**

| ID | Description   |
|----|---------------|
| 0  | Default       |
| 1  | Summon guards |
| 2  | Entry         |
| 4  | Entry         |

## **powerType**

| ID | Description |
|----|-------------|
| 0  | Mana        |
| 1  | Rage        |
| 2  | Focus       |
| 3  | Energy      |

## **RequiresSpellFocus**

Indicates that this spell needs a GO near (e.g. forges).
Required object has the type GAMEOBJECT\_TYPE\_SPELLFOCUS and data0 matches the RequiresSpellFocus value.
