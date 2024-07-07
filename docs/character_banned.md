# character\_banned

[<-Back-to:Characters](database-characters)

**The \`character\_banned\` table**

This table lists all of the characters that have been banned along with the date when (or if) the ban will expire.

**Table Structure**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]      | INT          | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |                          |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |                          |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### bandate

The date when the character was banned, in Unix time.

### unbandate

The date when the character will be automatically unbanned, in Unix time. A value less than the current date means, in effect, a permanent ban.

### bannedby

The character with the rights to the .ban command that banned the character.

### banreason

The reason for the ban.

### active

Boolean 0 or 1 controlling if the ban is currently active or not.
