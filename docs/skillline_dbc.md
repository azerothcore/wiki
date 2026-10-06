# skillline\_dbc

[<-Back-to:World](database-world)

**The \`skillline\_dbc\` table**

This table has the same columns as the client file `SkillLine.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: skillline\_dbc's Structure**

| Field                                         | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                     | INT          |          | NO   | PRI | 0       |       |         |
| [CategoryID](#categoryid)                     | INT          |          | NO   |     | 0       |       |         |
| [SkillCostsID](#skillcostsid)                 | INT          |          | NO   |     | 0       |       |         |
| [DisplayName_Lang_enUS](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enGB](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_koKR](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_frFR](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_deDE](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enCN](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_zhCN](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enTW](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_zhTW](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_esES](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_esMX](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ruRU](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ptPT](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ptBR](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_itIT](#displaynamelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_Unk](#displaynamelang)      | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_Mask](#displaynamelang)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Description_Lang_enUS](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enGB](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_koKR](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_frFR](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_deDE](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enCN](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhCN](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enTW](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhTW](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esES](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esMX](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ruRU](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptPT](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptBR](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_itIT](#descriptionlang)     | VARCHAR(300) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Unk](#descriptionlang)      | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Mask](#descriptionlang)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SpellIconID](#spelliconid)                   | INT          |          | NO   |     | 0       |       |         |
| [AlternateVerb_Lang_enUS](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_enGB](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_koKR](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_frFR](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_deDE](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_enCN](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_zhCN](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_enTW](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_zhTW](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_esES](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_esMX](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_ruRU](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_ptPT](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_ptBR](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_itIT](#alternateverblang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_Unk](#alternateverblang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AlternateVerb_Lang_Mask](#alternateverblang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [CanLink](#canlink)                           | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SkillLineEntry::id`.

### CategoryID

The core reads this column into `SkillLineEntry::categoryId`.

### SkillCostsID

Not used by the core.

### DisplayName\_Lang

The core reads `DisplayName_Lang_enUS` to `DisplayName_Lang_Unk` into `SkillLineEntry::name`. `DisplayName_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `DisplayName_Lang_enUS` = enUS, `DisplayName_Lang_enGB` = koKR, `DisplayName_Lang_koKR` = frFR, `DisplayName_Lang_frFR` = deDE, `DisplayName_Lang_deDE` = zhCN, `DisplayName_Lang_enCN` = zhTW, `DisplayName_Lang_zhCN` = esES, `DisplayName_Lang_enTW` = esMX, `DisplayName_Lang_zhTW` = ruRU. The remaining text columns, `DisplayName_Lang_esES` to `DisplayName_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Description\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.

### SpellIconID

The core reads this column into `SkillLineEntry::spellIcon`.

### AlternateVerb\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `AlternateVerb_Lang_enUS` = enUS, `AlternateVerb_Lang_enGB` = koKR, `AlternateVerb_Lang_koKR` = frFR, `AlternateVerb_Lang_frFR` = deDE, `AlternateVerb_Lang_deDE` = zhCN, `AlternateVerb_Lang_enCN` = zhTW, `AlternateVerb_Lang_zhCN` = esES, `AlternateVerb_Lang_enTW` = esMX, `AlternateVerb_Lang_zhTW` = ruRU. The remaining text columns, `AlternateVerb_Lang_esES` to `AlternateVerb_Lang_Unk`, are not supported in 3.3.5a and are not used.

### CanLink

The core reads this column into `SkillLineEntry::canLink`.

Comment in the core source: "(prof. with recipes"
