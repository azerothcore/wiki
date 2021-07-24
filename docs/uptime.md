# uptime

[<-Back-to:Auth](database-auth.md)

**The \`uptime\` table**

This table holds the server's uptime. The core will automatically update the latest entry's value until it crashes and a new record is added.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default     | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ----------- | ----- | ------- |
| [realmid][1]    | INT          | UNSIGNED   | PRI | NO   |             |       |         |
| [starttime][2]  | INT          | UNSIGNED   | PRI | NO   | 0           |       |         |
| [uptime][3]     | INT          | UNSIGNED   |     | NO   | 0           |       |         |
| [maxplayers][4] | SMALLINT     | UNSIGNED   |     | NO   | 0           |       |         |
| [revision][5]   | VARCHAR(255) | SIGNED     |     | NO   | AzerothCore |       |         |

[1]: #realmid
[2]: #starttime
[3]: #uptime
[4]: #maxplayers
[5]: #revision

**Description of the fields**

### realmid

The ID of the realm. See [realmlist.id](realmlist#id).

### starttime

The time when the server was started, in Unix time.

### uptime

The uptime of the server, in seconds.

### maxplayers

The maximum number of players connected.

### revision

The detailed revision of the worldserver.
