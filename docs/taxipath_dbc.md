# taxipath\_dbc

[<-Back-to:World](database-world)

**The \`taxipath\_dbc\` table**

This table has the same columns as the client file `TaxiPath.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: taxipath\_dbc's Structure**

| Field                         | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                     | INT  |     | NO   | PRI | 0       |       |         |
| [FromTaxiNode](#fromtaxinode) | INT  |     | NO   |     | 0       |       |         |
| [ToTaxiNode](#totaxinode)     | INT  |     | NO   |     | 0       |       |         |
| [Cost](#cost)                 | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `TaxiPathEntry::ID`.

### FromTaxiNode

The core reads this column into `TaxiPathEntry::from`.

### ToTaxiNode

The core reads this column into `TaxiPathEntry::to`.

### Cost

The core reads this column into `TaxiPathEntry::price`.
