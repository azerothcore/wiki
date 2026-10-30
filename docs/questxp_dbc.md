# questxp\_dbc

[<-Back-to:World](database-world)

**The \`questxp\_dbc\` table**

This table has the same columns as the client file `QuestXP.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: questxp\_dbc's Structure**

| Field                        | Type |     | Null | Key | Default | Extra | Comment |
| :--------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                    | INT  |     | NO   | PRI | 0       |       |         |
| [Difficulty_1](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_2](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_3](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_4](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_5](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_6](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_7](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_8](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_9](#difficulty)  | INT  |     | NO   |     | 0       |       |         |
| [Difficulty_10](#difficulty) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Difficulty

The core reads these columns.
