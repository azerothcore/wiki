# ip\_banned

[<-Back-to:Auth](database-auth)

**The \`ip\_banned\` table**

This table contains all of the banned IPs and the date when (or if) the ban will expire.

**Table: ip\_banned's Structure**

| Field                   | Type         |          | Null | Key | Default   | Extra | Comment |
| :---------------------- | :----------- | :------- | :--: | :-: | :-------: | :---: | :------ |
| [ip](#ip)               | VARCHAR(15)  |          | NO   | PRI | 127.0.0.1 |       |         |
| [bandate](#bandate)     | INT          | UNSIGNED | NO   | PRI |           |       |         |
| [unbandate](#unbandate) | INT          | UNSIGNED | NO   |     |           |       |         |
| [bannedby](#bannedby)   | VARCHAR(50)  |          | NO   |     | [Console] |       |         |
| [banreason](#banreason) | VARCHAR(255) |          | NO   |     | no reason |       |         |

**Description of the table's fields**

### ip

The IP address that is banned.

### bandate

The date when the IP was first banned, in Unix time.

### unbandate

The date when the IP will be unbanned in Unix time. Any date that is set lower than the current date basically classifies as a permanent ban as it will never auto expire.

### bannedby

The name of the character that banned the IP. The character should belong to an account with the rights to the .ban command in-game.

### banreason

The reason given for the IP ban.
