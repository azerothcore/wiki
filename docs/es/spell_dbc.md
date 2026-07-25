# spell\_dbc

[<-Volver a: World](database-world)

**Tabla \`spell\_dbc\`**

Esta tabla contiene datos sobre hechizos del lado del servidor que no se encuentran en los archivos DBC del cliente.

**Spell\_Effect\_ID**

- Effect\_IDs de [Effect1, Effect2 y/o Effect3](spell-effects-reference).

**Spell\_Effect\_Apply\_Aura_ID**

- EffectApplyAuraName\_IDs de [EffectApplyAuraName1, EffectApplyAuraName2 y/o EffectApplyAuraName3](spell-aura-reference).

**Estructura**

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

**Descripción de los campos**

### Id

El id del hechizo.

### Dispel

`campo-sin-descripción|2`

### Mechanic

`campo-sin-descripción|3`

### Attributes

`campo-sin-descripción|4`

### AttributesEx

`campo-sin-descripción|5`

### Stances

`campo-sin-descripción|6`

### StancesNot

`campo-sin-descripción|7`

### Targets

`campo-sin-descripción|8`

### CastingTimeIndex

`campo-sin-descripción|9`

### AuraInterruptFlags

`campo-sin-descripción|10`

### ProcFlags

`campo-sin-descripción|11`

### ProcChance

`campo-sin-descripción|12`

### ProcCharges

`campo-sin-descripción|13`

### MaxLevel

`campo-sin-descripción|14`

### BaseLevel

`campo-sin-descripción|15`

### SpellLevel

`campo-sin-descripción|16`

### DurationIndex

`campo-sin-descripción|17`

### RangeIndex

`campo-sin-descripción|18`

### StackAmount

`campo-sin-descripción|19`

### EquippedItemClass

`campo-sin-descripción|20`

### EquippedItemSubClassMask

`campo-sin-descripción|21`

### EquippedItemInventoryTypeMask

`campo-sin-descripción|22`

### Effect

[Effect1, Effect2 y Effect3. Effect\_ID del Spell\_Effect. Un hechizo solo puede tener hasta tres Spell\_Effects.](spell-effects-reference)

### EffectDieSides

`campo-sin-descripción|24`

### EffectRealPointsPerLevel

`campo-sin-descripción|25`

### EffectBasePoints

`campo-sin-descripción|26`

### EffectMechanic

`campo-sin-descripción|27`

### EffectImplicitTargetA

`campo-sin-descripción|28`

### EffectImplicitTargetB

`campo-sin-descripción|29`

### EffectRadiusIndex

`campo-sin-descripción|30`

### EffectApplyAuraName

[EffectApplyAuraName1, EffectApplyAuraName2 y EffectApplyAuraName3. EffectApplyAuraName\_ID del Spell\_Effect\_Apply\_Aura.](spell-aura-reference)

### EffectAmplitude

`campo-sin-descripción|32`

### EffectMultipleValue

`campo-sin-descripción|33`

### EffectMiscValue

`campo-sin-descripción|34`

### EffectMiscValueB

`campo-sin-descripción|35`

### EffectTriggerSpell

`campo-sin-descripción|36`

### EffectSpellClassMaskA

`campo-sin-descripción|37`

### EffectSpellClassMaskB

`campo-sin-descripción|38`

### EffectSpellClassMaskC

`campo-sin-descripción|39`

### MaxTargetLevel

`campo-sin-descripción|40`

### SpellFamilyName

`campo-sin-descripción|41`

### SpellFamilyFlags

`campo-sin-descripción|42`

### MaxAffectedTarget

`campo-sin-descripción|43`

### DmgClass

`campo-sin-descripción|44`

### PreventionType

`campo-sin-descripción|45`

### DmgMultiplier

`campo-sin-descripción|46`

### AreaGroupId

`campo-sin-descripción|47`

### SchoolMask

`campo-sin-descripción|48`

### Comment

`campo-sin-descripción|49`
