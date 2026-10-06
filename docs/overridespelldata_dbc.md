# overridespelldata\_dbc

[<-Back-to:World](database-world)

**The \`overridespelldata\_dbc\` table**

This table has the same columns as the client file `OverrideSpellData.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: overridespelldata\_dbc's Structure**

| Field                | Type |     | Null | Key | Default | Extra | Comment |
| :------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)            | INT  |     | NO   | PRI | 0       |       |         |
| [Spells_1](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_2](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_3](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_4](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_5](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_6](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_7](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_8](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_9](#spells)  | INT  |     | NO   |     | 0       |       |         |
| [Spells_10](#spells) | INT  |     | NO   |     | 0       |       |         |
| [Flags](#flags)      | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `OverrideSpellDataEntry::id`.

### Spells

The core reads these columns into `OverrideSpellDataEntry::spellId`.

### Flags

Not used by the core.
