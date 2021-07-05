# realmcharacters

[<-Back-to:Auth](database-auth.md)

**The \`realmcharacters\` table**

This table holds information on the number of characters each account has for each realm.
The data in this table is maintained by the core.

## Structure

| Field         | Type       | Attributes | Key | Null | Default | Extra | Comment |
|---------------|------------|------------|-----|------|---------|-------|---------|
| [realmid][1]  | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [acctid][2]   | INT        | UNSIGNED   | PRI | NO   |         |       |         |
| [numchars][3] | TINYINT    | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #realmid
[2]: #acctid
[3]: #numchars

## Description of the fields

### realmid

The ID of the realm. See [realmlist.id](realmlist#id)

### acctid

The account ID. See [account.id](account#id)

### numchars

The number of characters the account has on the realm.
