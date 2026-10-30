# player\_factionchange\_quests

[<-Back-to:World](database-world)

**The \`player\_factionchange\_quests\` table**

Determains what quest should be changed during a faction change

**Table: player\_factionchange\_quests's Structure**

| Field                      | Type |          | Null | Key | Default | Extra | Comment |
| :------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [alliance_id](#allianceid) | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [horde_id](#hordeid)       | INT  | UNSIGNED | NO   | PRI |         |       |         |

**Description of the table's fields**

### alliance_id

[quest_template.id](quest_template#id).

### horde_id

[quest_template.id](quest_template#id).
