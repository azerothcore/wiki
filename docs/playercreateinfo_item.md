# playercreateinfo\_item

[<-Back-to:World](database-world.md)

**The \`playercreateinfo\_item\` table**

This table is used for any custom items that you might want to give to characters on creation. I used to be used to hold the normal items that characters get as well, but now that info is read from CharStartOutfit.dbc

**Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| :-----------|:----------|:-----------|:----|:-----|:--------|:------|:--------|
| [race][1]   | tinyint   | unsigned   | PRI | NO   | 0       |       |         |
| [class][2]  | tinyint   | unsigned   | PRI | NO   | 0       |       |         |
| [itemid][3] | mediumint | unsigned   | PRI | NO   | 0       |       |         |
| [amount][4] | smallint  | unsigned   |     | NO   | 1       |       |         |

[1]: #race
[2]: #class
[3]: #itemid
[4]: #amount

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
