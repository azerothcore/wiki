# item\_refund\_instance

[<-返回至:Characters](database-characters)

**\`item\_refund\_instance\` 表**

此表作为游戏内 2 小时时间窗口内可退款购买的凭证。它保存了购买该物品时花费了哪种货币的信息。

**表结构**

| Field                 | Type     | Attributes | Key | Null | Default | Extra | Comment     |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ----------- |
| [item_guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |       | 物品 GUID   |
| [player_guid][2]      | INT      | UNSIGNED   | PRI | NO   |         |       | 玩家 GUID |
| [paidMoney][3]        | INT      | UNSIGNED   |     | NO   | 0       |       |             |
| [paidExtendedCost][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |             |

[1]: #itemguid
[2]: #playerguid
[3]: #paidmoney
[4]: #paidextendedcost

**字段说明**

### item\_guid

从商人处购买的物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### player\_guid

有资格获得退款的玩家的 GUID。参见 [characters.guid](characters#guid)。

### paidMoney

为该物品支付的金钱数额（以铜币为单位）。

### paidExtendedCost

为该物品支付的 ItemExtendedCost.dbc ID。
