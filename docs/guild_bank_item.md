# guild\_bank\_item

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_item\` table**

This table holds all item information for items that are stored in the guild bank.

**Table Structure**

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

**Description of the fields**

### guildid

The guild ID who owns the bank. See [guild.guildid](guild#guildid).

### TabId

The tab ID where the item is currently placed in. See [guild\_bank\_tab.TabId](guild_bank_tab#tabid).

### SlotId

The slot that the item is placed in in the tab.

### item\_guid

The item guid. See [item\_instance.guid](item_instance#guid).
