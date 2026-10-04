# battlemasterlist\_dbc

[<-Back-to:World](database-world)

**The \`battlemasterlist\_dbc\` table**

This table has the same columns as the client file `BattlemasterList.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: battlemasterlist\_dbc's Structure**

| Field                                   | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                               | INT          |          | NO   | PRI | 0       |       |         |
| [MapID_1](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_2](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_3](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_4](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_5](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_6](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_7](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapID_8](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [InstanceType](#instancetype)           | INT          |          | NO   |     | 0       |       |         |
| [GroupsAllowed](#groupsallowed)         | INT          |          | NO   |     | 0       |       |         |
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
| [MaxGroupSize](#maxgroupsize)           | INT          |          | NO   |     | 0       |       |         |
| [HolidayWorldState](#holidayworldstate) | INT          |          | NO   |     | 0       |       |         |
| [Minlevel](#minlevel)                   | INT          |          | NO   |     | 0       |       |         |
| [Maxlevel](#maxlevel)                   | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `BattlemasterListEntry::id`.

### MapID

The core reads these columns into `BattlemasterListEntry::mapid`.

### InstanceType

The core reads this column into `BattlemasterListEntry::type`.

### GroupsAllowed

Not used by the core.

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk` into `BattlemasterListEntry::name`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### MaxGroupSize

The core reads this column into `BattlemasterListEntry::maxGroupSize`.

Comment in the core source: "maxGroupSize, used for checking if queue as group"

### HolidayWorldState

The core reads this column into `BattlemasterListEntry::HolidayWorldStateId`.

### Minlevel

Not used by the core.

### Maxlevel

Not used by the core.

Comment in the core source: "may be max level"
