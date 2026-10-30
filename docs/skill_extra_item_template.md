# skill\_extra\_item\_template

[<-Back-to:World](database-world)

**The \`skill\_extra\_item\_template\` table**

This table holds information about when using certain profession spells, you have the chance of creating more than one copy of the item.

**Table: skill\_extra\_item\_template's Structure**

| Field                                             | Type    |          | Null | Key | Default | Extra | Comment                            |
| :------------------------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [spellId](#spellid)                               | INT     | UNSIGNED | NO   | PRI | 0       |       | SpellId of the item creation spell |
| [requiredSpecialization](#requiredspecialization) | INT     | UNSIGNED | NO   |     | 0       |       | Specialization spell id            |
| [additionalCreateChance](#additionalcreatechance) | FLOAT   |          | NO   |     | 0       |       | chance to create add               |
| [additionalMaxNum](#additionalmaxnum)             | TINYINT |          | NO   |     | 0       |       | max num of adds                    |

**Description of the table's fields**

### spellId

The spell ID that creates the item. See [Spell.dbc](spell)

### requiredSpecialization

The required specialization spell ID. The character must have the spell ID specified here learned to have a chance at making another item instantly.

### additionalCreateChance

The chance that the player will make another item instantly.

### additionalMaxNum

The number of extra copies that can be made.
