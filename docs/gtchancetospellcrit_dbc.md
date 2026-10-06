# gtchancetospellcrit\_dbc

[<-Back-to:World](database-world)

**The \`gtchancetospellcrit\_dbc\` table**

This table holds the data of the client file `gtChanceToSpellCrit.dbc`, with an `ID` column for the position of the row and one data column. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: gtchancetospellcrit\_dbc's Structure**

| Field         | Type  |     | Null | Key | Default | Extra | Comment |
| :------------ | :---- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)     | INT   |     | NO   | PRI | 0       |       |         |
| [Data](#data) | FLOAT |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### Data

The core reads this column.
