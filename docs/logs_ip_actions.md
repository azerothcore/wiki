# logs\_ip\_actions

[<-Back-to:Auth](database-auth.md)

**The \`logs\_ip\_actions\` table**

**Structure**

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

**Description of the fields**

### id

`field-no-description|1`

### account\_id

`field-no-description|2`

### character\_guid

`field-no-description|3`

### type

`field-no-description|4`

### ip

`field-no-description|5`

### systemnote

`field-no-description|6`

### unixtime

`field-no-description|7`

### time

`field-no-description|8`

### comment

`field-no-description|9`
