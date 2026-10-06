# logs

[<-Back-to:Auth](database-auth)

**The \`logs\` table**

This table stores logs from `Appender` type database in config file.
Example db appender:

```ini
Appender.DB=3,5,0
```

**Table: logs's Structure**

| Field             | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [time](#time)     | INT          | UNSIGNED | NO   |     |         |       |         |
| [realm](#realm)   | INT          | UNSIGNED | NO   |     |         |       |         |
| [type](#type)     | VARCHAR(250) |          | NO   |     |         |       |         |
| [level](#level)   | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [string](#string) | TEXT         |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
| ----- | ----------- |
| 1     | (Fatal)     |
| 2     | (Error)     |
| 3     | (Warning)   |
| 4     | (Info)      |
| 5     | (Debug)     |
| 6     | (Trace)     |

### string

The actual string that has been logged.
