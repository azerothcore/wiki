# updates_include

[<-返回:Auth](database-auth)
[<-返回:Characters](database-characters)
[<-返回:World](database-world)

**\`updates_include\` 表**

`table-no-description`

**表结构**

| Field      | Type         | Attributes               | Key | Null | Default  | Extra | Comment                                                           |
| ---------- | ------------ | ------------------------ | --- | ---- | -------- | ----- | ----------------------------------------------------------------- |
| [path][1]  | VARCHAR(200) |                          | PRI | NO   |          |       | 要包含的目录。$ 表示相对于源目录。                                |
| [state][2] | ENUM         | RELEASED,CUSTOM,ARCHIVED |     | NO   | RELEASED |       | 定义该目录包含的是 released 还是 archived 更新。                 |

[1]: #path
[2]: #state

## 字段描述

### path

要包含到更新中的目录。

$ 表示相对于源目录。

### state

定义该目录包含的是 released、custom 还是 archived 更新。
