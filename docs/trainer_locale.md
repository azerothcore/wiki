# trainer locale

[<-Back-to:World](database-world)

**The \`trainer\_locale\` table**

This table lists trainer templates (a trainer identifier and metadata). Spells a trainer can teach are stored in the related [trainer_spell](trainer_spell) table.

**Table Structure**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | :-: | :--: | ------- | ----- | ------- |
| [Id](#id)                       | INT        | unsigned   | PRI |  NO  | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            |     |  NO  |         |       |         |
| [Greeting_lang](#greeting)      | MEDIUMTEXT |            |     | YES  | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        | signed     |     | YES  | 0       |       |         |

**Description of fields**

### Id

Unique trainer ID. This ID is referenced by the [trainer_spell](trainer_spell) table to link localized strings to a trainer template.

### locale

Localization code for the row.

| Locale |
| ------ |
| koKR   |
| frFR   |
| deDE   |
| zhCN   |
| zhTW   |
| esES   |
| esMX   |
| ruRU   |

### Greeting_lang

Localized text shown at the top of the trainer window when opened. This is the localized equivalent of the `Greeting` column in `trainer`.

{% include note.html content="This is not the gossip text." %}

### VerifiedBuild

Used by AzerothCore to indicate whether this localized entry was verified against WDB files.

- `0` = not parsed
- `>0` = parsed with WDB files from that client build
- `-1` = placeholder until proper data is found
- -[Client Build](realmlist#gamebuild) = parsed with WDB files from that specific client build and manually edited for special reasons
