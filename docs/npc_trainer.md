# npc\_trainer

[<-Back-to:World](database-world.md)

**The \`npc\_trainer\` table**

This table contains all the spells that each trainer can teach.

**Structure**

|                                            |              |                |         |          |             |           |             |
|--------------------------------------------|--------------|----------------|---------|----------|-------------|-----------|-------------|
| **Field**                                  | **Type**     | **Attributes** | **Key** | **Null** | **Default** | **Extra** | **Comment** |
| [ID](#npc_trainer-entry)                   | MEDIUMINT | UNSIGNED       | PRI     | NO       | 0           |           |             |
| [SpellID](#npc_trainer-spell)              | MEDIUMINT | SIGNED         | PRI     | NO       | 0           |           |             |
| [MoneyCost](#npc_trainer-spellcost)        | INT      | UNSIGNED       |         | NO       | 0           |           |             |
| [ReqSkillLine](#npc_trainer-reqskill)      | SMALLINT  | UNSIGNED       |         | NO       | 0           |           |             |
| [ReqSkillRank](#npc_trainer-reqskillvalue) | SMALLINT  | UNSIGNED       |         | NO       | 0           |           |             |
| [ReqLevel](#npc_trainer-reqlevel)          | TINYINT   | UNSIGNED       |         | NO       | 0           |           |             |

**Description of the fields**

### ID

Usually, this would be an entry of a creature referring to [creature\_template.entry](creature_template#creature_template-entry). However, Biohazard included several trainer lists by refering to their id. For more information, see [Reference\_list](Trainer_reference).

### SpellID

The spell ID from [Spell.dbc](Spell). If the ID is negative, it's pointing to a reference template.

### MoneyCost

The cost that the player needs to pay in order to learn the spell in copper (1 gold = 100 silver = 10000 cooper). If you get this information from a data site such as Wowhead, be sure to take into account that they usually post the discounted prices based on friendly to exalted with a given faction.

### ReqSkillLine

The required skill the player needs to have in order to be able to learn the spell. See ID in SkillLine.dbc.

### ReqSkillRank

The proficiency in the skill from [reqskill](#npc_trainer-reqskill) that the player needs to meet in order to learn the spell.

### ReqLevel

The level the player needs to be in order to learn the spell.
