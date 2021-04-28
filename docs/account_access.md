# account\_access

[<-Back-to:Auth](database-auth.md)

**The \`account\_access\` table**

This table holds security access level for any realm in [realmlist](realmlist) table.

**Structure**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------|--------------|------------|-----|------|---------|-------|---------|
| [id][1]      | INT(10)      | UNSIGNED   | PRI | NO   |         |       |         |
| [gmlevel][2] | TINYINT(3)   | UNSIGNED   |     | NO   |         |       |         |
| [RealmID][3] | INT(11)      | SIGNED     | PRI | NO   | -1      |       |         |
| [comment][4] | VARCHAR(255) |            |     | YES  |         |       |         |

[1]: #id
[2]: #gmlevel
[3]: #realmid
[4]: #comment

**Description of the fields**

### id

The [account ID](account#id).

### gmlevel

The account security level. Different levels have access to different commands. The individual level required for a command is defined in the [command](command) table in each realm.

### RealmID

The [Realm ID](realmlist#id).

### comment
