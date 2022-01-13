# lfg\_data

[<-Volver a:Characters](database-characters.md)

**Tabla \`lfg\_data\`**

Esta tabla contiene datos guardados para LFG. Esta tabla está constantemente en uso por parte del núcleo.

**Estructura**

| Field        | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------ | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [dungeon][2] | INT     | UNSIGNED   |     | NO   | 0       |       |                          |
| [state][3]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #dungeon
[3]: #state

**Descripción de los campos**

### guid

La guid para este grupo.

### dungeon

El ID de la mazmorra de dbc.

### state

El estado de este grupo/mazmorra.
