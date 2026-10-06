# skilltiers\_dbc

[<-Back-to:World](database-world)

**The \`skilltiers\_dbc\` table**

This table has the same columns as the client file `SkillTiers.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: skilltiers\_dbc's Structure**

| Field              | Type |     | Null | Key | Default | Extra | Comment |
| :----------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)          | INT  |     | NO   | PRI | 0       |       |         |
| [Cost_1](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_2](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_3](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_4](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_5](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_6](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_7](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_8](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_9](#cost)    | INT  |     | NO   |     | 0       |       |         |
| [Cost_10](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_11](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_12](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_13](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_14](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_15](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Cost_16](#cost)   | INT  |     | NO   |     | 0       |       |         |
| [Value_1](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_2](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_3](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_4](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_5](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_6](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_7](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_8](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_9](#value)  | INT  |     | NO   |     | 0       |       |         |
| [Value_10](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_11](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_12](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_13](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_14](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_15](#value) | INT  |     | NO   |     | 0       |       |         |
| [Value_16](#value) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SkillTiersEntry::ID`.

### Cost

Not used by the core.

### Value

The core reads these columns into `SkillTiersEntry::Value`.
