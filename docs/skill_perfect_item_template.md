# skill\_perfect\_item\_template

[<-Back-to:World](database-world)

**The \`skill\_perfect\_item\_template\` table**

Implements the *perfection* crafting system (originally from The Burning Crusade): when a crafting spell is cast, it may create a higher-quality “perfect” version of the item instead of the normal one. Each row defines the perfect-craft chance and the replacement item for a creation spell.

**Table: skill\_perfect\_item\_template's Structure**

| Field                                             | Type  |          | Null | Key | Default | Extra | Comment                                   |
| :------------------------------------------------ | :---- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------- |
| [spellId](#spellid)                               | INT   | UNSIGNED | NO   | PRI | 0       |       | SpellId of the item creation spell        |
| [requiredSpecialization](#requiredspecialization) | INT   | UNSIGNED | NO   |     | 0       |       | Specialization spell id                   |
| [perfectCreateChance](#perfectcreatechance)       | FLOAT |          | NO   |     | 0       |       | chance to create the perfect item instead |
| [perfectItemType](#perfectitemtype)               | INT   | UNSIGNED | NO   |     | 0       |       | perfect item type to create instead       |

**Description of the table's fields**

### spellId

SpellId of the item creation spell

### requiredSpecialization

Specialization spell id

### perfectCreateChance

chance to create the perfect item instead

### perfectItemType

perfect item type to create instead
