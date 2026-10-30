# character\_banned

[<-Back-to:Characters](database-characters)

**The \`character\_banned\` table**

This table lists all of the characters that have been banned along with the date when (or if) the ban will expire.

**Table: character\_banned's Structure**

| Field                   | Type         |          | Null | Key | Default | Extra | Comment                  |
| :---------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)           | INT          | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [bandate](#bandate)     | INT          | UNSIGNED | NO   | PRI | 0       |       |                          |
| [unbandate](#unbandate) | INT          | UNSIGNED | NO   |     | 0       |       |                          |
| [bannedby](#bannedby)   | VARCHAR(50)  |          | NO   |     |         |       |                          |
| [banreason](#banreason) | VARCHAR(255) |          | NO   |     |         |       |                          |
| [active](#active)       | TINYINT      | UNSIGNED | NO   |     | 1       |       |                          |

**Description of the table's fields**

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
