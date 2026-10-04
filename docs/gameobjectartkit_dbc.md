# gameobjectartkit\_dbc

[<-Back-to:World](database-world)

**The \`gameobjectartkit\_dbc\` table**

This table has the same columns as the client file `GameObjectArtKit.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: gameobjectartkit\_dbc's Structure**

| Field                          | Type |     | Null | Key | Default | Extra | Comment |
| :----------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                      | INT  |     | NO   | PRI | 0       |       |         |
| [Texture_1](#texture)          | INT  |     | NO   |     | 0       |       |         |
| [Texture_2](#texture)          | INT  |     | NO   |     | 0       |       |         |
| [Texture_3](#texture)          | INT  |     | NO   |     | 0       |       |         |
| [Attach_Model_1](#attachmodel) | INT  |     | NO   |     | 0       |       |         |
| [Attach_Model_2](#attachmodel) | INT  |     | NO   |     | 0       |       |         |
| [Attach_Model_3](#attachmodel) | INT  |     | NO   |     | 0       |       |         |
| [Attach_Model_4](#attachmodel) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `GameObjectArtKitEntry::ID`.

### Texture

Not used by the core.

### Attach\_Model

Not used by the core.
