# areagroup\_dbc

[<-Back-to:World](database-world)

**The \`areagroup\_dbc\` table**

This table has the same columns as the client file `AreaGroup.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: areagroup\_dbc's Structure**

| Field                     | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT  |     | NO   | PRI | 0       |       |         |
| [AreaID_1](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [AreaID_2](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [AreaID_3](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [AreaID_4](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [AreaID_5](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [AreaID_6](#areaid)       | INT  |     | NO   |     | 0       |       |         |
| [NextAreaID](#nextareaid) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `AreaGroupEntry::AreaGroupId`.

### AreaID

The core reads these columns into `AreaGroupEntry::AreaId`.

### NextAreaID

The core reads this column into `AreaGroupEntry::nextGroup`.

Comment in the core source: "index of next group"
