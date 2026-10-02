# mail\_server\_character

[<-Back-to:Characters](database-characters)

**The \`mail\_server\_character\` table**

This table keeps entries of which player has received a server mail. This prevents the same mail to be sent twice to the same player.

Note: Entries in this table will be deleted automatically when the referenced entry in [mail_server_template.id](mail_server_template#id) is deleted. CONSTRAINT `fk_mail_server_character`

**Table: mail\_server\_character's Structure**

| Field       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [mailId][2] | INT  | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #guid
[2]: #mailid

**Description of the table's fields**

### guid

[characters.guid](characters#guid).

### mailId

[mail_server_template.id](mail_server_template#id).
