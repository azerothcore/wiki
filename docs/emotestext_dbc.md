# emotestext\_dbc

[<-Back-to:World](database-world)

**The \`emotestext\_dbc\` table**

This table has the same columns as the client file `EmotesText.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: emotestext\_dbc's Structure**

| Field                      | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                  | INT          | SIGNED     | PRI | NO   | 0       |       |         |
| [Name](#name)              | VARCHAR(100) |            |     | YES  | NULL    |       |         |
| [EmoteID](#emoteid)        | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_1](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_2](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_3](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_4](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_5](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_6](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_7](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_8](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_9](#emotetext)  | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_10](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_11](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_12](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_13](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_14](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_15](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |
| [EmoteText_16](#emotetext) | INT          | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Name

Not used by the core.

### EmoteID

The core reads this column.

### EmoteText

Not used by the core.
