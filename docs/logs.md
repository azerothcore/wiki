# logs

[<-Back-to:Auth](database-auth.md)

**The \`logs\` table**

This table stores all logs from authserver if database logging in config is enabled.

**Structure**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------|--------------|------------|-----|------|---------|-------|---------|
| [time][1]   | int(10)      | unsigned   |     | NO   |         |       |         |
| [realm][2]  | int(10)      | unsigned   |     | NO   |         |       |         |
| [type][3]   | VARCHAR(250) |            |     | NO   |         |       |         |
| [level][4]  | tinyint(3)   | unsigned   |     | NO   | 0       |       |         |
| [string][5] | text         |            |     | YES  |         |       |         |

[1]: #time
[2]: #realm
[3]: #type
[4]: #level
[5]: #string

**Description of the fields**

### time

A unixtime TIMESTAMP indicating when this string was logged.

### realm

The [RealmID](realmlist#id) of the realm this log string came from. 0 if realmd.

### type

The type of log this is:

| Name            | Value | Description                 |
|-----------------|-------|-----------------------------|
| LOG_TYPE_STRING | 0     | A NORMAL INFORMATIVE STRING |
| LOG_TYPE_ERROR  | 1     | SOME SORT OF ERROR          |
| LOG_TYPE_BASIC  | 2     | BASIC INFORMATION           |
| LOG_TYPE_DETAIL | 3     | DETAILED INFORMATION        |
| LOG_TYPE_DEBUG  | 4     | DEBUGGING INFORMATION       |
| LOG_TYPE_CHAR   | 5     | CHARACTER-RELATED           |
| LOG_TYPE_WORLD  | 6     | WORLD PACKET DUMP           |
| LOG_TYPE_RA     | 7     | REMOTE ACCESS LOGS          |
| LOG_TYPE_GM     | 8     | GM COMMAND LOGS             |
| LOG_TYPE_CRASH  | 9     | CRASH ALARM LOGS            |
| LOG_TYPE_CHAT   | 10    | CHAT/MESSAGE LOGS           |

### level

Depends on LogLevel in authserver.conf

| Value | Description |
|-------|-------------|
| 1     | (Trace)     |
| 2     | (Debug)     |
| 3     | (Info)      |
| 4     | (Warn)      |
| 5     | (Error)     |
| 6     | (Fatal)     |

### string

The actual string that has been logged.
