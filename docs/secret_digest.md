# secret\_digest

[<-Back-to:Auth](database-auth)

**The \`secret\_digest\` table**

**Table: secret\_digest's Structure**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]     | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [digest][2] | VARCHAR(100) |            |     | NO   |         |       |         |

[1]: #id
[2]: #digest

**Description of the table's fields**

### id

The id digest.

### digest

The stored HMAC-SHA1 digest value used to verify integrity.
