# petition\_sign

[<-Back-to:Characters](database-characters)

**The \`petition\_sign\` table**

This table holds information on all the signatures of a petition for either a guild or an arena team.

**Table Structure**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ownerguid][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [petitionguid][2]   | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [playerguid][3]     | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [player_account][4] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #playerguid
[4]: #playeraccount
[5]: #type

**Description of the fields**

### ownerguid

The GUID of the owner that is trying to make the guild/arena team. See [characters.guid](characters#guid).

### petitionguid

The GUID of the charter item. See [item\_template.guid](item_template#guid).

### playerguid

The GUID of the player that has signed the charter. See [characters.guid](characters#guid).

### player\_account

The account ID of the player that has signed the charter. No two players can sign the same charter from the same account.

### type

The type of the petition.

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
