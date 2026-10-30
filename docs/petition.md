# petition

[<-Back-to:Characters](database-characters)

**The \`petition\` table**

This table holds information on all ongoing petitions for a guild or for an arena team.

**Table: petition's Structure**

| Field                         | Type        |          | Null | Key | Default | Extra | Comment |
| :---------------------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ownerguid](#ownerguid)       | INT         | UNSIGNED | NO   | PRI |         |       |         |
| [petitionguid](#petitionguid) | INT         | UNSIGNED | YES  |     | 0       |       |         |
| [petition_id](#petitionid)    | INT         | UNSIGNED | NO   | MUL | 0       |       |         |
| [name](#name)                 | VARCHAR(24) |          | NO   |     |         |       |         |
| [type](#type)                 | TINYINT     | UNSIGNED | NO   | PRI | 0       |       |         |

**Description of the table's fields**

### ownerguid

The petition's owner's GUID. See [characters.guid](characters#guid).

### petitionguid

The GUID of the petition item. See [item\_instance.guid](item_instance#guid).

### petition_id

Sequential identifier of the petition, unique per petition. Used to reference the petition independently of the charter item GUID.

### name

The name of the guild or arena team that the player is trying to ask for petitions for.

### type

The type of the petition.

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
