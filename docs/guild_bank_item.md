# guild\_bank\_item

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_item\` table**

This table holds all item information for items that are stored in the guild bank.

**Table: guild\_bank\_item's Structure**

| Field                  | Type    |          | Null | Key | Default | Extra | Comment |
| :--------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guildid](#guildid)    | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [TabId](#tabid)        | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [SlotId](#slotid)      | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [item_guid](#itemguid) | INT     | UNSIGNED | NO   | MUL | 0       |       |         |

**Description of the table's fields**

### guildid

The guild ID who owns the bank. See [guild.guildid](guild#guildid).

### TabId

The tab ID where the item is currently placed in. See [guild\_bank\_tab.TabId](guild_bank_tab#tabid).

### SlotId

The slot that the item is placed in in the tab.

### item\_guid

The item guid. See [item\_instance.guid](item_instance#guid).
