# cinematicsequences\_dbc

[<-Back-to:World](database-world)

**The \`cinematicsequences\_dbc\` table**

This table has the same columns as the client file `CinematicSequences.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: cinematicsequences\_dbc's Structure**

| Field               | Type |     | Null | Key | Default | Extra | Comment |
| :------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)           | INT  |     | NO   | PRI | 0       |       |         |
| [SoundID](#soundid) | INT  |     | NO   |     | 0       |       |         |
| [Camera_1](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_2](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_3](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_4](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_5](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_6](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_7](#camera) | INT  |     | NO   |     | 0       |       |         |
| [Camera_8](#camera) | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `CinematicSequencesEntry::Id`.

### SoundID

Not used by the core.

### Camera

The core reads `Camera_1` into `CinematicSequencesEntry::cinematicCamera`. `Camera_2` to `Camera_8` are not used by the core.

Comment in the core source: "id in CinematicCamera.dbc"
