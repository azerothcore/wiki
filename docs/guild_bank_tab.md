# guild\_bank\_tab

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_tab\` table**

This table holds information on all the tabs in use for all guilds that make use of the guild bank.

**Table: guild\_bank\_tab's Structure**

| Field               | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guildid](#guildid) | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [TabId](#tabid)     | TINYINT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [TabName](#tabname) | VARCHAR(16)  |          | NO   |     | ''      |       |         |
| [TabIcon](#tabicon) | VARCHAR(100) |          | NO   |     | ''      |       |         |
| [TabText](#tabtext) | VARCHAR(500) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
