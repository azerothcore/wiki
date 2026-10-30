# chartitles\_dbc

[<-Back-to:World](database-world)

**The \`chartitles\_dbc\` table**

This table has the same columns as the client file `CharTitles.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: chartitles\_dbc's Structure**

| Field                         | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                     | INT          |          | NO   | PRI | 0       |       |         |
| [Condition_ID](#conditionid)  | INT          |          | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Name1_Lang_enUS](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_enGB](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_koKR](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_frFR](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_deDE](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_enCN](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_zhCN](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_enTW](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_zhTW](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_esES](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_esMX](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_ruRU](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_ptPT](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_ptBR](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_itIT](#name1lang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_Unk](#name1lang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name1_Lang_Mask](#name1lang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Mask_ID](#maskid)            | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `CharTitlesEntry::ID`.

Comment in the core source: "title ids, for example in Quest::GetCharTitleId()"

### Condition\_ID

Not used by the core.

Comment in the core source: "Never used by the client. Should be used serverside?"

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk` into `CharTitlesEntry::nameMale`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Name1\_Lang

The core reads `Name1_Lang_enUS` to `Name1_Lang_Unk` into `CharTitlesEntry::nameFemale`. `Name1_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name1_Lang_enUS` = enUS, `Name1_Lang_enGB` = koKR, `Name1_Lang_koKR` = frFR, `Name1_Lang_frFR` = deDE, `Name1_Lang_deDE` = zhCN, `Name1_Lang_enCN` = zhTW, `Name1_Lang_zhCN` = esES, `Name1_Lang_enTW` = esMX, `Name1_Lang_zhTW` = ruRU. The remaining text columns, `Name1_Lang_esES` to `Name1_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Mask\_ID

The core reads this column into `CharTitlesEntry::bit_index`.

Comment in the core source: "used in PLAYER_CHOSEN_TITLE and 1<<index in PLAYER__FIELD_KNOWN_TITLES"
