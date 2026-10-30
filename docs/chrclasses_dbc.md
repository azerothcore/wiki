# chrclasses\_dbc

[<-Back-to:World](database-world)

**The \`chrclasses\_dbc\` table**

This table has the same columns as the client file `ChrClasses.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: chrclasses\_dbc's Structure**

| Field                                       | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                   | INT          |          | NO   | PRI | 0       |       |         |
| [Field01](#field01)                         | INT          |          | NO   |     | 0       |       |         |
| [DisplayPower](#displaypower)               | INT          |          | NO   |     | 0       |       |         |
| [PetNameToken](#petnametoken)               | INT          |          | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)                  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Name_Female_Lang_enUS](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_enGB](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_koKR](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_frFR](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_deDE](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_enCN](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_zhCN](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_enTW](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_zhTW](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_esES](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_esMX](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_ruRU](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_ptPT](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_ptBR](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_itIT](#namefemalelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_Unk](#namefemalelang)     | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Female_Lang_Mask](#namefemalelang)    | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Name_Male_Lang_enUS](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_enGB](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_koKR](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_frFR](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_deDE](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_enCN](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_zhCN](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_enTW](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_zhTW](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_esES](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_esMX](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_ruRU](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_ptPT](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_ptBR](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_itIT](#namemalelang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_Unk](#namemalelang)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Male_Lang_Mask](#namemalelang)        | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Filename](#filename)                       | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SpellClassSet](#spellclassset)             | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                             | INT          |          | NO   |     | 0       |       |         |
| [CinematicSequenceID](#cinematicsequenceid) | INT          |          | NO   |     | 0       |       |         |
| [Required_Expansion](#requiredexpansion)    | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Field01

Not used by the core.

### DisplayPower

The core reads this column.

### PetNameToken

Not used by the core.

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Name\_Female\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Female_Lang_enUS` = enUS, `Name_Female_Lang_enGB` = koKR, `Name_Female_Lang_koKR` = frFR, `Name_Female_Lang_frFR` = deDE, `Name_Female_Lang_deDE` = zhCN, `Name_Female_Lang_enCN` = zhTW, `Name_Female_Lang_zhCN` = esES, `Name_Female_Lang_enTW` = esMX, `Name_Female_Lang_zhTW` = ruRU. The remaining text columns, `Name_Female_Lang_esES` to `Name_Female_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Name\_Male\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Male_Lang_enUS` = enUS, `Name_Male_Lang_enGB` = koKR, `Name_Male_Lang_koKR` = frFR, `Name_Male_Lang_frFR` = deDE, `Name_Male_Lang_deDE` = zhCN, `Name_Male_Lang_enCN` = zhTW, `Name_Male_Lang_zhCN` = esES, `Name_Male_Lang_enTW` = esMX, `Name_Male_Lang_zhTW` = ruRU. The remaining text columns, `Name_Male_Lang_esES` to `Name_Male_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Filename

Not used by the core.

### SpellClassSet

The core reads this column.

### Flags

Not used by the core.

### CinematicSequenceID

The core reads this column.

### Required\_Expansion

The core reads this column.
