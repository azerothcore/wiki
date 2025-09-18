# channels\_rights

[<-Volver a:Characters](database-characters)

**Tabla \`channels\_rights\`**

**Estructura**

| Campo             | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ----------------- | ------------ | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [name][1]         | VARCHAR(128) | SIGNED    | PRI   | NO   |             |       |            |
| [flags][2]        | INT          | UNSIGNED  |       | NO   |             |       |            |
| [speakdelay][3]   | INT          | UNSIGNED  |       | NO   |             |       |            |
| [joinmessage][4]  | VARCHAR(255) | SIGNED    |       | NO   | ''          |       |            |
| [delaymessage][5] | VARCHAR(255) | SIGNED    |       | NO   | ''          |       |            |
| [moderators][6]   | TEXT         | SIGNED    |       | YES  |             |       |            |

[1]: #name
[2]: #flags
[3]: #speakdelay
[4]: #joinmessage
[5]: #delaymessage
[6]: #moderators

**Descripción de los Campos**

### name

`field-no-description|1`

### flags

`field-no-description|2`

### speakdelay

`field-no-description|3`

### joinmessage

`field-no-description|4`

### delaymessage

`field-no-description|5`

### moderators

`field-no-description|6`
