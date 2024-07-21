# player\_factionchange\_spells

[<-Back-to:World](database-world)

**The \`player\_factionchange\_spells\` table**

Basically all spell changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id][2]    | INT  | SIGNED     | PRI | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id

**Description of the fields**

### alliance\_id

This is the alliance spell ID. If you convert to horde and your spells have a record in his table, they will be converted to [\#horde\_id](#hordeid)

### horde\_id

This is the horde spell ID. If you convert to alliance and your spells have a record in his table, they will be converted to [\#alliance\_id](#allianceid)
