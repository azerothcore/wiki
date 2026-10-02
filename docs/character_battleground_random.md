# character\_battleground\_random

[<-Back-to:Characters](database-characters)

**The \`character\_battleground\_random\` table**

This table stores battlegrounds IDs for random battleground sessions.

**Table: character\_battleground\_random's Structure**

| Field     | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1] | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #guid

**Description of the table's fields**

### guid

The guid of the character who has already won random battleground today. See [characters.guid](characters#guid).
