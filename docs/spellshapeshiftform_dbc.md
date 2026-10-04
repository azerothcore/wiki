# spellshapeshiftform\_dbc

[<-Back-to:World](database-world)

**The \`spellshapeshiftform\_dbc\` table**

This table has the same columns as the client file `SpellShapeshiftForm.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellshapeshiftform\_dbc's Structure**

| Field                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |          | NO   | PRI | 0       |       |         |
| [BonusActionBar](#bonusactionbar)         | INT          |          | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)               | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)                | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Flags](#flags)                           | INT          |          | NO   |     | 0       |       |         |
| [CreatureType](#creaturetype)             | INT          |          | NO   |     | 0       |       |         |
| [AttackIconID](#attackiconid)             | INT          |          | NO   |     | 0       |       |         |
| [CombatRoundTime](#combatroundtime)       | INT          |          | NO   |     | 0       |       |         |
| [CreatureDisplayID_1](#creaturedisplayid) | INT          |          | NO   |     | 0       |       |         |
| [CreatureDisplayID_2](#creaturedisplayid) | INT          |          | NO   |     | 0       |       |         |
| [CreatureDisplayID_3](#creaturedisplayid) | INT          |          | NO   |     | 0       |       |         |
| [CreatureDisplayID_4](#creaturedisplayid) | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_1](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_2](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_3](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_4](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_5](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_6](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_7](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |
| [PresetSpellID_8](#presetspellid)         | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellShapeshiftFormEntry::ID`.

### BonusActionBar

Not used by the core.

### Name\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Flags

The core reads this column into `SpellShapeshiftFormEntry::flags1`.

### CreatureType

The core reads this column into `SpellShapeshiftFormEntry::creatureType`.

Comment in the core source: "<= 0 humanoid, other normal creature types"

### AttackIconID

Not used by the core.

### CombatRoundTime

The core reads this column into `SpellShapeshiftFormEntry::attackSpeed`.

### CreatureDisplayID

The core reads `CreatureDisplayID_1` and `CreatureDisplayID_2`. `CreatureDisplayID_3` and `CreatureDisplayID_4` are not used by the core.

Comment in the core source: "alliance modelid; horde modelid (only one form)"

### PresetSpellID

The core reads these columns into `SpellShapeshiftFormEntry::stanceSpell`.
