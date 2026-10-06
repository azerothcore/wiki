# spellrunecost\_dbc

[<-Back-to:World](database-world)

**The \`spellrunecost\_dbc\` table**

This table has the same columns as the client file `SpellRuneCost.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellrunecost\_dbc's Structure**

| Field                     | Type |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT  |     | NO   | PRI | 0       |       |         |
| [Blood](#blood)           | INT  |     | NO   |     | 0       |       |         |
| [Unholy](#unholy)         | INT  |     | NO   |     | 0       |       |         |
| [Frost](#frost)           | INT  |     | NO   |     | 0       |       |         |
| [RunicPower](#runicpower) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellRuneCostEntry::ID`.

### Blood

The core reads this column into `SpellRuneCostEntry::RuneCost`.

Comment in the core source: "(0=blood, 1=frost, 2=unholy)"

### Unholy

The core reads this column into `SpellRuneCostEntry::RuneCost`.

Comment in the core source: "(0=blood, 1=frost, 2=unholy)"

### Frost

The core reads this column into `SpellRuneCostEntry::RuneCost`.

Comment in the core source: "(0=blood, 1=frost, 2=unholy)"

### RunicPower

The core reads this column into `SpellRuneCostEntry::runePowerGain`.
