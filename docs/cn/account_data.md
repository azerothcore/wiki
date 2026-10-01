# account\_data

[<-返回至:Characters](database-characters)

**`account\_data` 表**

包含有关客户端账号和设置的数据。

**表结构**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment            |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [accountId][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       | 账号标识符         |
| [type][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |                    |
| [time][3]      | INT     | UNSIGNED   |     | NO   | 0       |       |                    |
| [data][4]      | BLOB    | SIGNED     |     | NO   |         |       |                    |

[1]: #accountid
[2]: #type
[3]: #time
[4]: #data

**字段说明**

### accountId

[account.id](account#id)。

### type

| 值    | 描述                    |
| ----- | ----------------------- |
| 0     | 全局账号配置缓存        |
| 2     | 全局账号按键绑定缓存    |
| 4     | 全局账号宏缓存          |

### time

最后一次修改的时间，以 Unix 时间表示。

### data

无法给出描述。你只需明白它是一份数据即可。
