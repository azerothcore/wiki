# pvpdifficulty\_dbc

[<-Back-to:World](database-world)

**The \`pvpdifficulty\_dbc\` table**

This table has the same columns as the client file `PvpDifficulty.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: pvpdifficulty\_dbc's Structure**

| Field                     | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT  |     | NO   | PRI | 0       |       |         |
| [MapID](#mapid)           | INT  |     | NO   |     | 0       |       |         |
| [RangeIndex](#rangeindex) | INT  |     | NO   |     | 0       |       |         |
| [MinLevel](#minlevel)     | INT  |     | NO   |     | 0       |       |         |
| [MaxLevel](#maxlevel)     | INT  |     | NO   |     | 0       |       |         |
| [Difficulty](#difficulty) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### MapID

The core reads this column into `PvPDifficultyEntry::mapId`.

### RangeIndex

The core reads this column into `PvPDifficultyEntry::bracketId`.

### MinLevel

The core reads this column into `PvPDifficultyEntry::minLevel`.

### MaxLevel

The core reads this column into `PvPDifficultyEntry::maxLevel`.

### Difficulty

The core reads this column into `PvPDifficultyEntry::difficulty`.
