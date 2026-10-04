# emotes\_dbc

[<-Back-to:World](database-world)

**The \`emotes\_dbc\` table**

This table has the same columns as the client file `Emotes.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: emotes\_dbc's Structure**

| Field                                     | Type         |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |     | NO   | PRI | 0       |       |         |
| [EmoteSlashCommand](#emoteslashcommand)   | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [AnimID](#animid)                         | INT          |     | NO   |     | 0       |       |         |
| [EmoteFlags](#emoteflags)                 | INT          |     | NO   |     | 0       |       |         |
| [EmoteSpecProc](#emotespecproc)           | INT          |     | NO   |     | 0       |       |         |
| [EmoteSpecProcParam](#emotespecprocparam) | INT          |     | NO   |     | 0       |       |         |
| [EventSoundID](#eventsoundid)             | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `EmotesEntry::Id`.

### EmoteSlashCommand

Not used by the core.

Comment in the core source: "internal name"

### AnimID

Not used by the core.

Comment in the core source: "ref to animationData"

### EmoteFlags

The core reads this column into `EmotesEntry::Flags`.

Comment in the core source: "bitmask, may be unit_flags"

### EmoteSpecProc

The core reads this column into `EmotesEntry::EmoteType`.

Comment in the core source: "Can be 0, 1 or 2 (determine how emote are shown)"

### EmoteSpecProcParam

The core reads this column into `EmotesEntry::UnitStandState`.

Comment in the core source: "uncomfirmed, may be enum UnitStandStateType"

### EventSoundID

Not used by the core.

Comment in the core source: "ref to soundEntries"
