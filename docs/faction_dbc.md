# faction\_dbc

[<-Back-to:World](database-world)

**The \`faction\_dbc\` table**

This table has the same columns as the client file `Faction.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: faction\_dbc's Structure**

| Field                                         | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                     | INT          |          | NO   | PRI | 0       |       |         |
| [ReputationIndex](#reputationindex)           | INT          |          | NO   |     | 0       |       |         |
| [ReputationRaceMask_1](#reputationracemask)   | INT          |          | NO   |     | 0       |       |         |
| [ReputationRaceMask_2](#reputationracemask)   | INT          |          | NO   |     | 0       |       |         |
| [ReputationRaceMask_3](#reputationracemask)   | INT          |          | NO   |     | 0       |       |         |
| [ReputationRaceMask_4](#reputationracemask)   | INT          |          | NO   |     | 0       |       |         |
| [ReputationClassMask_1](#reputationclassmask) | INT          |          | NO   |     | 0       |       |         |
| [ReputationClassMask_2](#reputationclassmask) | INT          |          | NO   |     | 0       |       |         |
| [ReputationClassMask_3](#reputationclassmask) | INT          |          | NO   |     | 0       |       |         |
| [ReputationClassMask_4](#reputationclassmask) | INT          |          | NO   |     | 0       |       |         |
| [ReputationBase_1](#reputationbase)           | INT          |          | NO   |     | 0       |       |         |
| [ReputationBase_2](#reputationbase)           | INT          |          | NO   |     | 0       |       |         |
| [ReputationBase_3](#reputationbase)           | INT          |          | NO   |     | 0       |       |         |
| [ReputationBase_4](#reputationbase)           | INT          |          | NO   |     | 0       |       |         |
| [ReputationFlags_1](#reputationflags)         | INT          |          | NO   |     | 0       |       |         |
| [ReputationFlags_2](#reputationflags)         | INT          |          | NO   |     | 0       |       |         |
| [ReputationFlags_3](#reputationflags)         | INT          |          | NO   |     | 0       |       |         |
| [ReputationFlags_4](#reputationflags)         | INT          |          | NO   |     | 0       |       |         |
| [ParentFactionID](#parentfactionid)           | INT          |          | NO   |     | 0       |       |         |
| [ParentFactionMod_1](#parentfactionmod)       | FLOAT        |          | NO   |     | 0       |       |         |
| [ParentFactionMod_2](#parentfactionmod)       | FLOAT        |          | NO   |     | 0       |       |         |
| [ParentFactionCap_1](#parentfactioncap)       | INT          |          | NO   |     | 0       |       |         |
| [ParentFactionCap_2](#parentfactioncap)       | INT          |          | NO   |     | 0       |       |         |
| [Name_Lang_enUS](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)                   | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)                    | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
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

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `FactionEntry::ID`.

### ReputationIndex

The core reads this column into `FactionEntry::reputationListID`.

### ReputationRaceMask

The core reads these columns into `FactionEntry::BaseRepRaceMask`.

### ReputationClassMask

The core reads these columns into `FactionEntry::BaseRepClassMask`.

### ReputationBase

The core reads these columns into `FactionEntry::BaseRepValue`.

### ReputationFlags

The core reads these columns into `FactionEntry::ReputationFlags`.

### ParentFactionID

The core reads this column into `FactionEntry::team`.

### ParentFactionMod

The core reads these columns.

Comment in the core source: "Faction gains incoming rep * spilloverRateIn; Faction outputs rep * spilloverRateOut as spillover reputation"

### ParentFactionCap

The core reads `ParentFactionCap_1` into `FactionEntry::spilloverMaxRankIn`. `ParentFactionCap_2` is not used by the core.

Comment in the core source: "The highest rank the faction will profit from incoming spillover; It does not seem to be the max standing at which a faction outputs spillover ...so no idea"

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk` into `FactionEntry::name`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Description\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.
