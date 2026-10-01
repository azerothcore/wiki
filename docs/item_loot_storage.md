# item\_loot_\storage

[<-Back-to:Characters](database-characters)

**The \`item\_loot_\storage\` table**

**Table Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [containerGUID][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [itemid][2]             | INT     | UNSIGNED   |     | NO   |         |       |         |
| [count][3]              | INT     | UNSIGNED   |     | NO   |         |       |         |
| [item_index][13]        | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [randomPropertyId][4]   | INT     | SIGNED     |     | NO   |         |       |         |
| [randomSuffix][5]       | INT     | UNSIGNED   |     | NO   |         |       |         |
| [follow_loot_rules][6]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [freeforall][7]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_blocked][8]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_counted][9]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_underthreshold][10] | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [needs_quest][11]       | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [conditionLootId][12]   | INT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #containerguid
[2]: #itemid
[3]: #count
[4]: #randompropertyid
[5]: #randomsuffix
[6]: #followlootrules
[7]: #freeforall
[8]: #isblocked
[9]: #iscounted
[10]: #isunderthreshold
[11]: #needsquest
[12]: #conditionlootid
[13]: #itemindex

**Description of the fields**

### containerGUID

GUID of the container item the loot is in, for example a clam or a lockbox. See [item\_instance.guid](item_instance#guid).

### itemid

The item entry. See [item\_template.entry](item_template#entry).

### count

Number of items.

### item_index

Index used to distinguish multiple stored stacks of the same item within the same container.

### randomPropertyId

The random property of the item. See [item\_instance.randomPropertyId](item_instance#randompropertyid).

### randomSuffix

The random suffix factor of the item.

### follow\_loot\_rules

1 if the item follows the group loot rules.

### freeforall

1 if every player can loot their own copy of the item.

### is\_blocked

1 if the item is blocked while the group rolls for it.

### is\_counted

1 if the item has been counted for the loot.

### is\_underthreshold

1 if the item quality is below the group loot threshold.

### needs\_quest

1 if the item is a quest item.

### conditionLootId

The SourceGroup of the [conditions](conditions) of the item, 0 if the item has no conditions.
