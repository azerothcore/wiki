# recovery\_item

[<-Back-to:Characters](database-characters)

**The \`recovery\_item\` table**

This table holds information about saved items into database when the player sells items to vendor
Items which were kept back in the database after being deleted and are older than the specified amount of days, will be completely deleted.

**Table Structure**

| Field          | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [Id][1]        | INT       | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Guid][2]      | INT       | UNSIGNED   |     | NO   | 0       |                |         |
| [ItemEntry][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [Count][4]     | INT       | UNSIGNED   |     | NO   | 0       |                |         |
| [DeleteDate][5] | INT      | UNSIGNED   |     | YES  | NULL    |                |         |

[1]: #id
[2]: #guid
[3]: #itementry
[4]: #count
[5]: #deletedate

**Description of the fields**

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
