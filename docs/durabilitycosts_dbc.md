# durabilitycosts\_dbc

[<-Back-to:World](database-world)

**The \`durabilitycosts\_dbc\` table**

This table has the same columns as the client file `DurabilityCosts.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: durabilitycosts\_dbc's Structure**

| Field                                        | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                    | INT  |     | NO   | PRI | 0       |       |         |
| [WeaponSubClassCost_1](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_2](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_3](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_4](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_5](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_6](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_7](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_8](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_9](#weaponsubclasscost)  | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_10](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_11](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_12](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_13](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_14](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_15](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_16](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_17](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_18](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_19](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_20](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [WeaponSubClassCost_21](#weaponsubclasscost) | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_1](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_2](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_3](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_4](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_5](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_6](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_7](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |
| [ArmorSubClassCost_8](#armorsubclasscost)    | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `DurabilityCostsEntry::Itemlvl`.

### WeaponSubClassCost

The core reads these columns into `DurabilityCostsEntry::multiplier`.

### ArmorSubClassCost

The core reads these columns into `DurabilityCostsEntry::multiplier`.
