# logs

[<-返回:Auth](database-auth)

**\`logs\` 表**

该表存储来自配置文件中 `Appender` 类型数据库的日志。
数据库附加器示例：

```ini
Appender.DB=3,5,0
```

**表结构**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [time][1]   | INT          | UNSIGNED   |     | NO   |         |       |         |
| [realm][2]  | INT          | UNSIGNED   |     | NO   |         |       |         |
| [type][3]   | VARCHAR(250) | SIGNED     |     | NO   |         |       |         |
| [level][4]  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [string][5] | TEXT         | SIGNED     |     | YES  |         |       |         |

[1]: #time
[2]: #realm
[3]: #type
[4]: #level
[5]: #string

**字段说明**

### time

指示该字符串记录时间的 unixtime 时间戳。

### realm

该日志字符串来源领域的 [RealmID](realmlist#id)。如果是 realmd，则为 0。

### type

来自配置的 `Logger` 名称
记录器示例：
```ini
Logger.server=4,Console Server
```

### level

取决于 authserver.conf 中的 LogLevel

| 值    | 描述       |
| ----- | ----------- |
| 1     | (Fatal)     |
| 2     | (Error)     |
| 3     | (Warning)   |
| 4     | (Info)      |
| 5     | (Debug)     |
| 6     | (Trace)     |

### string

已记录的实际字符串。
