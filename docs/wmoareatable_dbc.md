# wmoareatable\_dbc

[<-Back-to:World](database-world)

**The \`wmoareatable\_dbc\` table**

This table has the same columns as the client file `WMOAreaTable.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: wmoareatable\_dbc's Structure**

| Field                                                       | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                                   | INT          |          | NO   | PRI | 0       |       |         |
| [WMOID](#wmoid)                                             | INT          |          | NO   |     | 0       |       |         |
| [NameSetID](#namesetid)                                     | INT          |          | NO   |     | 0       |       |         |
| [WMOGroupID](#wmogroupid)                                   | INT          |          | NO   |     | 0       |       |         |
| [SoundProviderPref](#soundproviderpref)                     | INT          |          | NO   |     | 0       |       |         |
| [SoundProviderPrefUnderwater](#soundproviderprefunderwater) | INT          |          | NO   |     | 0       |       |         |
| [AmbienceID](#ambienceid)                                   | INT          |          | NO   |     | 0       |       |         |
| [ZoneMusic](#zonemusic)                                     | INT          |          | NO   |     | 0       |       |         |
| [IntroSound](#introsound)                                   | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                                             | INT          |          | NO   |     | 0       |       |         |
| [AreaTableID](#areatableid)                                 | INT          |          | NO   |     | 0       |       |         |
| [AreaName_Lang_enUS](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enGB](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_koKR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_frFR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_deDE](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enCN](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_zhCN](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enTW](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_zhTW](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_esES](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_esMX](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ruRU](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ptPT](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ptBR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_itIT](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_Unk](#areanamelang)                          | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_Mask](#areanamelang)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `WMOAreaTableEntry::Id`.

### WMOID

The core reads this column into `WMOAreaTableEntry::rootId`.

Comment in the core source: "used in root WMO"

### NameSetID

The core reads this column into `WMOAreaTableEntry::adtId`.

Comment in the core source: "used in adt file"

### WMOGroupID

The core reads this column into `WMOAreaTableEntry::groupId`.

Comment in the core source: "used in group WMO"

### SoundProviderPref

Not used by the core.

### SoundProviderPrefUnderwater

Not used by the core.

### AmbienceID

Not used by the core.

### ZoneMusic

Not used by the core.

### IntroSound

Not used by the core.

### Flags

The core reads this column into `WMOAreaTableEntry::Flags`.

Comment in the core source: "used for indoor/outdoor determination"

### AreaTableID

The core reads this column into `WMOAreaTableEntry::areaId`.

Comment in the core source: "link to AreaTableEntry.ID"

### AreaName\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `AreaName_Lang_enUS` = enUS, `AreaName_Lang_enGB` = koKR, `AreaName_Lang_koKR` = frFR, `AreaName_Lang_frFR` = deDE, `AreaName_Lang_deDE` = zhCN, `AreaName_Lang_enCN` = zhTW, `AreaName_Lang_zhCN` = esES, `AreaName_Lang_enTW` = esMX, `AreaName_Lang_zhTW` = ruRU. The remaining text columns, `AreaName_Lang_esES` to `AreaName_Lang_Unk`, are not supported in 3.3.5a and are not used.
