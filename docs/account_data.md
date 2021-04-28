# account\_data

[<-Back-to:Characters](database-characters.md)

**The \`account\_data\` table**

Contains data about client account and settings.

**Structure**

| Field        | Type       | Attributes | Key | Null | Default | Extra | Comment |
|--------------|------------|------------|-----|------|---------|-------|---------|
| [account][1] | INT(10)    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [type][2]    | TINYINT(3) | UNSIGNED   | PRI | NO   | 0       |       |         |
| [time][3]    | INT(10)    | UNSIGNED   |     | NO   | 0       |       |         |
| [data][4]    | BLOB       | SIGNED     |     | NO   |         |       |         |

[1]: #account
[2]: #type
[3]: #time
[4]: #data

**Description of the fields**

### account

[Account.id](http://www.azerothcore.org/wiki/account#id).

### type

| Value | Description                   |
|-------|-------------------------------|
| 0     | Global-account config cache   |
| 2     | Global-account bindings cache |
| 4     | Global-account macros cache   |

### time

Time of last modification in Unixtime

### data

No description can be written. You just must understand it's data.
