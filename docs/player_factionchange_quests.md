# player\_factionchange\_quests

[<-Back-to:World](database-world)

**The \`player\_factionchange\_quests\` table**

Determains what quest should be changed during a faction change

**Table: player\_factionchange\_quests's Structure**

| Field                      | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid) | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id](#hordeid)       | INT  | UNSIGNED   | PRI | NO   |         |       |         |

**Description of the table's fields**

### alliance_id

[quest_template.id](quest_template#id).

### horde_id

[quest_template.id](quest_template#id).
