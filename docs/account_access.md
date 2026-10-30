# account\_access

[<-Back-to:Auth](database-auth)

**The \`account\_access\` table**

This table holds security access level for any realm in [realmlist](realmlist) table.

**Table: account\_access's Structure**

| Field               | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)           | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [gmlevel](#gmlevel) | TINYINT      | UNSIGNED | NO   |     |         |       |         |
| [RealmID](#realmid) | INT          |          | NO   | PRI | -1      |       |         |
| [comment](#comment) | VARCHAR(255) |          | YES  |     | ''      |       |         |

**Description of the table's fields**

### id

The [account ID](account#id).

### gmlevel

The account security level. Different levels have access to different commands. The individual level required for a command is defined in the [command](command) table in each realm.

### RealmID

The [Realm ID](realmlist#id).

### comment

A description of the row. Not used by the core.
