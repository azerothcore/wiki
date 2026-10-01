# realmcharacters

[<-返回至:Auth](database-auth)

**`realmcharacters` 表**

此表保存每个账号在每个服务器上拥有的角色数量的信息。
该表中的数据由核心（core）维护。

**表结构**

| Field         | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1]  | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [acctid][2]   | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [numchars][3] | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #realmid
[2]: #acctid
[3]: #numchars

**字段说明**

### realmid

服务器的 ID。参见 [realmlist.id](realmlist#id)。

### acctid

账号 ID。参见 [account.id](account#id)。

### numchars

该账号在此服务器上拥有的角色数量。
