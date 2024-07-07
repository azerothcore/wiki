# item\_instance

[<-Back-to:Characters](database-characters)

**The \`item\_instance\` table**

This table holds individual item instance information for all items currently equipped in some kind of character bag or bank, in auction houses, in guild banks or in mails.

**Table Structure**

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

**Description of the fields**

### guid

The GUID of the item. This number is unique for each item instance.

### itemEntry

[Item_template.entry](item_template#entry).

### owner\_guid

The GUID of the character who has ownership of this item. See [characters.guid](characters#guid).

### creatorGuid

[Characters.guid](characters#guid) of character who created the item.

### giftCreatorGuid

[Characters.guid](characters#guid) of character who created the [item](character_gifts#item_guid).

### count

Current number of item copies in the stack.

### duration

`field-no-description|6`

### charges

The number of charges for each of the five possible spellcharges on an item, specified via five space separated integers.

### flags

`field-no-description|8`

### enchantments

Enchantments from SpellItemEnchantment.dbc see: [item_instance_enchantments](item_instance_enchantments)

### randomPropertyId

`field-no-description|10`

### durability

Current item durability.

### playedTime

Time in seconds.

### text

The text contained in that specific item.
