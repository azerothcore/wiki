# npc\_trainer

[<-Back-to:World](database-world)

**The \`npc\_trainer\` table**

This table contains all the spells that each trainer can teach.

**Table Structure**

| Field                          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#entry)                   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellID](#spell)              | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [MoneyCost](#spellcost)        | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillLine](#reqskill)      | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillRank](#reqskillvalue) | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqLevel](#reqlevel)          | TINYINT   | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the fields**

### ID

Usually, this would be an entry of a creature referring to [creature\_template.entry](creature_template#entry).

### SpellID

The spell ID is from [Spell.dbc](Spell). If the ID is negative, it's a reference pointing to the positive value of the ID.

### MoneyCost

The price that the player needs to pay to learn the spell in copper. If you get this information from a data site such as Wowhead, consider that they usually post discounted prices based on friendly to exalted with a given faction.'

(1 gold = 100 silver = 10000 cooper).

### ReqSkillLine

The required skill the player needs to have to be able to learn the spell. See ID in SkillLine.dbc.

### ReqSkillRank

The proficiency in the skill from [reqskill](#reqskill) that the player needs to meet to learn the spell.

### ReqLevel

The level the player needs to be to learn the spell.
