# player\_factionchange\_reputations

[<-Back-to:World](database-world)

**The \`player\_factionchange\_reputations\` table**

Basically all faction/reputation changes made when player changes faction.

**Table: player\_factionchange\_reputations's Structure**

| Field                                | Type |          | Null | Key | Default | Extra | Comment |
| :----------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [alliance_id](#allianceid)           | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |          | YES  |     | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### alliance_id

This is the alliance reputation ID. If you convert to horde and your reputations have a record in his table, they will be converted to [\#horde_id](#hordeid)

See [character_reputation.faction](character_reputation#faction)

### alliance_comment

comment

### horde_id

This is the horde reputation ID. If you convert to alliance and your reputations have a record in his table, they will be converted to [\#alliance_id](#allianceid)

See [character_reputation.faction](character_reputation#faction)

### horde_comment

comment
