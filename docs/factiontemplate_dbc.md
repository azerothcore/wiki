# factiontemplate\_dbc

[<-Back-to:World](database-world)

**The \`factiontemplate\_dbc\` table**

This table has the same columns as the client file `FactionTemplate.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: factiontemplate\_dbc's Structure**

| Field                         | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                     | INT  |     | NO   | PRI | 0       |       |         |
| [Faction](#faction)           | INT  |     | NO   |     | 0       |       |         |
| [Flags](#flags)               | INT  |     | NO   |     | 0       |       |         |
| [FactionGroup](#factiongroup) | INT  |     | NO   |     | 0       |       |         |
| [FriendGroup](#friendgroup)   | INT  |     | NO   |     | 0       |       |         |
| [EnemyGroup](#enemygroup)     | INT  |     | NO   |     | 0       |       |         |
| [Enemies_1](#enemies)         | INT  |     | NO   |     | 0       |       |         |
| [Enemies_2](#enemies)         | INT  |     | NO   |     | 0       |       |         |
| [Enemies_3](#enemies)         | INT  |     | NO   |     | 0       |       |         |
| [Enemies_4](#enemies)         | INT  |     | NO   |     | 0       |       |         |
| [Friend_1](#friend)           | INT  |     | NO   |     | 0       |       |         |
| [Friend_2](#friend)           | INT  |     | NO   |     | 0       |       |         |
| [Friend_3](#friend)           | INT  |     | NO   |     | 0       |       |         |
| [Friend_4](#friend)           | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `FactionTemplateEntry::ID`.

### Faction

The core reads this column into `FactionTemplateEntry::faction`.

### Flags

The core reads this column into `FactionTemplateEntry::factionFlags`.

### FactionGroup

The core reads this column into `FactionTemplateEntry::ourMask`.

### FriendGroup

The core reads this column into `FactionTemplateEntry::friendlyMask`.

### EnemyGroup

The core reads this column into `FactionTemplateEntry::hostileMask`.

### Enemies

The core reads these columns.

### Friend

The core reads these columns.
