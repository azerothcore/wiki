# mail\_items

[<-返回至:Characters](database-characters)

**\`mail\_items\` 表**

此表包含通过电子邮件发送的、来自 item\_instance 的物品相关数据。

**表结构**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment                            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [mail_id][1]   | INT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |                                    |
| [receiver][3]  | INT  | UNSIGNED   |     | NO   | 0       |       | 角色全局唯一标识符                 |

[1]: #mailid
[2]: #itemguid
[3]: #receiver

## 字段说明

### mail\_id

物品所附着的邮件 ID。

### item\_guid

这是来自 [item\_instance.guid](item_instance#guid) 的物品的 guid。

### receiver

应接收此物品的角色 guid。
