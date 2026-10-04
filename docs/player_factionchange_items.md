# player\_factionchange\_items

[<-Back-to:World](database-world)

**The \`player\_factionchange\_items\` table**

Basically all item changes made when player changes faction.

**Table: player\_factionchange\_items's Structure**

| Field                                | Type |          | Null | Key | Default | Extra | Comment |
| :----------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [alliance_id](#allianceid)           | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |          | NO   |     |         |       |         |
| [horde_id](#hordeid)                 | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |          | NO   |     |         |       |         |

**Description of the table's fields**

### alliance\_id

This is the alliance item ID. If you convert to horde and your items have a record in his table, they will be converted to [\#horde\_id](#hordeid)

### alliance\_comment

This is for easy item name identifying. Comment style should be name(ItemLevel)

### horde\_id

This is the horde item ID. If you convert to alliance and your items have a record in his table, they will be converted to [\#alliance\_id](#allianceid)

### horde\_comment

This is for easy item name identifying. Comment style should be name (ItemLevel)
