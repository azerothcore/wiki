# recovery\_item

[<-返回至:Characters](database-characters)

**`recovery\_item` 表**

此表保存玩家向商人出售物品时保存到数据库中的物品信息。
被删除后保留在数据库中、且超过指定天数的物品，将被完全删除。

**表结构**

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

**字段说明**

### Id

此表中记录的序号。

### Guid

角色 guid

参见 [characters.guid](characters#guid)。

### ItemEntry

参见 [item_template.entry](item_template#entry)。

### Count

物品的数量。

### DeleteDate

物品被删除时的 Unix 时间戳。用于判断记录何时足够旧、可以被永久清除。如果未设置则为 `NULL`。
