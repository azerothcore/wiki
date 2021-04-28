# guild\_bank\_item

[<-Back-to:Characters](database-characters.md)

**The \`guild\_bank\_item\` table**

This table holds all item information for items that are stored in the guild bank.

**Structure**

| Field          | Type       | Attributes | Key | Null | Default | Extra | Comment |
|----------------|------------|------------|-----|------|---------|-------|---------|
| [guildid][1]   | INT(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [TabId][2]     | TINYINT(3) | unsigned   | PRI | NO   | 0       |       |         |
| [SlotId][3]    | TINYINT(3) | unsigned   | PRI | NO   | 0       |       |         |
| [item_guid][4] | INT(10)    | unsigned   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #slotid
[4]: #item_guid

**Description of the fields**

### guildid

The guild ID who owns the bank. See [guild.guildid](guild_2130175.html#guild-guildid)

### TabId

The tab ID where the item is currently placed in. See guild\_bank\_tab.TabId

### SlotId

The slot that the item is placed in in the tab.

### item\_guid

The item guid. See  [item\_instance.guid](Item+instance+tc2#Iteminstancetc2-guid)
