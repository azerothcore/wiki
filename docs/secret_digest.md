# secret\_digest

[<-Back-to:Auth](database-auth)

**The \`secret\_digest\` table**

Stores a digest of each server secret, such as the TOTP master secret, so the core can detect when the configured secret has changed.

**Table: secret\_digest's Structure**

| Field             | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)         | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [digest](#digest) | VARCHAR(100) |          | NO   |     |         |       |         |

**Description of the table's fields**

### id

The id digest.

### digest

The stored HMAC-SHA1 digest value used to verify integrity.
