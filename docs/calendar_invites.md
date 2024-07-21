# calendar\_invites

[<-Back-to:Characters](database-characters)

**The \`calendar\_invites\` table**

**Table Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]         | BIGINT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [event][2]      | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |
| [invitee][3]    | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [sender][4]     | INT          | UNSIGNED   |     | NO   | ''      |       |         |
| [status][5]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [statustime][6] | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [rank][7]       | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [text][8]       | VARCHAR(255) | SIGNED     |     | NO   | ''      |       |         |

[1]: #id
[2]: #event
[3]: #invitee
[4]: #sender
[5]: #status
[6]: #statustime
[7]: #rank
[8]: #text

**Description of the fields**

### id

`field-no-description|1`

### event

`field-no-description|2`

### invitee

`field-no-description|3`

### sender

`field-no-description|4`

### status

`field-no-description|5`

### rank

`field-no-description|6`

### eventtime

`field-no-description|7`

### text

`field-no-description|8`
