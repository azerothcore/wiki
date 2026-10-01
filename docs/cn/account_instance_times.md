# account\_instance\_times

[<-返回至:Characters](database-characters)

**`account\_instance\_times` 表**

此表控制该账号的角色在过去 1 小时内已进入多少个副本实例。如果每个账号有 5 条记录，玩家将无法进入另一个副本。

**表结构**

| Field            | Type   | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [accountId][1]   | INT    | UNSIGNED   | PRI | NO   |         |       |         |
| [instanceId][2]  | INT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [releaseTime][3] | BIGINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #accountid
[2]: #instanceid
[3]: #releasetime

**字段说明**

### accountId

玩家的账号。参见 [account.id](account#id)。

### instanceId

该账号的角色在过去 5 小时内（原文如此）进入过的副本实例 ID。

### releaseTime

允许再次进入这些副本实例的时间，以 Unix 时间表示。
