# lfg\_entrances

[<-Volver a:World](database-world)

**Tabla \`lfg\_entrances\`**

Usada por el sistema LFG para teletransportar a los jugadores a una posición especificada. En el futuro, esta tabla debería usarse en lugar de la tabla \`areatrigger_teleport\` para todas las mazmorras.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------------------- |
| [dungeonId][1]   | INT          | UNSIGNED   | PRI | NO   | 0       |       | Entry de la mazmorra del dbc |
| [name][2]        | VARCHAR(255) |            |     | YES  | NULL    |       | Nombre de la mazmorra del dbc |
| [position_x][3]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [position_y][4]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [position_z][5]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [orientation][6] | FLOAT        |            |     | NO   | 0       |       |                        |

[1]: #dungeonid
[2]: #name
[3]: #position_x
[4]: #position_y
[5]: #position_z
[6]: #orientation

**Descripción de los campos**

### dungeonId

ID de la mazmorra de LFGDungeons.dbc

### name

Nombre de la mazmorra de LFGDungeons.dbc

### position\_x

Coordenada X de la posición de entrada

### position\_y

Coordenada Y de la posición de entrada

### position\_z

Coordenada Z de la posición de entrada

### orientation

Orientación que tendrá el jugador al aparecer en esta ubicación
