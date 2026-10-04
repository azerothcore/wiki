# instance\_encounters

[<-Back-to:World](database-world)

**The \`instance\_encounters\` table**

Definitions of instance encounters. Used by LFG.

**Table: instance\_encounters's Structure**

| Field                                         | Type         |          | Null | Key | Default | Extra | Comment                                                                 |
| :-------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------------------------------------- |
| [entry](#entry)                               | INT          | UNSIGNED | NO   | PRI |         |       | Unique entry from DungeonEncounter.dbc                                  |
| [creditType](#credittype)                     | TINYINT      | UNSIGNED | NO   |     | 0       |       |                                                                         |
| [creditEntry](#creditentry)                   | INT          | UNSIGNED | NO   |     | 0       |       |                                                                         |
| [lastEncounterDungeon](#lastencounterdungeon) | SMALLINT     | UNSIGNED | NO   |     | 0       |       | If not 0, LfgDungeon.dbc entry for the instance it is last encounter in |
| [comment](#comment)                           | VARCHAR(255) |          | NO   |     | ''      |       |                                                                         |

**Description of the table's fields**

### entry

Unique entry from [DungeonEncounter.dbc](https://wowdev.wiki/DB/DungeonEncounter)

### creditType

See enum EncounterCreditType.

ENCOUNTER\_CREDIT\_KILL\_CREATURE = 0

ENCOUNTER\_CREDIT\_CAST\_SPELL = 1

### creditEntry

If creditType = 0, then value for this field is creature entry. See creature\_template.entry

If creditType = 1, then value for this field is a spell. See Spell.dbc.

### lastEncounterDungeon

Reference to [LfgDungeon.dbc](https://wowdev.wiki/DB/LFGDungeons) entry for the instance it which is this encounter last. If 0, encounter is not last one.

### comment

Instance encounter comment for easy identification. Encounter name used only.
