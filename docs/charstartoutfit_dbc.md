# charstartoutfit\_dbc

[<-Back-to:World](database-world)

**The \`charstartoutfit\_dbc\` table**

This table has the same columns as the client file `CharStartOutfit.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: charstartoutfit\_dbc's Structure**

| Field                              | Type    |          | Null | Key | Default | Extra | Comment |
| :--------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                          | INT     |          | NO   | PRI | 0       |       |         |
| [RaceID](#raceid)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [ClassID](#classid)                | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [SexID](#sexid)                    | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [OutfitID](#outfitid)              | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [ItemID_1](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_2](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_3](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_4](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_5](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_6](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_7](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_8](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_9](#itemid)                | INT     |          | NO   |     | 0       |       |         |
| [ItemID_10](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_11](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_12](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_13](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_14](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_15](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_16](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_17](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_18](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_19](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_20](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_21](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_22](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_23](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [ItemID_24](#itemid)               | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_1](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_2](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_3](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_4](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_5](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_6](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_7](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_8](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_9](#displayitemid)  | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_10](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_11](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_12](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_13](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_14](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_15](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_16](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_17](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_18](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_19](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_20](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_21](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_22](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_23](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [DisplayItemID_24](#displayitemid) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_1](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_2](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_3](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_4](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_5](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_6](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_7](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_8](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_9](#inventorytype)  | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_10](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_11](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_12](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_13](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_14](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_15](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_16](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_17](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_18](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_19](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_20](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_21](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_22](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_23](#inventorytype) | INT     |          | NO   |     | 0       |       |         |
| [InventoryType_24](#inventorytype) | INT     |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### RaceID

The core reads this column into `CharStartOutfitEntry::Race`.

### ClassID

The core reads this column into `CharStartOutfitEntry::Class`.

### SexID

The core reads this column into `CharStartOutfitEntry::Gender`.

### OutfitID

Not used by the core.

### ItemID

The core reads these columns into `CharStartOutfitEntry::ItemId`.

### DisplayItemID

Not used by the core.

Comment in the core source: "not required at server side"

### InventoryType

Not used by the core.

Comment in the core source: "not required at server side"
