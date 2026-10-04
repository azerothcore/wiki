# uptime

[<-Back-to:Auth](database-auth)

**The \`uptime\` table**

This table holds the server's uptime. The core will automatically update the latest entry's value until it crashes and a new record is added.

**Table: uptime's Structure**

| Field                             | Type         |          | Null | Key | Default     | Extra | Comment                                           |
| :-------------------------------- | :----------- | :------- | :--: | :-: | :---------: | :---: | :------------------------------------------------ |
| [realmid](#realmid)               | INT          | UNSIGNED | NO   | PRI |             |       |                                                   |
| [starttime](#starttime)           | INT          | UNSIGNED | NO   | PRI | 0           |       |                                                   |
| [uptime](#uptime)                 | INT          | UNSIGNED | NO   |     | 0           |       |                                                   |
| [EndTime](#endtime)               | INT          | UNSIGNED | YES  |     | NULL        |       |                                                   |
| [maxplayers](#maxplayers)         | SMALLINT     | UNSIGNED | NO   |     | 0           |       |                                                   |
| [revision](#revision)             | VARCHAR(255) |          | NO   |     | AzerothCore |       |                                                   |
| [ShutdownType](#shutdowntype)     | TINYINT      | UNSIGNED | NO   |     | 0           |       | 0 = unknown, 1 = shutdown, 2 = restart, 3 = error |
| [ExitCode](#exitcode)             | TINYINT      | UNSIGNED | YES  |     | NULL        |       |                                                   |
| [ShutdownReason](#shutdownreason) | VARCHAR(255) |          | NO   |     | ''          |       |                                                   |

**Description of the table's fields**

### realmid

The ID of the realm. See [realmlist.id](realmlist#id).

### starttime

The time when the server was started, in Unix time.

### uptime

The uptime of the server, in seconds.

### EndTime

The time the server shut down, in Unix time. NULL while the server is running, or if it crashed. The `.server info` command uses this to show whether the last session crashed.

### maxplayers

The maximum number of players connected.

### revision

The detailed revision of the worldserver.

### ShutdownType

| Value | Type     |
| ----- | -------- |
| 0     | Unknown  |
| 1     | Shutdown |
| 2     | Restart  |
| 3     | Error    |

### ExitCode

The exit code of the worldserver: 0 for a shutdown, 1 for an error and 2 for a restart. NULL if the server did not shut down cleanly.

### ShutdownReason

The reason given for the shutdown or restart, for example with `.server shutdown`.
