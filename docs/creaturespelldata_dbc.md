# creaturespelldata\_dbc

[<-Back-to:World](database-world)

**The \`creaturespelldata\_dbc\` table**

This table has the same columns as the client file `CreatureSpellData.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: creaturespelldata\_dbc's Structure**

| Field                           | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT  |     | NO   | PRI | 0       |       |         |
| [Spells_1](#spells)             | INT  |     | NO   |     | 0       |       |         |
| [Spells_2](#spells)             | INT  |     | NO   |     | 0       |       |         |
| [Spells_3](#spells)             | INT  |     | NO   |     | 0       |       |         |
| [Spells_4](#spells)             | INT  |     | NO   |     | 0       |       |         |
| [Availability_1](#availability) | INT  |     | NO   |     | 0       |       |         |
| [Availability_2](#availability) | INT  |     | NO   |     | 0       |       |         |
| [Availability_3](#availability) | INT  |     | NO   |     | 0       |       |         |
| [Availability_4](#availability) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Spells

The core reads these columns.

### Availability

Not used by the core.
