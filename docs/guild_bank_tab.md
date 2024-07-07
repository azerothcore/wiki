# guild\_bank\_tab

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_tab\` table**

This table holds information on all the tabs in use for all guilds that make use of the guild bank.

**Table Structure**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1] | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]   | TINYINT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabName][3] | VARCHAR(16)  | SIGNED     |     | NO   | "       |       |         |
| [TabIcon][4] | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| [TabText][5] | VARCHAR(500) | SIGNED     |     | YES  |         |       |         |

[1]: #guildid
[2]: #tabid
[3]: #tabname
[4]: #tabicon
[5]: #tabtext

**Description of the fields**

### guildid

The guild ID that the guild bank belongs to.

### TabId

The tab ID.

### TabName

The name assigned to the tab.

### TabIcon

The icon assigned to the tab.

### TabText

The text assigned to the tab.
