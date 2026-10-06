# item\_instance

[<-Back-to:Characters](database-characters)

**The \`item\_instance\` table**

This table holds individual item instance information for all items currently equipped in some kind of character bag or bank, in auction houses, in guild banks or in mails.

**Table: item\_instance's Structure**

| Field                                 | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)                         | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [itemEntry](#itementry)               | INT      | UNSIGNED | YES  |     | 0       |       |         |
| [owner_guid](#ownerguid)              | INT      | UNSIGNED | NO   | MUL | 0       |       |         |
| [creatorGuid](#creatorguid)           | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [giftCreatorGuid](#giftcreatorguid)   | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [count](#count)                       | INT      | UNSIGNED | NO   |     | 1       |       |         |
| [duration](#duration)                 | INT      |          | NO   |     | 0       |       |         |
| [charges](#charges)                   | TINYTEXT |          | YES  |     | NULL    |       |         |
| [flags](#flags)                       | INT      | UNSIGNED | YES  |     | 0       |       |         |
| [enchantments](#enchantments)         | TEXT     |          | NO   |     |         |       |         |
| [randomPropertyId](#randompropertyid) | SMALLINT |          | NO   |     | 0       |       |         |
| [durability](#durability)             | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [playedTime](#playedtime)             | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [text](#text)                         | TEXT     |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### guid

The GUID of the item. This number is unique for each item instance.

### itemEntry

[Item_template.entry](item_template#entry).

### owner\_guid

The GUID of the character who has ownership of this item. See [characters.guid](characters#guid).

### creatorGuid

[Characters.guid](characters#guid) of character who created the item.

### giftCreatorGuid

[Characters.guid](characters#guid) of character who created the [item](character_gifts#itemguid).

### count

Current number of item copies in the stack.

### duration

Time in seconds before the item disappears, for items with a limited duration. 0 if the item does not expire.

### charges

The number of charges for each of the five possible spellcharges on an item, specified via five space separated integers.

### flags

| Value | Hex      | Flag                          | Comment                                             |
| :---- | :------: | :---------------------------- | :-------------------------------------------------- |
| 1     | `0x0001` | ITEM_FIELD_FLAG_SOULBOUND     | The item is soulbound.                              |
| 4     | `0x0004` | ITEM_FIELD_FLAG_UNLOCKED      | The item had a lock that has been opened.           |
| 8     | `0x0008` | ITEM_FIELD_FLAG_WRAPPED       | The item is wrapped and contains another item.      |
| 256   | `0x0100` | ITEM_FIELD_FLAG_BOP_TRADEABLE | The soulbound item can still be traded for a while. |
| 512   | `0x0200` | ITEM_FIELD_FLAG_READABLE      | Right clicking the item opens a text page.          |
| 4096  | `0x1000` | ITEM_FIELD_FLAG_REFUNDABLE    | The item can still be returned to the vendor.       |

### enchantments

Enchantments from SpellItemEnchantment.dbc see: [item_instance_enchantments](item_instance_enchantments)

### randomPropertyId

The random enchantment of the item. A positive value is an ID from ItemRandomProperties.dbc, a negative value is an ID from ItemRandomSuffix.dbc. 0 if none.

### durability

Current item durability.

### playedTime

Time in seconds.

### text

The text contained in that specific item.
