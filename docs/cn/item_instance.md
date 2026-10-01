# item\_instance

[<-返回至:Characters](database-characters)

**`item\_instance` 表**

此表保存了当前装备在某种角色背包或银行中、在拍卖行中、在公会银行中或在邮件中的所有物品的单个物品实例信息。

**表结构**

| Field                  | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [itemEntry][2]         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [owner_guid][3]        | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [creatorGuid][4]       | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [giftCreatorGuid][5]   | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [count][6]             | INT       | UNSIGNED   |     | NO   | 1       |       |         |
| [duration][7]          | INT       | SIGNED     |     | NO   | 0       |       |         |
| [charges][8]           | TINYTEXT  | SIGNED     |     | YES  |         |       |         |
| [flags][9]             | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [enchantments][10]     | TEXT      | SIGNED     |     | NO   |         |       |         |
| [randomPropertyId][11] | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [durability][12]       | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [playedTime][13]       | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [text][14]             | TEXT      | SIGNED     |     | YES  |         |       |         |

[1]: #guid
[2]: #itementry
[3]: #ownerguid
[4]: #creatorguid
[5]: #giftcreatorguid
[6]: #count
[7]: #duration
[8]: #charges
[9]: #flags
[10]: #enchantments
[11]: #randompropertyid
[12]: #durability
[13]: #playedtime
[14]: #text

**字段说明**

### guid

物品的 GUID。此编号对每个物品实例都是唯一的。

### itemEntry

[Item_template.entry](item_template#entry)。

### owner\_guid

拥有此物品的角色的 GUID。参见 [characters.guid](characters#guid)。

### creatorGuid

创建该物品的角色的 [Characters.guid](characters#guid)。

### giftCreatorGuid

创建了该[物品](character_gifts#itemguid)的角色的 [Characters.guid](characters#guid)。

### count

当前堆叠中的物品副本数量。

### duration

`field-no-description|6`

### charges

物品上五种可能法术充能各自的数量，通过五个以空格分隔的整数指定。

### flags

`field-no-description|8`

### enchantments

来自 SpellItemEnchantment.dbc 的附魔，参见：[item_instance_enchantments](item_instance_enchantments)

### randomPropertyId

`field-no-description|10`

### durability

当前物品耐久度。

### playedTime

以秒为单位的时间。

### text

该特定物品中包含的文本。
