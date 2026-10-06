# player\_factionchange\_achievement

[<-Back-to:World](database-world)

**The \`player\_factionchange\_achievement\` table**

Basically all achievement changes made when player changes faction.

**Table: player\_factionchange\_achievement's Structure**

| Field                                | Type |          | Null | Key | Default | Extra | Comment |
| :----------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [alliance_id](#allianceid)           | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |          | YES  |     | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### alliance_id

This is the alliance achievement ID. If you convert to horde and your achievements have a record in his table, they will be converted to [\#horde_id](#hordeid)

### alliance_comment

comment

### horde_id

This is the horde achievement ID. If you convert to alliance and your achievements have a record in his table, they will be converted to [\#alliance_id](#allianceid)

### horde_comment

comment
