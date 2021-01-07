# guild\_bank\_tab

[<-Back-to:Characters](database-characters.md)

**The \`guild\_bank\_tab\` table**

This table holds information on all the tabs in use for all guilds that make use of the guild bank.

**Structure**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------|--------------|------------|-----|------|---------|-------|---------|
| [guildid][1] | int(10)      | unsigned   | PRI | NO   | 0       |       |         |
| [TabId][2]   | tinyint(3)   | unsigned   | PRI | NO   | 0       |       |         |
| [TabName][3] | varchar(16)  | signed     |     | NO   | "       |       |         |
| [TabIcon][4] | varchar(100) | signed     |     | NO   | "       |       |         |
| [TabText][5] | varchar(500) | signed     |     | YES  | NULL    |       |         |

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
