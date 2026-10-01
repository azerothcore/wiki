# playercreateinfo_item

[<-返回至:World](database-world)

**`playercreateinfo_item` 表**

该表用于你想在创建角色时给予角色的任何自定义物品。过去它也用于保存角色获得的常规物品，但现在这些信息是从 CharStartOutfit.dbc 读取的。

**表结构**

| Field       | Type      | Attributes | Key  | Null | Default | Extra | Comment |
| :---------- | :-------- | :--------- | :--- | :--- | :------ | :---- | :------ |
| [race][1]   | TINYINT   | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [class][2]  | TINYINT   | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [itemid][3] | MEDIUMINT | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [amount][4] | SMALLINT  | UNSIGNED   |      | NO   | 1       |       |         |
| [Note][5]   | VARCHAR   |            |      | YES  | NULL    |       |         |

[1]: #race
[2]: #class
[3]: #itemid
[4]: #amount
[5]: #Note

**字段说明**

### race

角色种族。
`:ChrRaces.dbc_tc2`

### class

角色职业。
`:ChrClasses.dbc_tc2`

### itemid

物品的模板 ID。参见 item_template.entry

### amount

该物品的数量。

### Note

条目注释
