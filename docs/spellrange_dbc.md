# spellrange\_dbc

[<-Back-to:World](database-world)

**The \`spellrange\_dbc\` table**

This table has the same columns as the client file `SpellRange.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellrange\_dbc's Structure**

| Field                                               | Type  |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                           | INT   |          | NO   | PRI | 0       |       |         |
| [RangeMin_1](#rangemin)                             | FLOAT |          | NO   |     | 0       |       |         |
| [RangeMin_2](#rangemin)                             | FLOAT |          | NO   |     | 0       |       |         |
| [RangeMax_1](#rangemax)                             | FLOAT |          | NO   |     | 0       |       |         |
| [RangeMax_2](#rangemax)                             | FLOAT |          | NO   |     | 0       |       |         |
| [Flags](#flags)                                     | INT   |          | NO   |     | 0       |       |         |
| [DisplayName_Lang_enUS](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enGB](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_koKR](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_frFR](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_deDE](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enCN](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_zhCN](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_enTW](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_zhTW](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_esES](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_esMX](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ruRU](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ptPT](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_ptBR](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_itIT](#displaynamelang)           | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_Unk](#displaynamelang)            | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayName_Lang_Mask](#displaynamelang)           | INT   | UNSIGNED | NO   |     | 0       |       |         |
| [DisplayNameShort_Lang_enUS](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_enGB](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_koKR](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_frFR](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_deDE](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_enCN](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_zhCN](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_enTW](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_zhTW](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_esES](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_esMX](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_ruRU](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_ptPT](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_ptBR](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_itIT](#displaynameshortlang) | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_Unk](#displaynameshortlang)  | TEXT  |          | YES  |     | NULL    |       |         |
| [DisplayNameShort_Lang_Mask](#displaynameshortlang) | INT   | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellRangeEntry::ID`.

### RangeMin

The core reads these columns into `SpellRangeEntry::RangeMin`.

Comment in the core source: "[0] Hostile [1] Friendly"

### RangeMax

The core reads these columns into `SpellRangeEntry::RangeMax`.

Comment in the core source: "[0] Hostile [1] Friendly"

### Flags

The core reads this column into `SpellRangeEntry::Flags`.

### DisplayName\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `DisplayName_Lang_enUS` = enUS, `DisplayName_Lang_enGB` = koKR, `DisplayName_Lang_koKR` = frFR, `DisplayName_Lang_frFR` = deDE, `DisplayName_Lang_deDE` = zhCN, `DisplayName_Lang_enCN` = zhTW, `DisplayName_Lang_zhCN` = esES, `DisplayName_Lang_enTW` = esMX, `DisplayName_Lang_zhTW` = ruRU. The remaining text columns, `DisplayName_Lang_esES` to `DisplayName_Lang_Unk`, are not supported in 3.3.5a and are not used.

### DisplayNameShort\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `DisplayNameShort_Lang_enUS` = enUS, `DisplayNameShort_Lang_enGB` = koKR, `DisplayNameShort_Lang_koKR` = frFR, `DisplayNameShort_Lang_frFR` = deDE, `DisplayNameShort_Lang_deDE` = zhCN, `DisplayNameShort_Lang_enCN` = zhTW, `DisplayNameShort_Lang_zhCN` = esES, `DisplayNameShort_Lang_enTW` = esMX, `DisplayNameShort_Lang_zhTW` = ruRU. The remaining text columns, `DisplayNameShort_Lang_esES` to `DisplayNameShort_Lang_Unk`, are not supported in 3.3.5a and are not used.
