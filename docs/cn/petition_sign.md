# petition\_sign

[<-返回至:Characters](database-characters)

**`petition_sign` 表**

该表保存公会或竞技场队伍申请的所有签名的信息。

**表结构**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ownerguid][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [petitionguid][2]   | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [petition_id][6]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [playerguid][3]     | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [player_account][4] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #playerguid
[4]: #playeraccount
[5]: #type
[6]: #petitionid

## 字段说明

### ownerguid

试图创建公会/竞技场队伍的申请所有者的 GUID。参见 [characters.guid](characters#guid)。

### petitionguid

契约物品的 GUID。参见 [item\_template.guid](item_template#guid)。

### petition_id

被签名的申请的序号标识符。与 [petition.petition_id](petition#petitionid) 匹配。

### playerguid

已签署契约的玩家的 GUID。参见 [characters.guid](characters#guid)。

### player\_account

已签署契约的玩家的账号 ID。同一账号下不能有两名玩家签署同一契约。

### type

申请的类型。

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
