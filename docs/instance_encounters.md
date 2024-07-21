# instance\_encounters

[<-Back-to:World](database-world)

**The \`instance\_encounters\` table**

Definitions of instance encounters. Used by LFG.

**Table Structure**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| ------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [entry][1]                | INT          | UNSIGNED   | PRI | NO   | 0       |       | Unique entry from DungeonEncounter.dbc                                  |
| [creditType][2]           | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                                                                         |
| [creditEntry][3]          | INT          | UNSIGNED   |     | NO   | 0       |       |                                                                         |
| [lastEncounterDungeon][4] | SMALLINT     | UNSIGNED   |     | NO   | 0       |       | If not 0, LfgDungeon.dbc entry for the instance it is last encounter in |
| [comment][5]              | varchat(255) | SIGNED     |     | NO   | "       |       |                                                                         |

[1]: #entry
[2]: #credittype
[3]: #creditentry
[4]: #lastencounterdungeon
[5]: #comment

**Description of the fields**

### entry

Unique entry from [DungeonEncounter.dbc](DungeonEncounter)

### creditType

See enum EncounterCreditType.

ENCOUNTER\_CREDIT\_KILL\_CREATURE = 0

ENCOUNTER\_CREDIT\_CAST\_SPELL = 1

### creditEntry

If creditType = 0, then value for this field is creature entry. See creature\_template.entry

If creditType = 1, then value for this field is a spell. See Spell.dbc.

### lastEncounterDungeon

Reference to [LfgDungeon.dbc](LfgDungeon) entry for the instance it which is this encounter last. If 0, encounter is not last one.

### comment

Instance encounter comment for easy identification. Encounter name used only.
