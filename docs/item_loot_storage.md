# item\_loot\_storage

[<-Back-to:Characters](database-characters)

**The \`item\_loot\_storage\` table**

Stores the loot that is still inside item containers that have been opened but not fully looted.

**Table: item\_loot\_storage's Structure**

| Field                                  | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [containerGUID](#containerguid)        | INT     | UNSIGNED | NO   |     |         |       |         |
| [itemid](#itemid)                      | INT     | UNSIGNED | NO   |     |         |       |         |
| [count](#count)                        | INT     | UNSIGNED | NO   |     |         |       |         |
| [item_index](#itemindex)               | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [randomPropertyId](#randompropertyid)  | INT     |          | NO   |     |         |       |         |
| [randomSuffix](#randomsuffix)          | INT     | UNSIGNED | NO   |     |         |       |         |
| [follow_loot_rules](#followlootrules)  | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [freeforall](#freeforall)              | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [is_blocked](#isblocked)               | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [is_counted](#iscounted)               | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [is_underthreshold](#isunderthreshold) | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [needs_quest](#needsquest)             | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [conditionLootId](#conditionlootid)    | INT     |          | NO   |     | 0       |       |         |

**Description of the table's fields**

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
