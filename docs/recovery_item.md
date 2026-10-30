# recovery\_item

[<-Back-to:Characters](database-characters)

**The \`recovery\_item\` table**

This table holds information about saved items into database when the player sells items to vendor
Items which were kept back in the database after being deleted and are older than the specified amount of days, will be completely deleted.

**Table: recovery\_item's Structure**

| Field                     | Type |          | Null | Key | Default | Extra          | Comment |
| :------------------------ | :--- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [Id](#id)                 | INT  | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [Guid](#guid)             | INT  | UNSIGNED | NO   | MUL | 0       |                |         |
| [ItemEntry](#itementry)   | INT  | UNSIGNED | YES  |     | 0       |                |         |
| [Count](#count)           | INT  | UNSIGNED | NO   |     | 0       |                |         |
| [DeleteDate](#deletedate) | INT  | UNSIGNED | YES  |     | NULL    |                |         |

**Description of the table's fields**

### Id

The ordinal number of the record in this table.

### Guid

Character guid

See [characters.guid](characters#guid).

### ItemEntry

See [item_template.entry](item_template#entry).

### Count

The amount of items.

### DeleteDate

Unix timestamp of when the item was deleted. Used to determine when the record is old enough to be purged permanently. `NULL` if not set.
