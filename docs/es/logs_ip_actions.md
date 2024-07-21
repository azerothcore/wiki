# logs\_ip\_actions

[<-Volver a:Auth](database-auth)

Leer en: [English :gb:](../logs_ip_actions) [Spanish :es:](logs_ip_actions)

**Tabla \`logs\_ip\_actions\`**

**Estructura**

| Field               | Type        | Attributes | Key | Null | Default           | Extra          | Comment                       |
| ------------------- | ----------- | ---------- | --- | ---- | ----------------- | -------------- | ----------------------------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Unique Identifier             |
| [account_id][2]     | INT         | UNSIGNED   |     | NO   |                   |                | Account ID                    |
| [character_guid][3] | INT         | UNSIGNED   |     | NO   |                   |                | Character Guid                |
| [type][4]           | TINYINT     | UNSIGNED   |     | NO   |                   |                |                               |
| [ip][5]             | VARCHAR(15) | SIGNED     |     | NO   | 127.0.0.1         |                |                               |
| [systemnote][6]     | TEXT        | SIGNED     |     | YES  |                   |                | Notes inserted by system      |
| [unixtime][7]       | INT         | UNSIGNED   |     | NO   |                   |                | Unixtime                      |
| [time][8]           | TIMESTAMP   | SIGNED     |     | NO   | CURRENT_TIMESTAMP |                | Timestamp                     |
| [comment][9]        | TEXT        | SIGNED     |     | YES  |                   |                | Allows users to add a comment |

[1]: #id
[2]: #accountid
[3]: #characterguid
[4]: #type
[5]: #ip
[6]: #systemnote
[7]: #unixtime
[8]: #time
[9]: #comment

**Descripción de los campos**

### id

`campo-sin-descripción|1`

### account\_id

`campo-sin-descripción|2`

### character\_guid

`campo-sin-descripción|3`

### type

`campo-sin-descripción|4`

### ip

`campo-sin-descripción|5`

### systemnote

`campo-sin-descripción|6`

### unixtime

`campo-sin-descripción|7`

### time

`campo-sin-descripción|8`

### comment

`campo-sin-descripción|9`
