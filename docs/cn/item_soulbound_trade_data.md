# item\_soulbound\_trade\_data

[<-返回至:Characters](database-characters)

**\`item\_soulbound\_trade\_data\` 表**

此表存储关于哪些玩家可以在彼此之间交易灵魂绑定物品的信息。

**表结构**

| Field              | Type | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| ------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [itemGuid][1]      | INT  | UNSIGNED   | PRI | NO   |         |       | 物品 GUID                                                               |
| [allowedPlayers][2] | TEXT |            |     | NO   |         |       | 空格分隔的、可在交易中接收此物品的玩家 GUID 列表                           |

[1]: #itemguid
[2]: #allowedplayers

**字段说明**

### itemGuid

可以交易的物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### allowedPlayers

有资格进行交易的玩家的 GUID 列表，以空格分隔。参见 [characters.guid](characters#guid)。
