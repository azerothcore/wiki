# calendar\_events

[<-Volver a:Characters](database-characters)

**Tabla \`calendar\_events\`**

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment  |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | -------- |
| [id][1]          | BIGINT       | UNSIGNED   | PRI | NO   | 0       |       |          |
| [creator][2]     | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [title][3]       | VARCHAR(255) | SIGNED     |     | NO   | ''      |       |          |
| [description][4] | VARCHAR(255) | SIGNED     |     | NO   | ''      |       |          |
| [type][5]        | TINYINT      | UNSIGNED   |     | NO   | 4       |       |          |
| [dungeon][6]     | INT          | SIGNED     |     | NO   | -1      |       |          |
| [eventtime][7]   | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [flags][8]       | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [time2][9]       | INT          | UNSIGNED   |     | NO   | 0       |       |          |

[1]: #id
[3]: #creator
[4]: #title
[5]: #description
[6]: #type
[7]: #dungeon
[8]: #eventtime
[9]: #flags
[10]: #time2

**Descripción de los Campos**

### id

`field-no-description|1` (ID del calendario)

### creator

`field-no-description|2` (¿GUID del creador?)

### title

`field-no-description|3` (Título del mismo)

### description

`field-no-description|4` (Descripción del mismo)

### type

`field-no-description|5` (¿Tipo del mismo? Se desconoce de dónde puede extraerse aquella información)

### dungeon

`field-no-description|6` (¿Evento de Mazmorra o Raid?)

### eventtime

`field-no-description|7` (¿Tiempo hasta que llegue el evento?)

### flags

`field-no-description|8` (Marcadores o "flags" del evento)

### time2

`field-no-description|9` (¿Tiempo hasta que finalice el evento?)
