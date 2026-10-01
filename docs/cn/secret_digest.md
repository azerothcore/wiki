# secret\_digest

[<-返回至:Auth](database-auth)

**`secret\_digest` 表**

**表结构**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]     | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [digest][2] | VARCHAR(100) | SIGNED     |     | NO   |         |       |         |

[1]: #id
[2]: #digest

**字段说明**

### id

id 摘要。

### digest

存储的 HMAC-SHA1 摘要值，用于验证完整性。
