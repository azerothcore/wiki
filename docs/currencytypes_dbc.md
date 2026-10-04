# currencytypes\_dbc

[<-Back-to:World](database-world)

**The \`currencytypes\_dbc\` table**

This table has the same columns as the client file `CurrencyTypes.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: currencytypes\_dbc's Structure**

| Field                     | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT  |     | NO   | PRI | 0       |       |         |
| [ItemID](#itemid)         | INT  |     | NO   |     | 0       |       |         |
| [CategoryID](#categoryid) | INT  |     | NO   |     | 0       |       |         |
| [BitIndex](#bitindex)     | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

Not used by the core.

### ItemID

The row ID. The core uses it as the index of the rows and stores it in `CurrencyTypesEntry::ItemId`.

Comment in the core source: "used as real index"

### CategoryID

Not used by the core.

Comment in the core source: "may be category"

### BitIndex

The core reads this column into `CurrencyTypesEntry::BitIndex`.

Comment in the core source: "bit index in PLAYER_FIELD_KNOWN_CURRENCIES (1 << (index-1))"
