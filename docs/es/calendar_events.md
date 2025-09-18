# calendar\_events

[<-Volver a:Characters](database-characters)

**Tabla \`calendar\_events\`**

**Estructura**

| Campo            | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario  |
| ---------------- | ------------ | --------- | ----- | ---- | ----------- | ----- | ----------- |
| [id][1]          | BIGINT       | UNSIGNED  | PRI   | NO   | 0           |       |             |
| [creator][2]     | INT          | UNSIGNED  |       | NO   | 0           |       |             |
| [title][3]       | VARCHAR(255) | SIGNED    |       | NO   | ''          |       |             |
| [description][4] | VARCHAR(255) | SIGNED    |       | NO   | ''          |       |             |
| [type][5]        | TINYINT      | UNSIGNED  |       | NO   | 4           |       |             |
| [dungeon][6]     | INT          | SIGNED    |       | NO   | -1          |       |             |
| [eventtime][7]   | INT          | UNSIGNED  |       | NO   | 0           |       |             |
| [flags][8]       | INT          | UNSIGNED  |       | NO   | 0           |       |             |
| [time2][9]       | INT          | UNSIGNED  |       | NO   | 0           |       |             |

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

`field-no-description|1`

### creator

`field-no-description|2`

### title

`field-no-description|3`

### description

`field-no-description|4`

### type

`field-no-description|5`

### dungeon

`field-no-description|6`

### eventtime

`field-no-description|7`

### flags

`field-no-description|8`

### time2

`field-no-description|9`
