# account\_banned

[<-Back-to:Auth](database-auth)

**The \`account\_banned\` table**

This table lists all of the accounts that have been banned along with the date when (or if) the ban will expire.

**Table: account\_banned's Structure**

| Field                   | Type         |          | Null | Key | Default | Extra | Comment    |
| :---------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :--------- |
| [id](#id)               | INT          | UNSIGNED | NO   | PRI | 0       |       | Account id |
| [bandate](#bandate)     | INT          | UNSIGNED | NO   | PRI | 0       |       |            |
| [unbandate](#unbandate) | INT          | UNSIGNED | NO   |     | 0       |       |            |
| [bannedby](#bannedby)   | VARCHAR(50)  |          | NO   |     |         |       |            |
| [banreason](#banreason) | VARCHAR(255) |          | NO   |     |         |       |            |
| [active](#active)       | TINYINT      | UNSIGNED | NO   |     | 1       |       |            |

**Description of the table's fields**

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
