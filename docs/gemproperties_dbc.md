# gemproperties\_dbc

[<-Back-to:World](database-world)

**The \`gemproperties\_dbc\` table**

This table has the same columns as the client file `GemProperties.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: gemproperties\_dbc's Structure**

| Field                          | Type |     | Null | Key | Default | Extra | Comment |
| :----------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                      | INT  |     | NO   | PRI | 0       |       |         |
| [Enchant_Id](#enchantid)       | INT  |     | NO   |     | 0       |       |         |
| [Maxcount_Inv](#maxcountinv)   | INT  |     | NO   |     | 0       |       |         |
| [Maxcount_Item](#maxcountitem) | INT  |     | NO   |     | 0       |       |         |
| [Type](#type)                  | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Enchant\_Id

The core reads this column.

### Maxcount\_Inv

Not used by the core.

### Maxcount\_Item

Not used by the core.

### Type

The core reads this column.
