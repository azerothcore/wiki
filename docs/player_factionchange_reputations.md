# player\_factionchange\_reputations

[<-Back-to:World](database-world)

**The \`player\_factionchange\_reputations\` table**

Basically all faction/reputation changes made when player changes faction.

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id][2]    | INT  | SIGNED     | PRI | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id

**Description of the fields**

### alliance\_id

This is the alliance reputation ID. If you convert to horde and your reputations have a record in his table, they will be converted to [\#horde\_id](#hordeid)

See [character\_reputation.faction](character_reputation#faction)

### horde\_id

This is the horde reputation ID. If you convert to alliance and your reputations have a record in his table, they will be converted to [\#alliance\_id](#allianceid)

See [character\_reputation.faction](character_reputation#faction)
