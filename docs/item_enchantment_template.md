# item\_enchantment\_template

[<-Back-to:World](database-world.md)

**The \`item\_enchantment\_template\` table**

This table holds enchantment chance information for items that should have either a random property or a random suffix attached to them.

**Structure**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------|--------------|------------|-----|------|---------|-------|---------|
| [entry][1]  | mediumint(8) | unsigned   | PRI | NO   | 0       |       |         |
| [ench][2]   | mediumint(8) | unsigned   | PRI | NO   | 0       |       |         |
| [chance][3] | float        | unsigned   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #ench
[3]: #chance

**Description of the fields**

### entry

This field ties in with EITHER RandomProperty OR RandomSuffix fields in the [item\_template](http://www.azerothcore.org/wiki/item_template) table. An item cannot have both of those fields set at non-zero values.

### ench

The enchantment to apply on the item. If the entry for the current row is used in RandomProperty, then this field points to the ID in ItemRandomProperties.dbc. If the entry is used in RandomSuffix, then this field points to the ID in [ItemRandomSuffix.dbc](ItemRandomSuffix).

### chance

The chance for a random property or suffix to be applied to the item. For each entry in this table, the combined chances of all properties/suffixes need to equal 100 otherwise the item may not get a random enchantment on it.
