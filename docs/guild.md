# guild

[<-Back-to:Characters](database-characters.md)

**The \`guild\` table**

This table holds the main guild information. All created guilds or all guilds in the process of being created have a record in this table.

**Structure**

| Field                | Type         | Attributes | Key | Null | Default | Extra  | Comment |
|----------------------|--------------|------------|-----|------|---------|--------|---------|
| [guildid][1]         | int(10)      | unsigned   | PRI | NO   | 0       | Unique |         |
| [name][2]            | varchar(24)  | signed     |     | NO   | "       |        |         |
| [leaderguid][3]      | int(10)      | unsigned   |     | NO   | 0       |        |         |
| [EmblemStyle][4]     | tinyint(3)   | unsigned   |     | NO   | 0       |        |         |
| [EmblemColor][5]     | tinyint(3)   | unsigned   |     | NO   | 0       |        |         |
| [BorderStyle][6]     | tinyint(3)   | unsigned   |     | NO   | 0       |        |         |
| [BorderColor][7]     | tinyint(3)   | unsigned   |     | NO   | 0       |        |         |
| [BackgroundColor][8] | tinyint(3)   | signed     |     | NO   | 0       |        |         |
| [info][9]            | text         | signed     |     | NO   | "       |        |         |
| [motd][10]           | varchar(128) | signed     |     | NO   | "       |        |         |
| [createdate][11]     | int(10)      | unsigned   |     | NO   | 0       |        |         |
| [BankMoney][12]      | bigint(20)   | signed     |     | NO   | 0       |        |         |

[1]: #guildid
[2]: #name
[3]: #leaderguid
[4]: #emblemstyle
[5]: #emblemcolor
[6]: #borderstyle
[7]: #bordercolor
[8]: #backgroundcolor
[9]: #info
[10]: #motd
[11]: #createdate
[12]: #bankmoney

**Description of the fields**

### guildid

The ID of the guild. This number is unique to each guild and is the main method to identify a guild.

### name

The guild name.

### leaderguid

The GUID of the character who created the guild. See characters.guid

### EmblemStyle

The emblem style of the guild tabard.

### EmblemColor

The emblem color of the guild tabard.

### BorderStyle

The border style of the guild tabard.

### BorderColor

The border color of the guild tabard.

### BackgroundColor

The background color of the guild tabard.

### info

The text message that appears in the Guild Information box.

### motd

The text that appears in the Message Of The Day box.

### createdate

The date when the guild was created.

### BankMoney

The total money, in copper, that is currently in the guild's guild bank.
