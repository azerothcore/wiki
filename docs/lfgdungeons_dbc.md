# lfgdungeons\_dbc

[<-Back-to:World](database-world)

**The \`lfgdungeons\_dbc\` table**

This table has the same columns as the client file `LFGDungeons.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: lfgdungeons\_dbc's Structure**

| Field                                     | Type |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT  |          | NO   | PRI | 0       |       |         |
| [Name_Lang_enUS](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelang)               | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelang)                | TEXT |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelang)               | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [MinLevel](#minlevel)                     | INT  |          | NO   |     | 0       |       |         |
| [MaxLevel](#maxlevel)                     | INT  |          | NO   |     | 0       |       |         |
| [Target_Level](#targetlevel)              | INT  |          | NO   |     | 0       |       |         |
| [Target_Level_Min](#targetlevelmin)       | INT  |          | NO   |     | 0       |       |         |
| [Target_Level_Max](#targetlevelmax)       | INT  |          | NO   |     | 0       |       |         |
| [MapID](#mapid)                           | INT  |          | NO   |     | 0       |       |         |
| [Difficulty](#difficulty)                 | INT  |          | NO   |     | 0       |       |         |
| [Flags](#flags)                           | INT  |          | NO   |     | 0       |       |         |
| [TypeID](#typeid)                         | INT  |          | NO   |     | 0       |       |         |
| [Faction](#faction)                       | INT  |          | NO   |     | 0       |       |         |
| [TextureFilename](#texturefilename)       | TEXT |          | YES  |     | NULL    |       |         |
| [ExpansionLevel](#expansionlevel)         | INT  |          | NO   |     | 0       |       |         |
| [Order_Index](#orderindex)                | INT  |          | NO   |     | 0       |       |         |
| [Group_Id](#groupid)                      | INT  |          | NO   |     | 0       |       |         |
| [Description_Lang_enUS](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_enGB](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_koKR](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_frFR](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_deDE](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_enCN](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhCN](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_enTW](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhTW](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_esES](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_esMX](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_ruRU](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptPT](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptBR](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_itIT](#descriptionlang) | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_Unk](#descriptionlang)  | TEXT |          | YES  |     | NULL    |       |         |
| [Description_Lang_Mask](#descriptionlang) | INT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `LFGDungeonEntry::ID`.

### Name\_Lang

The core reads `Name_Lang_enUS` to `Name_Lang_Unk` into `LFGDungeonEntry::Name`. `Name_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Name_Lang_enUS` = enUS, `Name_Lang_enGB` = koKR, `Name_Lang_koKR` = frFR, `Name_Lang_frFR` = deDE, `Name_Lang_deDE` = zhCN, `Name_Lang_enCN` = zhTW, `Name_Lang_zhCN` = esES, `Name_Lang_enTW` = esMX, `Name_Lang_zhTW` = ruRU. The remaining text columns, `Name_Lang_esES` to `Name_Lang_Unk`, are not supported in 3.3.5a and are not used.

### MinLevel

The core reads this column into `LFGDungeonEntry::MinLevel`.

### MaxLevel

The core reads this column into `LFGDungeonEntry::MaxLevel`.

### Target\_Level

The core reads this column into `LFGDungeonEntry::TargetLevel`.

### Target\_Level\_Min

The core reads this column into `LFGDungeonEntry::TargetLevelMin`.

### Target\_Level\_Max

The core reads this column into `LFGDungeonEntry::TargetLevelMax`.

### MapID

The core reads this column into `LFGDungeonEntry::MapID`.

### Difficulty

The core reads this column into `LFGDungeonEntry::Difficulty`.

### Flags

The core reads this column into `LFGDungeonEntry::Flags`.

### TypeID

The core reads this column into `LFGDungeonEntry::TypeID`.

### Faction

Not used by the core.

### TextureFilename

Not used by the core.

### ExpansionLevel

The core reads this column into `LFGDungeonEntry::ExpansionLevel`.

### Order\_Index

Not used by the core.

### Group\_Id

The core reads this column into `LFGDungeonEntry::GroupID`.

### Description\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.
