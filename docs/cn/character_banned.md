# character\_banned

[<-返回:Characters](database-characters)

**\`character\_banned\` 表**

该表列出了所有已被封禁的角色，以及封禁到期（或是否到期）的日期。

**表结构**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]      | INT          | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |                          |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |                          |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### bandate

角色被封禁的日期，使用 Unix 时间表示。

### unbandate

角色将被自动解除封禁的日期，使用 Unix 时间表示。若该值小于当前日期，则实际上表示永久封禁。

### bannedby

拥有 .ban 命令权限并封禁该角色的角色。

### banreason

封禁的原因。

### active

布尔值 0 或 1，控制该封禁当前是否生效。
