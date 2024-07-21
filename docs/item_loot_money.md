# item\_loot\_money

[<-Back-to:Characters](database-characters)

**The \`item\_loot\_money\` table**

Contains the money associated with a lootable inventory item
such as a "Fat Sack of Coins"

This table is populated the first time the player right-clicks to open an item. Rows are deleted when
the player either removes the money or destroys the container item.

**Table Structure**

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [container_id][1] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [money][2]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #container_id
[2]: #money

**Description of the fields**

### container\_id

The GUID of the container item. See item\_instance.guid

### money

The amount of money loot in copper.
