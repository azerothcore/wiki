# areapoi\_dbc

[<-Back-to:World](database-world)

**The \`areapoi\_dbc\` table**

This table has the same columns as the client file `AreaPOI.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: areapoi\_dbc's Structure**

| Field                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |          | NO   | PRI | 0       |       |         |
| [Importance](#importance)                 | INT          |          | NO   |     | 0       |       |         |
| [Icon_1](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_2](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_3](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_4](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_5](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_6](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_7](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_8](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [Icon_9](#icon)                           | INT          |          | NO   |     | 0       |       |         |
| [FactionID](#factionid)                   | INT          |          | NO   |     | 0       |       |         |
| [X](#x)                                   | FLOAT        |          | NO   |     | 0       |       |         |
| [Y](#y)                                   | FLOAT        |          | NO   |     | 0       |       |         |
| [Z](#z)                                   | FLOAT        |          | NO   |     | 0       |       |         |
| [ContinentID](#continentid)               | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                           | INT          |          | NO   |     | 0       |       |         |
| [AreaID](#areaid)                         | INT          |          | NO   |     | 0       |       |         |
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
| [Description_Lang_enUS](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enGB](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_koKR](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_frFR](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_deDE](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enCN](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhCN](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enTW](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhTW](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esES](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esMX](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ruRU](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptPT](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptBR](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_itIT](#descriptionlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Unk](#descriptionlang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Mask](#descriptionlang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [WorldStateID](#worldstateid)             | INT          |          | NO   |     | 0       |       |         |
| [WorldMapLink](#worldmaplink)             | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `AreaPOIEntry::id`.

### Importance

The core reads this column into `AreaPOIEntry::icon`.

### Icon

The core reads these columns into `AreaPOIEntry::icon`.

### FactionID

The core reads this column into `AreaPOIEntry::icon`.

### X

The core reads this column into `AreaPOIEntry::x`.

### Y

The core reads this column into `AreaPOIEntry::y`.

### Z

The core reads this column into `AreaPOIEntry::z`.

### ContinentID

The core reads this column into `AreaPOIEntry::mapId`.

### Flags

Not used by the core.

### AreaID

The core reads this column into `AreaPOIEntry::zoneId`.

### Name\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Description\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.

### WorldStateID

The core reads this column into `AreaPOIEntry::worldState`.

### WorldMapLink

Not used by the core.
