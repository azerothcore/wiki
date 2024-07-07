# playercreateinfo\_item

[<-Back-to:World](database-world)

**The \`playercreateinfo\_item\` table**

This table is used for any custom items that you might want to give to characters on creation. I used to be used to hold the normal items that characters get as well, but now that info is read from CharStartOutfit.dbc

**Table Structure**

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

**Description of the fields**

### race

The character's race.
`:ChrRaces.dbc_tc2`

### class

The character's class.
`:ChrClasses.dbc_tc2`

### itemid

The template ID of the item. See item\_template.entry

### amount

The number of copies of that item.

### Note

Note of the entry
