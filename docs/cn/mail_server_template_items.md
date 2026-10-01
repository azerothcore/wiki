# mail_server_template_items

[<-返回至:Characters](database-characters)

**\`mail_server_template_items\` 表**

与 [mail_server_template](mail_server_template) 协同工作。

注意：当 [mail_server_template.id](mail_server_template#id) 中被引用的条目被删除时，此表中的条目将自动删除。约束 CONSTRAINT `fk_mail_template`

**表结构**

| Field                     | Type | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                 | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templateID](#templateid) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [faction](#moneyh)        | ENUM |            |     | NO   |         |                |         |
| [item](#item)             | INT  | UNSIGNED   |     | NO   |         |                |         |
| [itemCount](#itemcount)   | INT  | UNSIGNED   |     | NO   |         |                |         |

## 字段说明

### id

唯一 ID。

### templateID

[mail_server_template.id](mail_server_template#id)。

### faction

- 联盟（Alliance）
- 部落（Horde）

### item

物品 entry。参见 [item_template.entry](item_template#entry)。

### itemCount

要发送的副本数量。
