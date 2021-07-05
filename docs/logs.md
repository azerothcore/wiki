# logs

[<-Back-to:Auth](database-auth.md)

**The \`logs\` table**

This table stores logs from `Appender` type database in config file.
Example db appender:
```ini
Appender.DB=3,5,0
```

**Structure**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------|--------------|------------|-----|------|---------|-------|---------|
| [time][1]   | INT          | UNSIGNED   |     | NO   |         |       |         |
| [realm][2]  | INT          | UNSIGNED   |     | NO   |         |       |         |
| [type][3]   | VARCHAR(250) |            |     | NO   |         |       |         |
| [level][4]  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [string][5] | TEXT         |            |     | YES  |         |       |         |

[1]: #time
[2]: #realm
[3]: #type
[4]: #level
[5]: #string

**Description of the fields**

### time

A unixtime timestamp indicating when this string was logged.

### realm

The [RealmID](realmlist#id) of the realm this log string came from. 0 if realmd.

### type

The `Logger` name from config
Example logger:
```ini
Logger.server=4,Console Server
```

### level

Depends on LogLevel in authserver.conf

| Value | Description |
|-------|-------------|
| 1     | (Fatal)     |
| 2     | (Error)     |
| 3     | (Warning)   |
| 4     | (Info)      |
| 5     | (Debug)     |
| 6     | (Trace)     |

### string

The actual string that has been logged.
