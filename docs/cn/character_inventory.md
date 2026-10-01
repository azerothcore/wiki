# character\_inventory

[<-返回:Characters](database-characters)

**\`character\_inventory\` 表**

包含所有角色的背包（inventory）数据，包括银行数据。

**表结构**

| Field     | Type    | Attributes | Key    | Null | Default | Extra | Comment                       |
| --------- | ------- | ---------- | ------ | ---- | ------- | ----- | ----------------------------- |
| [guid][1] | INT     | UNSIGNED   | Unique | NO   | 0       |       | Global Unique Identifier      |
| [bag][2]  | INT     | UNSIGNED   |        | NO   | 0       |       |                               |
| [slot][3] | TINYINT | UNSIGNED   |        | NO   | 0       |       |                               |
| [item][4] | INT     | UNSIGNED   | PRI    | NO   | 0       |       | Item Global Unique Identifier |

[1]: #guid
[2]: #bag
[3]: #slot
[4]: #item

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### bag

如果不为 0，则表示背包的物品 GUID。参见 [item\_instance.guid](item_instance#guid)。

### slot

如果 bag 字段非零，则 slot 表示物品在背包中的存放槽位。取值范围可能因背包的槽位数而异。

如果 bag 字段为零，则 slot 的取值范围为 0 到 130，其值含义如下：

| 槽位    | 含义                                  |
| ------- | -------------------------------------- |
| 0       | 头部                                   |
| 1       | 颈部                                   |
| 2       | 肩部                                   |
| 3       | 衬衣                                   |
| 4       | 胸甲                                   |
| 5       | 腰部                                   |
| 6       | 腿部                                   |
| 7       | 脚部                                   |
| 8       | 手腕                                   |
| 9       | 手部                                   |
| 10      | 戒指 1                                 |
| 11      | 戒指 2                                 |
| 12      | 饰品 1                                 |
| 13      | 饰品 2                                 |
| 14      | 背部                                   |
| 15      | 主手                                   |
| 16      | 副手                                   |
| 17      | 远程武器                               |
| 18      | 战袍                                   |
| 19-22   | 已装备的背包                           |
| 23-38   | 主背包                                 |
| 39-66   | 主银行                                 |
| 67-73   | 银行背包                               |
| 86-117  | 钥匙链中的钥匙                         |
| 118-135 | 货币（徽章、奖章、印记等）             |

### item

物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。
