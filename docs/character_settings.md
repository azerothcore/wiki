# character_settings

[<-Back-to:Characters](database-characters)

**The `character_settings` table**

Stores arbitrary per-character settings as keyed data blobs. Modules and subsystems use this table to persist their own character-scoped configuration. `guid` references `characters.guid`.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid](#guid) | INT | UNSIGNED | PRI | NO |  |  |  |
| [source](#source) | VARCHAR(40) |  | PRI | NO |  |  |  |
| [data](#data) | TEXT |  |  | YES | (NULL) |  |  |

**Description of the fields**

### guid

References `characters.guid` – the character the settings belong to.

### source

Identifier of the setting group / module that owns this row.

### data

Serialized setting payload for the given `source`.
