# spellcasttimes\_dbc

[<-Back-to:World](database-world)

**The \`spellcasttimes\_dbc\` table**

This table has the same columns as the client file `SpellCastTimes.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellcasttimes\_dbc's Structure**

| Field                 | Type |     | Null | Key | Default | Extra | Comment |
| :-------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)             | INT  |     | NO   | PRI | 0       |       |         |
| [Base](#base)         | INT  |     | NO   |     | 0       |       |         |
| [PerLevel](#perlevel) | INT  |     | NO   |     | 0       |       |         |
| [Minimum](#minimum)   | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellCastTimesEntry::ID`.

### Base

The core reads this column into `SpellCastTimesEntry::CastTime`.

### PerLevel

Not used by the core.

Comment in the core source: "unsure / per skill?"

### Minimum

Not used by the core.
