# mail_server_character

[<-Back-to:Character](database-character.md)

**The \`mail_server_character\` table**

This table keeps entries of which player has received a server mail. This prevents the same mail to be sent twice to the same player.

**Structure**

| Field       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [mailId][2] | INT  | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #guid
[2]: #mailId

## Description of the fields

### guid

[characters.guid](characters#guid).

### mailId

[mail_server_template.id](mail_server_template#guid).
