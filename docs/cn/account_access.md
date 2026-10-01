# account\_access

[<-返回至:Auth](database-auth)

**`account\_access` 表**

此表保存 [realmlist](realmlist) 表中任何领域的（服务器）安全访问级别。

**表结构**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]      | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [gmlevel][2] | TINYINT      | UNSIGNED   |     | NO   |         |       |         |
| [RealmID][3] | INT          | SIGNED     | PRI | NO   | -1      |       |         |
| [comment][4] | VARCHAR(255) | SIGNED     |     | YES  | ''      |       |         |

[1]: #id
[2]: #gmlevel
[3]: #realmid
[4]: #comment

**字段说明**

### id

[账号 ID](account#id)。

### gmlevel

账号安全级别。不同的级别可以访问不同的命令。单个命令所需的具体级别在每个领域的 [command](command) 表中定义。

### RealmID

[领域 ID](realmlist#id)。

### comment

暂无描述。
