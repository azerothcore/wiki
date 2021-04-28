# ip\_banned

[<-Back-to:Auth](database-auth.md)

**The \`ip\_banned\` table**

This table contains all of the banned IPs and the date when (or if) the ban will expire.

**Structure**

| Field          | Type         | Attributes | Key | Null | Default   | Extra | Comment |
|----------------|--------------|------------|-----|------|-----------|-------|---------|
| [ip][1]        | VARCHAR(15)  |            | PRI | NO   | 127.0.0.1 |       |         |
| [bandate][2]   | INT(10)      | UNSIGNED   | PRI | NO   |           |       |         |
| [unbandate][3] | INT(10)      | UNSIGNED   |     | NO   |           |       |         |
| [bannedby][4]  | VARCHAR(50)  |            |     | NO   | [Console] |       |         |
| [banreason][5] | VARCHAR(255) |            |     | NO   | no reason |       |         |

[1]: #ip
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason

**Description of the fields**

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
