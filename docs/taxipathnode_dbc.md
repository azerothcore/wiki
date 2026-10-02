# taxipathnode\_dbc

[<-Back-to:World](database-world)

**The \`taxipathnode\_dbc\` table**

This table has the same columns as the client file `TaxiPathNode.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: taxipathnode\_dbc's Structure**

| Field                                 | Type  | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                             | INT   | SIGNED     | PRI | NO   | 0       |       |         |
| [PathID](#pathid)                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [NodeIndex](#nodeindex)               | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ContinentID](#continentid)           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [LocX](#locx)                         | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [LocY](#locy)                         | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [LocZ](#locz)                         | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [Flags](#flags)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [Delay](#delay)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ArrivalEventID](#arrivaleventid)     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [DepartureEventID](#departureeventid) | INT   | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### PathID

The core reads this column into `TaxiPathNodeEntry::path`.

### NodeIndex

The core reads this column into `TaxiPathNodeEntry::index`.

### ContinentID

The core reads this column into `TaxiPathNodeEntry::mapid`.

### LocX

The core reads this column into `TaxiPathNodeEntry::x`.

### LocY

The core reads this column into `TaxiPathNodeEntry::y`.

### LocZ

The core reads this column into `TaxiPathNodeEntry::z`.

### Flags

The core reads this column into `TaxiPathNodeEntry::actionFlag`.

### Delay

The core reads this column into `TaxiPathNodeEntry::delay`.

### ArrivalEventID

The core reads this column into `TaxiPathNodeEntry::arrivalEventID`.

### DepartureEventID

The core reads this column into `TaxiPathNodeEntry::departureEventID`.
