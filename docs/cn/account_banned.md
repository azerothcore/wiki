# account\_banned

[<-返回至:Auth](database-auth)

**`account\_banned` 表**

此表列出了所有被禁封的账号，以及封禁到期（或是否到期）的日期。

**表结构**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment    |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       | 账号 ID    |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |            |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |            |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |            |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |            |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |            |

[1]: #id
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**字段说明**

### id

账号 ID。参见 [account.id](account#id)。

### bandate

账号被禁封的日期，以 Unix 时间表示。

### unbandate

账号将被自动解封的日期，以 Unix 时间表示。如果该值小于当前日期，实际上就相当于永久封禁。

### bannedby

禁封该账号的 GM 角色名。如果是从控制台禁封的，则该字段为空（直到改进）。

### banreason

封禁的原因。

### active

布尔值 0 或 1，控制封禁当前是否处于生效状态。
