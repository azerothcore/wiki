# light\_dbc

[<-Back-to:World](database-world)

**The \`light\_dbc\` table**

This table has the same columns as the client file `Light.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: light\_dbc's Structure**

| Field                             | Type  |     | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :---- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                         | INT   |     | NO   | PRI | 0       |       |         |
| [ContinentID](#continentid)       | INT   |     | NO   |     | 0       |       |         |
| [X](#x)                           | FLOAT |     | NO   |     | 0       |       |         |
| [Y](#y)                           | FLOAT |     | NO   |     | 0       |       |         |
| [Z](#z)                           | FLOAT |     | NO   |     | 0       |       |         |
| [FalloffStart](#falloffstart)     | FLOAT |     | NO   |     | 0       |       |         |
| [FalloffEnd](#falloffend)         | FLOAT |     | NO   |     | 0       |       |         |
| [LightParamsID_1](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_2](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_3](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_4](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_5](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_6](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_7](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |
| [LightParamsID_8](#lightparamsid) | INT   |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### ContinentID

The core reads this column.

### X

The core reads this column.

### Y

The core reads this column.

### Z

The core reads this column.

### FalloffStart

Not used by the core.

### FalloffEnd

Not used by the core.

### LightParamsID

Not used by the core.
