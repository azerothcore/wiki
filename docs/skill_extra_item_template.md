# skill\_extra\_item\_template

[<-Back-to:World](database-world)

**The \`skill\_extra\_item\_template\` table**

This table holds information about when using certain profession spells, you have the chance of creating more than one copy of the item.

**Table Structure**

| Field                       | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| --------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [spellId][1]                | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | SpellId of the item creation spell |
| [requiredSpecialization][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | Specialization spell id            |
| [additionalCreateChance][3] | FLOAT     | SIGNED     |     | NO   | 0       |       | chance to create add               |
| [additionalMaxNum][4]       | TINYINT   | UNSIGNED   |     | NO   | 0       |       | max num of adds                    |

[1]: #spellid
[2]: #requiredspecialization
[3]: #additionalcreatechance
[4]: #additionalmaxnum

**Description of the fields**

### spellId

The spell ID that creates the item. See [Spell.dbc](Spell)

### requiredSpecialization

The required specialization spell ID. The character must have the spell ID specified here learned to have a chance at making another item instantly.

### additionalCreateChance

The chance that the player will make another item instantly.

### additionalMaxNum

The number of extra copies that can be made.
