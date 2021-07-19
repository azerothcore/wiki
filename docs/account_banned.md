# account\_banned

[<-Back-to:Auth](database-auth.md)

Read in: [English :gb:](account_banned) [Spanish :es:](es/account_banneds)

**The \`account\_banned\` table**

This table lists all of the accounts that have been banned along with the date when (or if) the ban will expire.

**Structure**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment    |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       | Account id |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |            |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |            |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |            |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |            |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |            |

[1]: #id
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**Description of the fields**

### id

The account ID. See [account.id](account#id).

### bandate

The date when the account was banned, in Unix time.

### unbandate

The date when the account will be automatically unbanned, in Unix time. A value less than the current date means, in effect, a permanent ban.

### bannedby

The GM character's name who banned that account. If banned from the console, then it will be empty (until improved).

### banreason

The reason for the ban.

### active

Boolean 0 or 1 controlling if the ban is currently active or not.
