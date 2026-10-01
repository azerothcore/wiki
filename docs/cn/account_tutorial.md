# account\_tutorial

[<-返回至:Characters](database-characters)

**`account\_tutorial` 表**

此表用于存储所有账号的新手引导（tutorial）状态。

**表结构**

| Field          | Type | Attributes | Key | Null | Default | Extra  | Comment            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ------ | ------------------ |
| [accountId][1] | INT  | UNSIGNED   | PRI | NO   | 0       | Unique | 账号标识符         |
| [tut0][2]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut1][3]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut2][4]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut3][5]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut4][6]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut5][7]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut6][8]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut7][9]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |

[1]: #accountid
[2]: #tut0
[3]: #tut1
[4]: #tut2
[5]: #tut3
[6]: #tut4
[7]: #tut5
[8]: #tut6
[9]: #tut7

**字段说明**

### guid

玩家的账号。参见 [account.id](account#id)。

### tut0

`field-no-description|2`

### tut1

`field-no-description|3`

### tut2

`field-no-description|4`

### tut3

`field-no-description|5`

### tut4

`field-no-description|6`

### tut5

`field-no-description|7`

### tut6

`field-no-description|8`

### tut7

这些值是 32 位标志。因此 8 个 32 位值共提供 256 位，用于存储 256 条新手引导消息的状态。

每一位的含义如下：

- 0 - 尚未显示
- 1 - 已显示

这用于只显示角色之前没有见过的新手引导消息。

在游戏中取消勾选"显示新手引导"选项后，所有位都会被置为 1，因此在更改该选项后，所有 tutX 列都将包含二进制的 11111111111111111111111111111111，即十进制的 4294967295。
