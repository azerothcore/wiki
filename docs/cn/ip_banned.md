# ip\_banned

[<-返回至:Auth](database-auth)

**`ip\_banned` 表**

此表包含所有被禁用的 IP 以及封禁到期（或是否到期）的日期。

**表结构**

| Field          | Type         | Attributes | Key | Null | Default   | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | --------- | ----- | ------- |
| [ip][1]        | VARCHAR(15)  | SIGNED     | PRI | NO   | 127.0.0.1 |       |         |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   |           |       |         |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   |           |       |         |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   | [Console] |       |         |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   | no reason |       |         |

[1]: #ip
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason

**字段说明**

### ip

被封禁的 IP 地址。

### bandate

该 IP 首次被封禁的日期，以 Unix 时间表示。

### unbandate

该 IP 将被解禁的日期，以 Unix 时间表示。任何设置低于当前日期的日期基本上都视为永久封禁，因为它永远不会自动过期。

### bannedby

封禁该 IP 的角色名称。该角色应属于一个拥有游戏内 .ban 命令权限的账号。

### banreason

对该 IP 封禁给出的原因。
