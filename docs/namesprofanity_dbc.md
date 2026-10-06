# namesprofanity\_dbc

[<-Back-to:World](database-world)

**The \`namesprofanity\_dbc\` table**

This table has the same columns as the client file `NamesProfanity.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: namesprofanity\_dbc's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                   | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [Pattern](#pattern)         | TINYTEXT |          | NO   |     |         |       |         |
| [LanguagueID](#languagueid) | TINYINT  |          | NO   |     |         |       |         |

**Description of the table's fields**

### ID

Not used by the core.

### Pattern

The core reads this column into `NamesProfanityEntry::Pattern`.

### LanguagueID

Not used by the core.
