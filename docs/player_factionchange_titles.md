# player\_factionchange\_titles

[<-Back-to:World](database-world)

**The \`player\_factionchange\_titles\` table**

Determines which title should be swapped during a faction change.

**Table: player\_factionchange\_titles's Structure**

| Field                                | Type |     | Null | Key | Default | Extra | Comment |
| :----------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [alliance_id](#allianceid)           | INT  |     | NO   | PRI |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |     | YES  |     | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  |     | NO   | PRI |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |     | YES  |     | NULL    |       |         |

**Description of the table's fields**

### alliance_id

ID from Titles.dbc

### alliance_comment

Title name

### horde_id

ID from Titles.dbc

### horde_comment

Title name
