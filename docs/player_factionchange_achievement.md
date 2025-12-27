# player_factionchange_achievement

[<-Back-to:World](database-world)

**The \`player_factionchange_achievement\` table**

Basically all achievement changes made when player changes faction.

**Table Structure**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            |     | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | SIGNED     | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            |     | YES  | NULL    |       |         |

**Description of the fields**

### alliance_id

This is the alliance achievement ID. If you convert to horde and your achievements have a record in his table, they will be converted to [\#horde_id](##hordeid)

### alliance_comment

comment

### horde_id

This is the horde achievement ID. If you convert to alliance and your achievements have a record in his table, they will be converted to [\#alliance_id](#allianceid)

### horde_comment

comment
