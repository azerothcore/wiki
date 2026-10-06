# realmcharacters

[<-Back-to:Auth](database-auth)

**The \`realmcharacters\` table**

This table holds information on the number of characters each account has for each realm.
The data in this table is maintained by the core.

**Table: realmcharacters's Structure**

| Field                 | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [realmid](#realmid)   | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [acctid](#acctid)     | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [numchars](#numchars) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### realmid

The ID of the realm. See [realmlist.id](realmlist#id).

### acctid

The account ID. See [account.id](account#id).

### numchars

The number of characters the account has on the realm.
