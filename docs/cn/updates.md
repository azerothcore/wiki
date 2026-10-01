# updates

[<-返回:Auth](database-auth)
[<-返回:Characters](database-characters)
[<-返回:World](database-world)

**\`updates\` 表**

`table-no-description`

**表结构**

| Field          | Type         | Attributes               | Key | Null | Default           | Extra | Comment                                                       |
| -------------- | ------------ | ------------------------ | --- | ---- | ----------------- | ----- | ------------------------------------------------------------- |
| [name][1]      | VARCHAR(200) |                          | PRI | NO   |                   |       | 更新文件的文件名（含扩展名）。                                |
| [hash][2]      | CHAR(40)     |                          |     | YES  | ''                |       | sql 文件的 SHA1 哈希。                                        |
| [state][3]     | ENUM         | RELEASED,CUSTOM,ARCHIVED |     | NO   | RELEASED          |       | 定义更新是 released、custom 还是 archived。                   |
| [timestamp][4] | TIMESTAMP    |                          |     | NO   | CURRENT_TIMESTAMP |       | 应用该查询时的时间戳。                                        |
| [speed][5]     | INT          | UNSIGNED                 |     | NO   | 0                 |       | 应用该查询所需的时间（毫秒）。                                |

[1]: #name
[2]: #hash
[3]: #state
[4]: #timestamp
[5]: #speed


## 字段描述

### name

导入文件的文件名。

### hash

导入文件的 SHA1 哈希。

### state

定义更新是 released、custom 还是 archived。

### timestamp

导入该文件的时间。

### speed

导入该文件所需的时间（毫秒）。
