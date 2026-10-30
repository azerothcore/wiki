# achievement\_criteria\_dbc

[<-Back-to:World](database-world)

**The \`achievement\_criteria\_dbc\` table**

This table has the same columns as the client file `Achievement_Criteria.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: achievement\_criteria\_dbc's Structure**

| Field                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |          | NO   | PRI | 0       |       |         |
| [Achievement_Id](#achievementid)          | INT          |          | NO   |     | 0       |       |         |
| [Type](#type)                             | INT          |          | NO   |     | 0       |       |         |
| [Asset_Id](#assetid)                      | INT          |          | NO   |     | 0       |       |         |
| [Quantity](#quantity)                     | INT          |          | NO   |     | 0       |       |         |
| [Start_Event](#startevent)                | INT          |          | NO   |     | 0       |       |         |
| [Start_Asset](#startasset)                | INT          |          | NO   |     | 0       |       |         |
| [Fail_Event](#failevent)                  | INT          |          | NO   |     | 0       |       |         |
| [Fail_Asset](#failasset)                  | INT          |          | NO   |     | 0       |       |         |
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
| [Flags](#flags)                           | INT          |          | NO   |     | 0       |       |         |
| [Timer_Start_Event](#timerstartevent)     | INT          |          | NO   |     | 0       |       |         |
| [Timer_Asset_Id](#timerassetid)           | INT          |          | NO   |     | 0       |       |         |
| [Timer_Time](#timertime)                  | INT          |          | NO   |     | 0       |       |         |
| [Ui_Order](#uiorder)                      | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `AchievementCriteriaEntry::ID`.

### Achievement\_Id

The core reads this column into `AchievementCriteriaEntry::referredAchievement`.

### Type

The core reads this column into `AchievementCriteriaEntry::requiredType`.

### Asset\_Id

The core reads this column into `AchievementCriteriaEntry::field3`.

Comment in the core source: "main requirement"

### Quantity

The core reads this column into `AchievementCriteriaEntry::count`.

Comment in the core source: "main requirement count"

### Start\_Event

The core reads this column.

### Start\_Asset

The core reads this column.

### Fail\_Event

The core reads this column.

### Fail\_Asset

The core reads this column.

### Description\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Flags

The core reads this column into `AchievementCriteriaEntry::flags`.

### Timer\_Start\_Event

The core reads this column into `AchievementCriteriaEntry::timedType`.

### Timer\_Asset\_Id

The core reads this column into `AchievementCriteriaEntry::timerStartEvent`.

Comment in the core source: "Alway appears with timed events"

### Timer\_Time

The core reads this column into `AchievementCriteriaEntry::timeLimit`.

Comment in the core source: "time limit in seconds"

### Ui\_Order

Not used by the core.

Comment in the core source: "show order"
