# randproppoints\_dbc

[<-Back-to:World](database-world)

**The \`randproppoints\_dbc\` table**

This table has the same columns as the client file `RandPropPoints.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: randproppoints\_dbc's Structure**

| Field                   | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)               | INT  |     | NO   | PRI | 0       |       |         |
| [Epic_1](#epic)         | INT  |     | NO   |     | 0       |       |         |
| [Epic_2](#epic)         | INT  |     | NO   |     | 0       |       |         |
| [Epic_3](#epic)         | INT  |     | NO   |     | 0       |       |         |
| [Epic_4](#epic)         | INT  |     | NO   |     | 0       |       |         |
| [Epic_5](#epic)         | INT  |     | NO   |     | 0       |       |         |
| [Superior_1](#superior) | INT  |     | NO   |     | 0       |       |         |
| [Superior_2](#superior) | INT  |     | NO   |     | 0       |       |         |
| [Superior_3](#superior) | INT  |     | NO   |     | 0       |       |         |
| [Superior_4](#superior) | INT  |     | NO   |     | 0       |       |         |
| [Superior_5](#superior) | INT  |     | NO   |     | 0       |       |         |
| [Good_1](#good)         | INT  |     | NO   |     | 0       |       |         |
| [Good_2](#good)         | INT  |     | NO   |     | 0       |       |         |
| [Good_3](#good)         | INT  |     | NO   |     | 0       |       |         |
| [Good_4](#good)         | INT  |     | NO   |     | 0       |       |         |
| [Good_5](#good)         | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Epic

The core reads these columns.

### Superior

The core reads these columns.

### Good

The core reads these columns.
