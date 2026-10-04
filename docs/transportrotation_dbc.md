# transportrotation\_dbc

[<-Back-to:World](database-world)

**The \`transportrotation\_dbc\` table**

This table has the same columns as the client file `TransportRotation.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: transportrotation\_dbc's Structure**

| Field                           | Type  |     | Null | Key | Default | Extra | Comment |
| :------------------------------ | :---- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT   |     | NO   | PRI | 0       |       |         |
| [GameObjectsID](#gameobjectsid) | INT   |     | NO   |     | 0       |       |         |
| [TimeIndex](#timeindex)         | INT   |     | NO   |     | 0       |       |         |
| [RotX](#rotx)                   | FLOAT |     | NO   |     | 0       |       |         |
| [RotY](#roty)                   | FLOAT |     | NO   |     | 0       |       |         |
| [RotZ](#rotz)                   | FLOAT |     | NO   |     | 0       |       |         |
| [RotW](#rotw)                   | FLOAT |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### GameObjectsID

The core reads this column.

### TimeIndex

The core reads this column.

### RotX

The core reads this column.

### RotY

The core reads this column.

### RotZ

The core reads this column.

### RotW

The core reads this column.
