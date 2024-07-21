# player\_factionchange\_items

[<-Back-to:World](database-world)

**The \`player\_factionchange\_items\` table**

Basically all item changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race_A][1]      | INT  | SIGNED     |     | NO   |         |       |         |
| [alliance_id][2] | INT  | SIGNED     | PRI | NO   |         |       |         |
| [commentA][3]    | tex  | SIGNED     |     |      |         |       |         |
| [race_H][4]      | INT  | SIGNED     |     | NO   |         |       |         |
| [horde_id][5]    | INT  | SIGNED     | PRI | NO   |         |       |         |
| [commentH][6]    | INT  | SIGNED     |     |      |         |       |         |

[1]: #race_a
[2]: #alliance_id
[3]: #commenta
[4]: #race_h
[5]: #horde_id
[6]: #commenth

**Description of the fields**

### race\_A

Not implemented.

See item\_template.AllowableRace

### alliance\_id

This is the alliance item ID. If you convert to horde and your items have a record in his table, they will be converted to [\#horde\_id](#hordeid)

### commentA

This is for easy item name identifying. Comment style should be name(ItemLevel)

### race\_H

Not implemented.

See [item\_template.AllowableRace](item_template#allowablerace)

### horde\_id

This is the horde item ID. If you convert to alliance and your items have a record in his table, they will be converted to [\#alliance\_id](#allianceid)

### commentH

This is for easy item name identifying. Comment style should be name (ItemLevel)
