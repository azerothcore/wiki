# account\_data

[<-Back-to:Characters](database-characters)

**The \`account\_data\` table**

Contains data about client account and settings.

**Table: account\_data's Structure**

| Field                   | Type    |          | Null | Key | Default | Extra | Comment            |
| :---------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------- |
| [accountId](#accountid) | INT     | UNSIGNED | NO   | PRI | 0       |       | Account Identifier |
| [type](#type)           | TINYINT | UNSIGNED | NO   | PRI | 0       |       |                    |
| [time](#time)           | INT     | UNSIGNED | NO   |     | 0       |       |                    |
| [data](#data)           | BLOB    |          | NO   |     |         |       |                    |

**Description of the table's fields**

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

The data itself, as the client sent it. What it contains depends on [type](#type).
