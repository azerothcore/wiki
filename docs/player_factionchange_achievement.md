# player\_factionchange\_achievement

[<-Back-to:World](database-world)

**The \`player\_factionchange\_achievement\` table**

Basically all achievement changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id][2]    | INT  | SIGNED     | PRI | NO   |         |       |         |

[1]: #allianceid
[2]: #hordeid

**Description of the fields**

### alliance_id

This is the alliance achievement ID. If you convert to horde and your achievements have a record in his table, they will be converted to [\#horde\_id](##hordeid)

### horde_id

This is the horde achievement ID. If you convert to alliance and your achievements have a record in his table, they will be converted to [\#alliance\_id](#allianceid)
