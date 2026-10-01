# mail_server_template

[<-返回至:Characters](database-characters)

**\`mail_server_template\` 表**

此表包含要发送给满足条件的玩家的服务器邮件信息。邮件在登录时（OnLogin）发送。

与以下内容协同工作：
- [mail_server_template_items](mail_server_template_items) 用于向邮件附加物品。
- [mail_server_template_conditions](mail_server_template_conditions) 用于创建接收邮件的条件。

**表结构**

| Field                     | Type    | Attributes | Key | Null | Default | Extra          | Comment                                            |
| ------------------------- | ------- | ---------- | --- | ---- | ------- | -------------- | -------------------------------------------------- |
| [id](#id)                 | INT     | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |                                                    |
| [senderEntry](#senderentry) | INT    | UNSIGNED   |     | NO   | 0       |                | 来自 creature_template 的条目。0 = 客户支持        |
| [moneyA](#moneya)         | INT     | UNSIGNED   |     | NO   | 0       |                |                                                    |
| [moneyH](#moneyh)         | INT     | UNSIGNED   |     | NO   | 0       |                |                                                    |
| [subject](#subject)       | TEXT    |            |     | NO   |         |                |                                                    |
| [body](#body)             | TEXT    |            |     | NO   |         |                |                                                    |
| [active](#active)         | TINYINT | UNSIGNED   |     | NO   | 1       |                |                                                    |

## 字段说明

### id

唯一 ID。

### senderentry

用作邮件发件人的 [creature_template.entry](creature_template#entry)。

设置为 `0` 以继续使用默认的 **客户支持（Customer Support）** 发件人。

### moneyA

发送给联盟玩家的金币（以铜币为单位）。

### moneyH

发送给部落玩家的金币（以铜币为单位）。

### subject

邮件的标题/主题。

### body

邮件的正文。

### active

布尔值

- 1 = 邮件处于激活状态，如果玩家满足条件，将会发送给他们。
- 0 = 已禁用。
