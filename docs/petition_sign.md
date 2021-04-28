# petition\_sign

[<-Back-to:Characters](database-characters.md)

**The \`petition\_sign\` table**

This table holds information on all the signatures of a petition for either a guild or an arena team.

**Structure**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment |
|---------------------|------------|------------|-----|------|---------|-------|---------|
| [ownerguid][1]      | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [petitionguid][2]   | INT(10)    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [playerguid][3]     | INT(10)    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [player_account][4] | INT(10)    | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]           | TINYINT(3) | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #playerguid
[4]: #player_account
[5]: #type

**Description of the fields**

### ownerguid

The GUID of the owner that is trying to make the guild/arena team. See characters.guid

### petitionguid

The GUID of the charter item. See item\_template.guid

### playerguid

The GUID of the player that has SIGNED the charter. See characters.guid

### player\_account

The account ID of the player that has SIGNED the charter. No two players can sign the same charter from the same account.

### type

The type of the petition.

| ID | Type               |
|----|--------------------|
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
