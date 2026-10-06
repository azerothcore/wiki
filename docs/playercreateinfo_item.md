# playercreateinfo\_item

[<-Back-to:World](database-world)

**The \`playercreateinfo\_item\` table**

This table is used for any custom items that you might want to give to characters on creation. I used to be used to hold the normal items that characters get as well, but now that info is read from CharStartOutfit.dbc

**Table: playercreateinfo\_item's Structure**

| Field             | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [race](#race)     | TINYINT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [class](#class)   | TINYINT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [itemid](#itemid) | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [amount](#amount) | INT          |          | NO   |     | 1       |       |         |
| [Note](#note)     | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
