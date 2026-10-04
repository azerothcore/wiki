# item\_enchantment\_template

[<-Back-to:World](database-world)

**The \`item\_enchantment\_template\` table**

This table holds enchantment chance information for items that should have either a random property or a random suffix attached to them.

**Table: item\_enchantment\_template's Structure**

| Field             | Type  |          | Null | Key | Default | Extra | Comment |
| :---------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)   | INT   | UNSIGNED | NO   | PRI | 0       |       |         |
| [ench](#ench)     | INT   | UNSIGNED | NO   | PRI | 0       |       |         |
| [chance](#chance) | FLOAT |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### entry

This field ties in with EITHER RandomProperty OR RandomSuffix fields in the [item\_template](item_template) table. An item cannot have both of those fields set at non-zero values.

### ench

The enchantment to apply on the item. If the entry for the current row is used in RandomProperty, then this field points to the ID in ItemRandomProperties.dbc. If the entry is used in RandomSuffix, then this field points to the ID in [ItemRandomSuffix.dbc](https://wowdev.wiki/DB/ItemRandomSuffix).

### chance

The chance for a random property or suffix to be applied to the item. For each entry in this table, the combined chances of all properties/suffixes need to equal 100 otherwise the item may not get a random enchantment on it.

Value must be >=0. If the value does not meet the condition the SQL will fail on `item_enchantment_template_chk_1`.
