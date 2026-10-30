# guild

[<-Back-to:Characters](database-characters)

**The \`guild\` table**

This table holds the main guild information. All created guilds or all guilds in the process of being created have a record in this table.

**Table: guild's Structure**

| Field                               | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guildid](#guildid)                 | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [name](#name)                       | VARCHAR(24)  |          | NO   |     | ''      |       |         |
| [leaderguid](#leaderguid)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [EmblemStyle](#emblemstyle)         | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [EmblemColor](#emblemcolor)         | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [BorderStyle](#borderstyle)         | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [BorderColor](#bordercolor)         | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [BackgroundColor](#backgroundcolor) | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [info](#info)                       | VARCHAR(500) |          | NO   |     | ''      |       |         |
| [motd](#motd)                       | VARCHAR(128) |          | NO   |     | ''      |       |         |
| [createdate](#createdate)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [BankMoney](#bankmoney)             | BIGINT       | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guildid

The ID of the guild. This number is unique to each guild and is the main method to identify a guild.

### name

The guild name.

### leaderguid

The GUID of the character who created the guild. See [characters.guid](characters#guid).

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
