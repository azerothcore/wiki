# scalingstatvalues\_dbc

[<-Back-to:World](database-world)

**The \`scalingstatvalues\_dbc\` table**

This table has the same columns as the client file `ScalingStatValues.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: scalingstatvalues\_dbc's Structure**

| Field                                         | Type |     | Null | Key | Default | Extra | Comment |
| :-------------------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                     | INT  |     | NO   | PRI | 0       |       |         |
| [Charlevel](#charlevel)                       | INT  |     | NO   |     | 0       |       |         |
| [ShoulderBudget](#shoulderbudget)             | INT  |     | NO   |     | 0       |       |         |
| [TrinketBudget](#trinketbudget)               | INT  |     | NO   |     | 0       |       |         |
| [WeaponBudget1H](#weaponbudget1h)             | INT  |     | NO   |     | 0       |       |         |
| [RangedBudget](#rangedbudget)                 | INT  |     | NO   |     | 0       |       |         |
| [ClothShoulderArmor](#clothshoulderarmor)     | INT  |     | NO   |     | 0       |       |         |
| [LeatherShoulderArmor](#leathershoulderarmor) | INT  |     | NO   |     | 0       |       |         |
| [MailShoulderArmor](#mailshoulderarmor)       | INT  |     | NO   |     | 0       |       |         |
| [PlateShoulderArmor](#plateshoulderarmor)     | INT  |     | NO   |     | 0       |       |         |
| [WeaponDPS1H](#weapondps1h)                   | INT  |     | NO   |     | 0       |       |         |
| [WeaponDPS2H](#weapondps2h)                   | INT  |     | NO   |     | 0       |       |         |
| [SpellcasterDPS1H](#spellcasterdps1h)         | INT  |     | NO   |     | 0       |       |         |
| [SpellcasterDPS2H](#spellcasterdps2h)         | INT  |     | NO   |     | 0       |       |         |
| [RangedDPS](#rangeddps)                       | INT  |     | NO   |     | 0       |       |         |
| [WandDPS](#wanddps)                           | INT  |     | NO   |     | 0       |       |         |
| [SpellPower](#spellpower)                     | INT  |     | NO   |     | 0       |       |         |
| [PrimaryBudget](#primarybudget)               | INT  |     | NO   |     | 0       |       |         |
| [TertiaryBudget](#tertiarybudget)             | INT  |     | NO   |     | 0       |       |         |
| [ClothCloakArmor](#clothcloakarmor)           | INT  |     | NO   |     | 0       |       |         |
| [ClothChestArmor](#clothchestarmor)           | INT  |     | NO   |     | 0       |       |         |
| [LeatherChestArmor](#leatherchestarmor)       | INT  |     | NO   |     | 0       |       |         |
| [MailChestArmor](#mailchestarmor)             | INT  |     | NO   |     | 0       |       |         |
| [PlateChestArmor](#platechestarmor)           | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The core reads this column into `ScalingStatValuesEntry::Id`.

### Charlevel

The row ID. The core uses it as the index of the rows and stores it in `ScalingStatValuesEntry::Level`.

### ShoulderBudget

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier`.

Comment in the core source: "Multiplier for ScalingStatDistribution"

### TrinketBudget

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier`.

Comment in the core source: "Multiplier for ScalingStatDistribution"

### WeaponBudget1H

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier`.

Comment in the core source: "Multiplier for ScalingStatDistribution"

### RangedBudget

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier`.

Comment in the core source: "Multiplier for ScalingStatDistribution"

### ClothShoulderArmor

The core reads this column into `ScalingStatValuesEntry::armorMod`.

Comment in the core source: "Armor for level"

### LeatherShoulderArmor

The core reads this column into `ScalingStatValuesEntry::armorMod`.

Comment in the core source: "Armor for level"

### MailShoulderArmor

The core reads this column into `ScalingStatValuesEntry::armorMod`.

Comment in the core source: "Armor for level"

### PlateShoulderArmor

The core reads this column into `ScalingStatValuesEntry::armorMod`.

Comment in the core source: "Armor for level"

### WeaponDPS1H

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### WeaponDPS2H

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### SpellcasterDPS1H

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### SpellcasterDPS2H

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### RangedDPS

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### WandDPS

The core reads this column into `ScalingStatValuesEntry::dpsMod`.

Comment in the core source: "DPS mod for level"

### SpellPower

The core reads this column into `ScalingStatValuesEntry::spellPower`.

Comment in the core source: "spell power for level"

### PrimaryBudget

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier2`.

Comment in the core source: "there's data from 3.1 dbc ssdMultiplier[3]"

### TertiaryBudget

The core reads this column into `ScalingStatValuesEntry::ssdMultiplier3`.

### ClothCloakArmor

The core reads this column into `ScalingStatValuesEntry::armorMod2`.

Comment in the core source: "Armor for level"

### ClothChestArmor

The core reads this column into `ScalingStatValuesEntry::armorMod2`.

Comment in the core source: "Armor for level"

### LeatherChestArmor

The core reads this column into `ScalingStatValuesEntry::armorMod2`.

Comment in the core source: "Armor for level"

### MailChestArmor

The core reads this column into `ScalingStatValuesEntry::armorMod2`.

Comment in the core source: "Armor for level"

### PlateChestArmor

The core reads this column into `ScalingStatValuesEntry::armorMod2`.

Comment in the core source: "Armor for level"
