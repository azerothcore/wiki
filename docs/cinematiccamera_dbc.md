# cinematiccamera\_dbc

[<-Back-to:World](database-world)

**The \`cinematiccamera\_dbc\` table**

This table has the same columns as the client file `CinematicCamera.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: cinematiccamera\_dbc's Structure**

| Field                     | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT          |     | NO   | PRI | 0       |       |         |
| [model](#model)           | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [soundEntry](#soundentry) | INT          |     | NO   |     | 0       |       |         |
| [locationX](#locationx)   | FLOAT        |     | NO   |     | 0       |       |         |
| [locationY](#locationy)   | FLOAT        |     | NO   |     | 0       |       |         |
| [locationZ](#locationz)   | FLOAT        |     | NO   |     | 0       |       |         |
| [rotation](#rotation)     | FLOAT        |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `CinematicCameraEntry::ID`.

### model

The core reads this column into `CinematicCameraEntry::Model`.

Comment in the core source: "Model filename (translate .mdx to .m2)"

### soundEntry

The core reads this column into `CinematicCameraEntry::SoundID`.

Comment in the core source: "Sound ID       (voiceover for cinematic)"

### locationX

The core reads this column into `CinematicCameraEntry::Origin`.

Comment in the core source: "Position in map used for basis for M2 co-ordinates"

### locationY

The core reads this column into `CinematicCameraEntry::Origin`.

Comment in the core source: "Position in map used for basis for M2 co-ordinates"

### locationZ

The core reads this column into `CinematicCameraEntry::Origin`.

Comment in the core source: "Position in map used for basis for M2 co-ordinates"

### rotation

The core reads this column into `CinematicCameraEntry::OriginFacing`.

Comment in the core source: "Orientation in map used for basis for M2 co-ordinates"
