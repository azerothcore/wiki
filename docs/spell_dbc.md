# spell\_dbc

[<-Back-to:World](database-world)

**The \`spell\_dbc\` table**

This table contains data regarding serverside spells which are not to be found in Client DBC files.

**Spell\_Effect\_ID**

- Effect\_IDs of [Effect1, Effect2 and/or Effect3](spell-effects-reference).

**Spell\_Effect\_Apply\_Aura_ID**

- EffectApplyAuraName\_IDs of [EffectApplyAuraName1, EffectApplyAuraName2 and/or EffectApplyAuraName3](spell-aura-reference).

**Table Structure**

| Field                         | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| Id                            | INT      | UNSIGNED   | PRI | NO   | NULL    |       |         |
| Dispel                        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| Mechanic                      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| Attributes                    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| AttributesEx                  | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| AttributesEx2                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| AttributesEx3                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| AttributesEx4                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| AttributesEx5                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| Stances                       | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| StancesNot                    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| Targets                       | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| CastingTimeIndex              | TINYINT  | UNSIGNED   |     | NO   | 1       |       |         |
| AuraInterruptFlags            | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| ProcFlags                     | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| ProcChance                    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| ProcCharges                   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| MaxLevel                      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| BaseLevel                     | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| SpellLevel                    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| DurationIndex                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| RangeIndex                    | TINYINT  | UNSIGNED   |     | NO   | 1       |       |         |
| StackAmount                   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EquippedItemClass             | INT      | SIGNED     |     | NO   | -1      |       |         |
| EquippedItemSubClassMask      | INT      | SIGNED     |     | NO   | 0       |       |         |
| EquippedItemInventoryTypeMask | INT      | SIGNED     |     | NO   | 0       |       |         |
| Effect1                       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| Effect2                       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| Effect3                       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectDieSides1               | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectDieSides2               | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectDieSides3               | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel1     | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel2     | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectRealPointsPerLevel3     | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectBasePoints1             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectBasePoints2             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectBasePoints3             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMechanic1               | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectMechanic2               | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectMechanic3               | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetA1        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetA2        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetA3        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetB1        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetB2        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectImplicitTargetB3        | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectRadiusIndex1            | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectRadiusIndex2            | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectRadiusIndex3            | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| EffectApplyAuraName1          | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| EffectApplyAuraName2          | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| EffectApplyAuraName3          | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| EffectAmplitude1              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectAmplitude2              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectAmplitude3              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMultipleValue1          | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectMultipleValue2          | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectMultipleValue3          | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValue1              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValue2              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValue3              | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValueB1             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValueB2             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectMiscValueB3             | INT      | SIGNED     |     | NO   | 0       |       |         |
| EffectTriggerSpell1           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectTriggerSpell2           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectTriggerSpell3           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA1        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA2        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskA3        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB1        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB2        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskB3        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC1        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC2        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EffectSpellClassMaskC3        | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| MaxTargetLevel                | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| SpellFamilyName               | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| SpellFamilyFlags1             | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| SpellFamilyFlags2             | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| SpellFamilyFlags3             | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| MaxAffectedTargets            | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| DmgClass                      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| PreventionType                | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| DmgMultiplier1                | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| DmgMultiplier2                | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| DmgMultiplier3                | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| AreaGroupId                   | INT      | SIGNED     |     | NO   | 0       |       |         |
| SchoolMask                    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| Comment                       | text     | SIGNED     |     | NO   | NULL    |       |         |

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

[Effect1, Effect2 and Effect3. Effect\_ID of the Spell\_Effect. A Spell can only have up to three Spell\_Effects.](spell-effects-reference)

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

[EffectApplyAuraName1, EffectApplyAuraName2 and EffectApplyAuraName3. EffectApplyAuraName\_ID of the Spell\_Effect\_Apply\_Aura.](spell-aura-reference)

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
