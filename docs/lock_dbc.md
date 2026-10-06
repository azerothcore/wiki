# lock\_dbc

[<-Back-to:World](database-world)

**The \`lock\_dbc\` table**

This table has the same columns as the client file `Lock.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: lock\_dbc's Structure**

| Field               | Type |     | Null | Key | Default | Extra | Comment |
| :------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)           | INT  |     | NO   | PRI | 0       |       |         |
| [Type_1](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_2](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_3](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_4](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_5](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_6](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_7](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Type_8](#type)     | INT  |     | NO   |     | 0       |       |         |
| [Index_1](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_2](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_3](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_4](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_5](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_6](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_7](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Index_8](#index)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_1](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_2](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_3](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_4](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_5](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_6](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_7](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Skill_8](#skill)   | INT  |     | NO   |     | 0       |       |         |
| [Action_1](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_2](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_3](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_4](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_5](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_6](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_7](#action) | INT  |     | NO   |     | 0       |       |         |
| [Action_8](#action) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `LockEntry::ID`.

### Type

The core reads these columns into `LockEntry::Type`.

### Index

The core reads these columns into `LockEntry::Index`.

### Skill

The core reads these columns into `LockEntry::Skill`.

### Action

Not used by the core.
