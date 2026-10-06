# petition\_sign

[<-Back-to:Characters](database-characters)

**The \`petition\_sign\` table**

This table holds information on all the signatures of a petition for either a guild or an arena team.

**Table: petition\_sign's Structure**

| Field                            | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ownerguid](#ownerguid)          | INT     | UNSIGNED | NO   | MUL |         |       |         |
| [petitionguid](#petitionguid)    | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [petition_id](#petitionid)       | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [playerguid](#playerguid)        | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [player_account](#playeraccount) | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [type](#type)                    | TINYINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ownerguid

The GUID of the owner that is trying to make the guild/arena team. See [characters.guid](characters#guid).

### petitionguid

The GUID of the charter item. See [item\_instance.guid](item_instance#guid).

### petition_id

Sequential identifier of the petition being signed. Matches [petition.petition_id](petition#petitionid).

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
