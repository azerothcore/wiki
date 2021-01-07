# player\_factionchange\_reputations

[<-Back-to:World](database-world.md)

**The \`player\_factionchange\_reputations\` table**

Basically all faction/reputation changes made when player changes faction.

| Field            | Type   | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------|------------|-----|------|---------|-------|---------|
| [alliance_id][1] | int(8) | unsigned   | PRI | NO   |         |       |         |
| [horde_id][2]    | int(8) | signed     | PRI | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id

**Description of the fields**

### alliance\_id

This is the alliance reputation ID. If you convert to horde and your reputations have a record in his table, they will be converted to [\#horde\_id](#player_factionchange_reputations-horde_id)

See [character\_reputation.faction](character_reputation#faction)

### horde\_id

This is the horde reputation ID. If you convert to alliance and your reputations have a record in his table, they will be converted to [\#alliance\_id](#player_factionchange_reputations-alliance_id)

See [character\_reputation.faction](character_reputation#faction)
