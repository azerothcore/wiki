# character\_settings

[<-Back-to:Characters](database-characters)

**The \`character\_settings\` table**

Stores arbitrary per-character settings as keyed data blobs. Modules and subsystems use this table to persist their own character-scoped configuration. `guid` references `characters.guid`.

**Table: character\_settings's Structure**

| Field             | Type        |          | Null | Key | Default | Extra | Comment |
| :---------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)     | INT         | UNSIGNED | NO   | PRI |         |       |         |
| [source](#source) | VARCHAR(40) |          | NO   | PRI |         |       |         |
| [data](#data)     | TEXT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### guid

References `characters.guid` – the character the settings belong to.

### source

Identifier of the setting group / module that owns this row.

### data

Serialized setting payload for the given `source`.
