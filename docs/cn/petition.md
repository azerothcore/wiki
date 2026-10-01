# petition

[<-返回至:Characters](database-characters)

**`petition` 表**

该表保存公会或竞技场队伍所有进行中的申请的信息。

**表结构**

| Field             | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ownerguid][1]    | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [petitionguid][2] | INT         | UNSIGNED   |     | YES  | 0       |       |         |
| [petition_id][5]  | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [name][3]         | VARCHAR(24) | SIGNED     |     | NO   |         |       |         |
| [type][4]         | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #name
[4]: #type
[5]: #petitionid

## 字段说明

### ownerguid

申请所有者的 GUID。参见 [characters.guid](characters#guid)。

### petitionguid

申请物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### petition_id

申请的序号标识符，每个申请唯一。用于独立于契约物品 GUID 引用该申请。

### name

玩家试图为其征询申请的工会或竞技场队伍的名称。

### type

申请的类型。

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |
