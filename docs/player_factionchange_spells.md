# player\_factionchange\_spells

[<-Back-to:World](database-world)

**The \`player\_factionchange\_spells\` table**

Basically all spell changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment][3] | TEXT |        |     | NO   |         |       |         |
| [horde_id][2]    | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_comment][4] | TEXT |          |     | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id
[3]: #alliance_comment
[4]: #horde_comment

**Description of the fields**

### alliance\_id

This is the alliance spell ID. If you convert to horde and your spells have a record in his table, they will be converted to [\#horde\_id](#hordeid)

### alliance\_comment

Optional comment for easy identification of the alliance spell (e.g. the spell name).

### horde\_id

This is the horde spell ID. If you convert to alliance and your spells have a record in his table, they will be converted to [\#alliance\_id](#allianceid)

### horde\_comment

Optional comment for easy identification of the horde spell (e.g. the spell name).
