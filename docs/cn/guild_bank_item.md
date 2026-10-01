# guild\_bank\_item

[<-返回至:Characters](database-characters)

**\`guild\_bank\_item\` 表**

此表保存了存储在公会银行中的所有物品信息。

**表结构**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]   | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]     | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SlotId][3]    | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [item_guid][4] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #slotid
[4]: #itemguid

**字段说明**

### guildid

拥有该银行的公会的 ID。参见 [guild.guildid](guild#guildid)。

### TabId

物品当前所在的标签页 ID。参见 [guild\_bank\_tab.TabId](guild_bank_tab#tabid)。

### SlotId

物品在标签页中所放置的槽位。

### item\_guid

物品的 guid。参见 [item\_instance.guid](item_instance#guid)。
