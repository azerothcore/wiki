# warden\_checks

[<-返回至:World](database-world)

**\`warden\_checks\` 表**

该表包含与反作弊工具 Warden 使用相关的数据，Warden 可以通过 Worldserver.conf 启用。

**表结构**

| Field                             | Type        | Attributes | Key | NULL | Default         | Comment                                   |
| --------------------------------- | ----------- | ---------- | --- | ---- | --------------- | ----------------------------------------- |
| [id](#id)                         | SMALLINT    | UNSIGNED   | PRI | NO   | auto\_increment | 唯一 ID，自动递增 1                          |
| [type](#type)                     | TINYINT     | UNSIGNED   |     | YES  | NULL            |                                           |
| [data](#data)                     | VARCHAR(48) |            |     | YES  | NULL            |                                           |
| [str](#str)                       | VARCHAR(20) |            |     | YES  | NULL            |                                           |
| [address](#address)               | INT         | UNSIGNED   |     | YES  | NULL            |                                           |
| [length](#length)                 | TINYINT     | UNSIGNED   |     | YES  | NULL            |                                           |
| [result](#result)                 | VARCHAR(24) |            |     | YES  | NULL            |                                           |
| [comment](#comment)               | VARCHAR(50) |            |     | YES  | NULL            |                                           |

**字段说明：**

### id

唯一 ID，自动递增 1

### type

`field-no-description|2`

### data

`field-no-description|3`

### str

`field-no-description|4`

### address

`field-no-description|5`

### length

`field-no-description|6`

### result

`field-no-description|7`

### comment

`field-no-description|8`
