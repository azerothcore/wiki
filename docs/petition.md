# petition

[<-Back-to:Characters](database-characters.md)

**The \`petition\` table**

This table holds information on all ongoing petitions for a guild or for an arena team.

**Structure**

| Field             | Type        | Attributes | Key | Null | Default | Extra | Comment |
|-------------------|-------------|------------|-----|------|---------|-------|---------|
| [ownerguid][1]    | int(10)     | unsigned   | PRI | NO   |         |       |         |
| [petitionguid][2] | int(10)     | unsigned   |     | YES  | 0       |       |         |
| [name][3]         | varchar(24) | signed     |     | NO   |         |       |         |
| [type][4]         | tinyint(3)  | unsigned   | PRI | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #name
[4]: #type

**Description of the fields**

### ownerguid

The petition's owner's GUID. See characters.guid

### petitionguid

The GUID of the petition item. See item\_instance.guid

### name

The name of the guild or arena team that the player is trying to ask for petitions for.

### type

The type of the petition.

| ID | Type               |
|----|--------------------|
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
