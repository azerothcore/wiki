# scalingstatdistribution\_dbc

[<-Back-to:World](database-world)

**The \`scalingstatdistribution\_dbc\` table**

This table has the same columns as the client file `ScalingStatDistribution.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: scalingstatdistribution\_dbc's Structure**

| Field                 | Type |     | Null | Key | Default | Extra | Comment |
| :-------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)             | INT  |     | NO   | PRI | 0       |       |         |
| [StatID_1](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_2](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_3](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_4](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_5](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_6](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_7](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_8](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_9](#statid)   | INT  |     | NO   |     | 0       |       |         |
| [StatID_10](#statid)  | INT  |     | NO   |     | 0       |       |         |
| [Bonus_1](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_2](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_3](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_4](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_5](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_6](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_7](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_8](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_9](#bonus)     | INT  |     | NO   |     | 0       |       |         |
| [Bonus_10](#bonus)    | INT  |     | NO   |     | 0       |       |         |
| [Maxlevel](#maxlevel) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `ScalingStatDistributionEntry::Id`.

### StatID

The core reads these columns into `ScalingStatDistributionEntry::StatMod`.

### Bonus

The core reads these columns into `ScalingStatDistributionEntry::Modifier`.

### Maxlevel

The core reads this column into `ScalingStatDistributionEntry::MaxLevel`.
