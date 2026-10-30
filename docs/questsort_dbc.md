# questsort\_dbc

[<-Back-to:World](database-world)

**The \`questsort\_dbc\` table**

This table has the same columns as the client file `QuestSort.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: questsort\_dbc's Structure**

| Field                               | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                           | INT          |          | NO   | PRI | 0       |       |         |
| [SortName_Lang_enUS](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_enGB](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_koKR](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_frFR](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_deDE](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_enCN](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_zhCN](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_enTW](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_zhTW](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_esES](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_esMX](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_ruRU](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_ptPT](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_ptBR](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_itIT](#sortnamelang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_Unk](#sortnamelang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [SortName_Lang_Mask](#sortnamelang) | INT          | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `QuestSortEntry::id`.

### SortName\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `SortName_Lang_enUS` = enUS, `SortName_Lang_enGB` = koKR, `SortName_Lang_koKR` = frFR, `SortName_Lang_frFR` = deDE, `SortName_Lang_deDE` = zhCN, `SortName_Lang_enCN` = zhTW, `SortName_Lang_zhCN` = esES, `SortName_Lang_enTW` = esMX, `SortName_Lang_zhTW` = ruRU. The remaining text columns, `SortName_Lang_esES` to `SortName_Lang_Unk`, are not supported in 3.3.5a and are not used.
