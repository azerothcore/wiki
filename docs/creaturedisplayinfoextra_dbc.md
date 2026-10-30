# creaturedisplayinfoextra\_dbc

[<-Back-to:World](database-world)

**The \`creaturedisplayinfoextra\_dbc\` table**

This table has the same columns as the client file `CreatureDisplayInfoExtra.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: creaturedisplayinfoextra\_dbc's Structure**

| Field                               | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                           | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [DisplayRaceID](#displayraceid)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [DisplaySexID](#displaysexid)       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [SkinID](#skinid)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [FaceID](#faceid)                   | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [HairStyleID](#hairstyleid)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [HairColorID](#haircolorid)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [FacialHairID](#facialhairid)       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay1](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay2](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay3](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay4](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay5](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay6](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay7](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay8](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay9](#npcitemdisplay)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay10](#npcitemdisplay) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [NPCItemDisplay11](#npcitemdisplay) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Flags](#flags)                     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [BakeName](#bakename)               | VARCHAR(100) |          | NO   |     |         |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### DisplayRaceID

The core reads this column into `CreatureDisplayInfoExtraEntry::DisplayRaceID`.

### DisplaySexID

Not used by the core.

### SkinID

Not used by the core.

### FaceID

Not used by the core.

### HairStyleID

Not used by the core.

### HairColorID

Not used by the core.

### FacialHairID

Not used by the core.

### NPCItemDisplay

Not used by the core.

### Flags

Not used by the core.

### BakeName

Not used by the core.
