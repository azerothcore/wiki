# item\_loot\_items

[<-Back-to:Characters](database-characters)

**The \`item\_loot\_items\` table**

Contains the items associated with a lootable inventory item such as a "watertight trunk" or "Bulging Sack of Gems"

This table is populated the first time the player right-clicks to open an item. Rows are deleted when
the player either removes an item or destroys the container item.

**Table Structure**

| Field                | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [container_id][1]    | INT     | UNSIGNED   |     | NO   |         |       |         |
| [item_id][2]         | INT     | UNSIGNED   |     | NO   |         |       |         |
| [item_count][3]      | INT     |            |     | NO   |         |       |         |
| [follow_rules][4]    | TINYINT |            |     | NO   |         |       |         |
| [ffa][5]             | TINYINT |            |     | NO   |         |       |         |
| [blocked][6]         | TINYINT |            |     | NO   |         |       |         |
| [counted][7]         | TINYINT |            |     | NO   |         |       |         |
| [under_threshold][8] | TINYINT |            |     | NO   |         |       |         |
| [needs_quest][9]     | TINYINT |            |     | NO   |         |       |         |
| [rnd_prop][10]       | INT     |            |     | NO   |         |       |         |
| [rnd_suffix][11]     | INT     |            |     | NO   |         |       |         |

[1]: #container_id
[2]: #item_id
[3]: #item_count
[4]: #follow_rules
[5]: #ffa
[6]: #blocked
[7]: #counted
[8]: #under_threshold
[9]: #needs_quest
[10]: #rnd_prop
[11]: #rnd_suffix

**Description of the fields**

### container\_id

The GUID of the container item that holds the loot item(s). See item\_instance.guid

Note: A [container\_id](#item_loot_items-container_id) can have more than one [item\_id](#item_loot_items-item_id) associated with it.

### item\_id

The entry of the loot item. See item\_instance.itemEntry

Note: It is possible for there to be more than one of the same item in a container.

### item\_count

The stack size of the item. Only stackable items can be &gt; 1.

### follow\_rules

Flag to determine if the core should apply additional loot rules when the item
is removed from the container.

### ffa

Flag to determine if free-for-all looting applies. This should typically be 0 because the items are inside

an item in the character's inventory.

### blocked

`field-no-description|6`

### counted

`field-no-description|6`

### under\_threshold

`field-no-description|6`

### needs\_quest

Flag to determine if the item is a quest item to be counted as a "quest drop".

### rnd\_prop

The random enchantment (if any) that was rolled and added to the item when the loot container was
originally opened.

For example: "Ebon Scimitar" (as opposed to a plain "Scimitar").

### rnd\_suffix

The random suffix (if any) that was rolled and added to the item when the loot container was
originally opened.

For example: "of the Monkey"
