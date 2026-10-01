# motd

[<-返回至:Auth](database-auth)

**\`motd\` 表**

**表结构**

| Field        | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT      | SIGNED     | PRI | NO   |         |       |         |
| [text][2]    | LONGTEXT |            |     | YES  | NULL    |       |         |


[1]: #realmid
[2]: #text

## 字段说明

### realmid

要发送的服务器公告（Motd）所对应的 RealmID

-1 表示所有服务器（全部领域）

指定特定领域优先于 -1（所有领域）

### text

服务器公告（Motd）的文本内容
