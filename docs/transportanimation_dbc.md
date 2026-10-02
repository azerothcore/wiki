# transportanimation\_dbc

[<-Back-to:World](database-world)

**The \`transportanimation\_dbc\` table**

This table has the same columns as the client file `TransportAnimation.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: transportanimation\_dbc's Structure**

| Field                       | Type  | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                   | INT   | SIGNED     | PRI | NO   | 0       |       |         |
| [TransportID](#transportid) | INT   | SIGNED     |     | NO   | 0       |       |         |
| [TimeIndex](#timeindex)     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [PosX](#posx)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [PosY](#posy)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [PosZ](#posz)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [SequenceID](#sequenceid)   | INT   | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### TransportID

The core reads this column.

### TimeIndex

The core reads this column.

### PosX

The core reads this column.

### PosY

The core reads this column.

### PosZ

The core reads this column.

### SequenceID

Not used by the core.
