# spellitemenchantment\_dbc

[<-Back-to:World](database-world)

**The \`spellitemenchantment\_dbc\` table**

This table has the same columns as the client file `SpellItemEnchantment.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellitemenchantment\_dbc's Structure**

| Field                                   | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                               | INT          |          | NO   | PRI | 0       |       |         |
| [Charges](#charges)                     | INT          |          | NO   |     | 0       |       |         |
| [Effect_1](#effect)                     | INT          |          | NO   |     | 0       |       |         |
| [Effect_2](#effect)                     | INT          |          | NO   |     | 0       |       |         |
| [Effect_3](#effect)                     | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMin_1](#effectpointsmin)   | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMin_2](#effectpointsmin)   | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMin_3](#effectpointsmin)   | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMax_1](#effectpointsmax)   | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMax_2](#effectpointsmax)   | INT          |          | NO   |     | 0       |       |         |
| [EffectPointsMax_3](#effectpointsmax)   | INT          |          | NO   |     | 0       |       |         |
| [EffectArg_1](#effectarg)               | INT          |          | NO   |     | 0       |       |         |
| [EffectArg_2](#effectarg)               | INT          |          | NO   |     | 0       |       |         |
| [EffectArg_3](#effectarg)               | INT          |          | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)              | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ItemVisual](#itemvisual)               | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                         | INT          |          | NO   |     | 0       |       |         |
| [Src_ItemID](#srcitemid)                | INT          |          | NO   |     | 0       |       |         |
| [Condition_Id](#conditionid)            | INT          |          | NO   |     | 0       |       |         |
| [RequiredSkillID](#requiredskillid)     | INT          |          | NO   |     | 0       |       |         |
| [RequiredSkillRank](#requiredskillrank) | INT          |          | NO   |     | 0       |       |         |
| [MinLevel](#minlevel)                   | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellItemEnchantmentEntry::ID`.

### Charges

The core reads this column into `SpellItemEnchantmentEntry::charges`.

### Effect

The core reads these columns into `SpellItemEnchantmentEntry::type`.

### EffectPointsMin

The core reads these columns into `SpellItemEnchantmentEntry::amount`.

### EffectPointsMax

Not used by the core.

### EffectArg

The core reads these columns into `SpellItemEnchantmentEntry::spellid`.

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk` into `SpellItemEnchantmentEntry::description`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

Comment in the core source: "name flags"

### ItemVisual

The core reads this column into `SpellItemEnchantmentEntry::aura_id`.

### Flags

The core reads this column into `SpellItemEnchantmentEntry::slot`.

### Src\_ItemID

The core reads this column into `SpellItemEnchantmentEntry::GemID`.

### Condition\_Id

The core reads this column into `SpellItemEnchantmentEntry::EnchantmentCondition`.

### RequiredSkillID

The core reads this column into `SpellItemEnchantmentEntry::requiredSkill`.

### RequiredSkillRank

The core reads this column into `SpellItemEnchantmentEntry::requiredSkillValue`.

### MinLevel

The core reads this column into `SpellItemEnchantmentEntry::requiredLevel`.
