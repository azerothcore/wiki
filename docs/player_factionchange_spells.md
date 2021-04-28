# player\_factionchange\_spells

[<-Back-to:World](database-world.md)

**The \`player\_factionchange\_spells\` table**

Basically all spell changes made when player changes faction.

| Field            | Type   | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------|------------|-----|------|---------|-------|---------|
| [alliance_id][1] | INT(8) | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id][2]    | INT(8) | SIGNED     | PRI | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id

**Description of the fields**

### alliance\_id

This is the alliance spell ID. If you convert to horde and your spells have a record in his table, they will be converted to [\#horde\_id](#player_factionchange_spells-horde_id)

### horde\_id

This is the horde spell ID. If you convert to alliance and your spells have a record in his table, they will be converted to [\#alliance\_id](#player_factionchange_spells-alliance_id)
