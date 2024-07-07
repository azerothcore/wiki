# player_factionchange_quest

[<-Back-to:World](database-world)

**The \`player_factionchange_quest\` table**

Determains what quest should be changed during a faction change

**Table Structure**

| Field                      | Type | Attributes | Key        | Null | Default | Extra | Comment |
| -------------------------- | ---- | ---------- | ---------- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid) | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |
| [horde_id](#hordeid)       | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |

**Description of the fields**

### alliance_id

[quest_template.id](quest_template#id).

### horde_id

[quest_template.id](quest_template#id).
