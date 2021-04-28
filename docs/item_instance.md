# item\_instance

[<-Back-to:Characters](database-characters.md)

**The \`item\_instance\` table**

This table holds individual item instance information for all items currently equipped in some kind of character bag or bank, in auctionhouses, in guild banks or in mails.

**Structure**

| Field                  | Type         | Attributes | Key | Null | Default | Extra | Comment |
|------------------------|--------------|------------|-----|------|---------|-------|---------|
| [guid][1]              | int(10)      | unsigned   | PRI | NO   |         |       |         |
| [itemEntry][2]         | MEDIUMINT(8) | unsigned   |     | NO   |         |       |         |
| [owner_guid][3]        | int(10)      | unsigned   |     | NO   |         |       |         |
| [creatorGuid][4]       | int(10)      | unsigned   |     | NO   |         |       |         |
| [giftCreatorGuid][5]   | int(10)      | unsigned   |     | NO   |         |       |         |
| [count][6]             | int(10)      | unsigned   |     | NO   |         |       |         |
| [duration][7]          | int(10)      | unsigned   |     | NO   |         |       |         |
| [charges][8]           | tinytext     |            |     | YES  | NULL    |       |         |
| [flags][9]             | mediunint(8) | unsigned   |     | NO   |         |       |         |
| [enchantments][10]     | text         |            |     | NO   |         |       |         |
| [randomPropertyId][11] | SMALLINT(5)  | signed     |     | NO   |         |       |         |
| [durability][12]       | SMALLINT(5)  | unsigned   |     | NO   |         |       |         |
| [playedTime][13]       | int(10)      | unsigned   |     | NO   |         |       |         |
| [text][14]             | text         |            |     | YES  | NULL    |       |         |

[1]: #guid
[2]: #itementry
[3]: #owner_guid
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

**Description of the fields**

### guid

The GUID of the item. This number is unique for each item instance.

### itemEnry

[Item](item_template_2130222.html#item_template-entry) entry.

### owner\_guid

The GUID of the character who has ownership of this item. See [characters.guid](2129969.html#characters(table)-guid)

### creatorGuid

[GUID](2129969.html#characters(table)-guid) of character who created the item.

### giftCreatorGuid

[GUID](2129969.html#characters(table)-guid) of character who created the [item](character_gifts_2129986.html#character_gifts-item_guid).

### count

Current number of item copies in the stack.

### duration

`field-no-description|6`

### charges

`The number of charges for each of the five possible spellcharges on an item,  specified via five space separated integers.`

### flags

`field-no-description|8`

### enchantments

Enchantments from SpellItemEnchantment.dbc

### randomPropertyId

`field-no-description|10`

### durability

Current item durability.

### playedTime

Time in seconds

### text

The text contained in that specific item.

data-anchor=
