# skillraceclassinfo\_dbc

[<-Back-to:World](database-world)

**The \`skillraceclassinfo\_dbc\` table**

This table has the same columns as the client file `SkillRaceClassInfo.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: skillraceclassinfo\_dbc's Structure**

| Field                             | Type |     | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                         | INT  |     | NO   | PRI | 0       |       |         |
| [SkillID](#skillid)               | INT  |     | NO   |     | 0       |       |         |
| [RaceMask](#racemask)             | INT  |     | NO   |     | 0       |       |         |
| [ClassMask](#classmask)           | INT  |     | NO   |     | 0       |       |         |
| [Flags](#flags)                   | INT  |     | NO   |     | 0       |       |         |
| [MinLevel](#minlevel)             | INT  |     | NO   |     | 0       |       |         |
| [SkillTierID](#skilltierid)       | INT  |     | NO   |     | 0       |       |         |
| [SkillCostIndex](#skillcostindex) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### SkillID

The core reads this column into `SkillRaceClassInfoEntry::SkillID`.

### RaceMask

The core reads this column into `SkillRaceClassInfoEntry::RaceMask`.

### ClassMask

The core reads this column into `SkillRaceClassInfoEntry::ClassMask`.

### Flags

The core reads this column into `SkillRaceClassInfoEntry::Flags`.

### MinLevel

Not used by the core.

### SkillTierID

The core reads this column into `SkillRaceClassInfoEntry::SkillTierID`.

### SkillCostIndex

Not used by the core.
