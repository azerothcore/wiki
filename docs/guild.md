# guild

[<-Back-to:Characters](database-characters.md)

**The \`guild\` table**

This table holds the main guild information. All created guilds or all guilds in the process of being created have a record in this table.

**Structure**

| Field                | Type         | Attributes | Key | Null | Default | Extra  | Comment |
|----------------------|--------------|------------|-----|------|---------|--------|---------|
| [guildid][1]         | INT      | UNSIGNED   | PRI | NO   | 0       | Unique |         |
| [name][2]            | VARCHAR(24)  | SIGNED     |     | NO   |         |        |         |
| [leaderguid][3]      | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [EmblemStyle][4]     | TINYINT   | UNSIGNED   |     | NO   | 0       |        |         |
| [EmblemColor][5]     | TINYINT   | UNSIGNED   |     | NO   | 0       |        |         |
| [BorderStyle][6]     | TINYINT   | UNSIGNED   |     | NO   | 0       |        |         |
| [BorderColor][7]     | TINYINT   | UNSIGNED   |     | NO   | 0       |        |         |
| [BackgroundColor][8] | TINYINT   | SIGNED     |     | NO   | 0       |        |         |
| [info][9]            | text         | SIGNED     |     | NO   |         |        |         |
| [motd][10]           | VARCHAR(128) | SIGNED     |     | NO   |         |        |         |
| [createdate][11]     | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [BankMoney][12]      | BIGINT   | SIGNED     |     | NO   | 0       |        |         |

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
