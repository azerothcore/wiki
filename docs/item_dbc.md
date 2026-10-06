# item\_dbc

[<-Back-to:World](database-world)

**The \`item\_dbc\` table**

This table has the same columns as the client file `Item.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: item\_dbc's Structure**

| Field                                                 | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                             | INT  |     | NO   | PRI | 0       |       |         |
| [ClassID](#classid)                                   | INT  |     | NO   |     | 0       |       |         |
| [SubclassID](#subclassid)                             | INT  |     | NO   |     | 0       |       |         |
| [Sound_Override_Subclassid](#soundoverridesubclassid) | INT  |     | NO   |     | 0       |       |         |
| [Material](#material)                                 | INT  |     | NO   |     | 0       |       |         |
| [DisplayInfoID](#displayinfoid)                       | INT  |     | NO   |     | 0       |       |         |
| [InventoryType](#inventorytype)                       | INT  |     | NO   |     | 0       |       |         |
| [SheatheType](#sheathetype)                           | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `ItemEntry::ID`.

### ClassID

The core reads this column into `ItemEntry::ClassID`.

### SubclassID

The core reads this column into `ItemEntry::SubclassID`.

### Sound\_Override\_Subclassid

The core reads this column into `ItemEntry::SoundOverrideSubclassID`.

### Material

The core reads this column into `ItemEntry::Material`.

### DisplayInfoID

The core reads this column into `ItemEntry::DisplayInfoID`.

### InventoryType

The core reads this column into `ItemEntry::InventoryType`.

### SheatheType

The core reads this column into `ItemEntry::SheatheType`.
