# instance\_encounters

[<-Volver a:World](database-world)

**Tabla \`instance\_encounters\`**

Definiciones de los encuentros (encounters) de instancia. Usada por LFG.

**Estructura**

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

**Descripción de los campos**

### entry

Entry único de [DungeonEncounter.dbc](dungeonencounter)

### creditType

Ver enum EncounterCreditType.

ENCOUNTER\_CREDIT\_KILL\_CREATURE = 0

ENCOUNTER\_CREDIT\_CAST\_SPELL = 1

### creditEntry

Si creditType = 0, entonces el valor de este campo es el entry de una creature. Ver creature\_template.entry

Si creditType = 1, entonces el valor de este campo es un spell. Ver Spell.dbc.

### lastEncounterDungeon

Referencia al entry de [LfgDungeon.dbc](lfgdungeon) para la instancia en la que este encounter es el último. Si es 0, el encounter no es el último.

### comment

Comentario del encounter de instancia para identificarlo fácilmente. Solo se usa el nombre del encounter.
