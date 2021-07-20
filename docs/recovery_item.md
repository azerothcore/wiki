# recovery\_item

[<-Back-to:Characters](database-characters.md)

**The \`recovery\_item\` table**

This table holds information about character's matchmaker rating in all team types.

**Structure**

| Field          | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [Id][1]        | INT       | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Guid][2]      | INT       | UNSIGNED   |     | NO   | 0       |                |         |
| [ItemEntry][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [Count][4]     | INT       | UNSIGNED   |     | NO   | 0       |                |         |

[1]: #id
[2]: #guid
[3]: #itementry
[4]: #count

**Description of the fields**

### Id

`field-no-description|1`

### Guid

`field-no-description|2`

### ItemEntry

See [item_template.entry](item_template#entry).

### Count

The amount of items.
