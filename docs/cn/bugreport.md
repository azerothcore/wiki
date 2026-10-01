# bugreport

[<-返回至:Characters](database-characters)

**\`bugreport\` 表**

**表结构**

| Field                  | Type     | Attributes | Key | Null | Default | Extra          | Comment    |
| ---------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ---------- |
| [id](#id)              | INT      | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT | 标识符     |
| [type](#type)          | LONGTEXT | SIGNED     |     | NO   |         |                |            |
| [content](#conent)     | LONGTEXT | SIGNED     |     | NO   |         |                |            |
| [State](#state)        | TINYINT  | SIGNED     |     | NO   | 1       |                |            |
| [Assignee](#assignee)  | VARCHAR(255) |        |     | YES  | NULL    |                |            |
| [Comment](#comment)    | LONGTEXT |            |     | YES  | NULL    |                |            |

**字段说明**

### id

`field-no-description|1`

### type

`field-no-description|2`

### content

`field-no-description|3`

### State

`field-no-description|4`

### Assignee

`field-no-description|5`

### Comment

`field-no-description|6`
