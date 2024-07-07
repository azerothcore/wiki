# account\_data

[<-Back-to:Characters](database-characters)

**The \`account\_data\` table**

Contains data about client account and settings.

**Table Structure**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment            |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [accountId][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       | Account Identifier |
| [type][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |                    |
| [time][3]      | INT     | UNSIGNED   |     | NO   | 0       |       |                    |
| [data][4]      | BLOB    | SIGNED     |     | NO   |         |       |                    |

[1]: #accountid
[2]: #type
[3]: #time
[4]: #data

**Description of the fields**

### accountId

The [account.id](account#id).

### type

| Value | Description                   |
| ----- | ----------------------------- |
| 0     | Global-account config cache   |
| 2     | Global-account bindings cache |
| 4     | Global-account macros cache   |

### time

Time of last modification in Unixtime.

### data

No description can be written. You just must understand it's data.
