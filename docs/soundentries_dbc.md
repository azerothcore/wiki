# soundentries\_dbc

[<-Back-to:World](database-world)

**The \`soundentries\_dbc\` table**

This table has the same columns as the client file `SoundEntries.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: soundentries\_dbc's Structure**

| Field                                             | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------------------------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                         | INT          |     | NO   | PRI | 0       |       |         |
| [SoundType](#soundtype)                           | INT          |     | NO   |     | 0       |       |         |
| [Name](#name)                                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_1](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_2](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_3](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_4](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_5](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_6](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_7](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_8](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_9](#file)                                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [File_10](#file)                                  | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Freq_1](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_2](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_3](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_4](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_5](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_6](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_7](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_8](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_9](#freq)                                   | INT          |     | NO   |     | 0       |       |         |
| [Freq_10](#freq)                                  | INT          |     | NO   |     | 0       |       |         |
| [DirectoryBase](#directorybase)                   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Volumefloat](#volumefloat)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [Flags](#flags)                                   | INT          |     | NO   |     | 0       |       |         |
| [MinDistance](#mindistance)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [DistanceCutoff](#distancecutoff)                 | FLOAT        |     | NO   |     | 0       |       |         |
| [EAXDef](#eaxdef)                                 | INT          |     | NO   |     | 0       |       |         |
| [SoundEntriesAdvancedID](#soundentriesadvancedid) | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SoundEntriesEntry::Id`.

### SoundType

Not used by the core.

### Name

Not used by the core.

### File

Not used by the core.

### Freq

Not used by the core.

### DirectoryBase

Not used by the core.

### Volumefloat

Not used by the core.

### Flags

Not used by the core.

### MinDistance

Not used by the core.

### DistanceCutoff

Not used by the core.

### EAXDef

Not used by the core.

### SoundEntriesAdvancedID

Not used by the core.
