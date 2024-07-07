# player_factionchange_titles

[<-Back-to:World](database-world)

**The \`spell_cooldown_overrides\` table**

Determines which title should be swapped during a faction change.

**Table Structure**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  |            | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            | PRI | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  |            | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            | PRI | YES  | NULL    |       |         |

**Description of the fields**

### alliance_id

ID from Titles.dbc

### alliance_comment

Title name

### horde_id

ID from Titles.dbc

### horde_comment

Title name
