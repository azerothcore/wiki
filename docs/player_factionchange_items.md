# player\_factionchange\_items

[<-Back-to:World](database-world)

**The \`player\_factionchange\_items\` table**

Basically all item changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][2]      | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment][3] | TEXT |            |     | NO   |         |       |         |
| [horde_id][5]         | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_comment][6]    | TEXT |            |     | NO   |         |       |         |

[2]: #alliance_id
[3]: #alliance_comment
[5]: #horde_id
[6]: #horde_comment

**Description of the fields**

### alliance\_id

This is the alliance item ID. If you convert to horde and your items have a record in his table, they will be converted to [\#horde\_id](#hordeid)

### alliance\_comment

This is for easy item name identifying. Comment style should be name(ItemLevel)

### horde\_id

This is the horde item ID. If you convert to alliance and your items have a record in his table, they will be converted to [\#alliance\_id](#allianceid)

### horde\_comment

This is for easy item name identifying. Comment style should be name (ItemLevel)
