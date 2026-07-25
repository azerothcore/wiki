# lfg\_dungeon\_encounters

[<-Volver a:World](database-world)

**Tabla \`lfg\_dungeon\_encounters\`**

**Estructura**

| Field              | Type | Attributes | Key | Null | Default | Extra | Comment                                   |
| ------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------- |
| [achievementId][1] | INT  | UNSIGNED   | PRI | NO   | 0       |       | Logro que marca la finalización del jefe final |
| [dungeonId][2]     | INT  | UNSIGNED   |     | NO   | 0       |       | Entry de la mazmorra del dbc              |

[1]: #achievementid
[2]: #dungeonid

**Descripción de los campos**

### achievementId

No se sabe, pero seguramente se toma de [Achievement.dbc](achievement)

### dungeonId

ID de la mazmorra de LFGDungeons.dbc
