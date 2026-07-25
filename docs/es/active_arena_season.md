# active_arena_season

[<-Volver a:Characters](database-characters)

**Tabla \`active_arena_season\`**

Contiene información sobre la temporada de arena actual.

**Estructura**

| Field                        | Type    | Attributes | Key | Null | Default | Extra | Comment                                            |
| ---------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------- |
| [season_id](#seasonid)       | TINYINT | UNSIGNED   |     | NO   |         |       |                                                    |
| [season_state](#seasonstate) | TINYINT | UNSIGNED   |     | NO   |         |       | Supported 2 states: 0 - disabled; 1 - in progress. |

**Descripción de los campos**

### season_id

ID de la temporada actual.

### season_state

| value | comment       |
| ----- | ------------- |
| 0     | desactivada   |
| 1     | en progreso   |
