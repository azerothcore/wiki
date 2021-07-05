# logs\_ip\_actions

[<-Volver a:Auth](database-auth.md)

**Tabla \`logs\_ip\_actions\`**

## Estructura

| Field               | Type        | Attributes | Key | Null | Default           | Extra          | Comment                       |
|---------------------|-------------|------------|-----|------|-------------------|----------------|-------------------------------|
| [id][1]             | INT     | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Unique Identifier             |
| [account_id][2]     | INT     | UNSIGNED   |     | NO   |                   |                | Account ID                    |
| [character_guid][3] | INT     | UNSIGNED   |     | NO   |                   |                | Character Guid                |
| [type][4]           | TINYINT  | UNSIGNED   |     | NO   |                   |                |                               |
| [ip][5]             | VARCHAR(15) |            |     | NO   | 127.0.0.1         |                |                               |
| [systemnote][6]     | text        |            |     | YES  |                   |                | Notes inserted by system      |
| [unixtime][7]       | INT     | UNSIGNED   |     | NO   |                   |                | Unixtime                      |
| [time][8]           | TIMESTAMP   |            |     | NO   | CURRENT_TIMESTAMP |                | TIMESTAMP                     |
| [comment][9]        | text        |            |     | YES  |                   |                | Allows users to add a comment |

[1]: #id
[2]: #account_id
[3]: #character_guid
[4]: #type
[5]: #ip
[6]: #systemnote
[7]: #unixtime
[8]: #time
[9]: #comment

## Descripción de los campos

### id

### account_id

### character_guid

### type

### ip

### systemnote

### unixtime

### time

### comment