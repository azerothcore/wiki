# mail_server_character

[<-返回至:Characters](database-characters)

**\`mail_server_character\` 表**

此表保存哪些玩家已收到过服务器邮件的记录。这可以防止同一封邮件被重复发送给同一个玩家。

注意：当 [mail_server_template.id](mail_server_template#id) 中被引用的条目被删除时，此表中的条目将自动删除。约束 CONSTRAINT `fk_mail_server_character`

**表结构**

| Field       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [mailId][2] | INT  | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #guid
[2]: #mailId

## 字段说明

### guid

[characters.guid](characters#guid)。

### mailId

[mail_server_template.id](mail_server_template#id)。
