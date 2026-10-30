# creature\_model\_info

[<-Back-to:World](database-world)

**The \`creature\_model\_info\` table**

This table contains all models of mobs, their gender and other information that are model related. This means that when a creature uses another model, this information will change as well.

**Table: creature\_model\_info's Structure**

| Field                                           | Type      |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------------- | :-------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [DisplayID](#displayid)                         | INT       | UNSIGNED | NO   | PRI | 0       |       |         |
| [BoundingRadius](#boundingradius)               | FLOAT     |          | NO   |     | 0       |       |         |
| [CombatReach](#combatreach)                     | FLOAT     |          | NO   |     | 0       |       |         |
| [Gender](#gender)                               | TINYINT   | UNSIGNED | NO   |     | 2       |       |         |
| [DisplayID_Other_Gender](#displayidothergender) | INT       | UNSIGNED | NO   |     | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)                 | MEDIUMINT |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### DisplayID

Display ID from [CreatureDisplayInfo.dbc](https://wowdev.wiki/DB/CreatureDisplayInfo)

### BoundingRadius

The bounding radius of the model. The core multiplies it by the creature's scale and sends the result to the client as the unit's bounding radius.

### CombatReach

This value is the unit's radius in term of game mechanics: The bigger this value is, the higher the unit's range is and also the further away it can get hit from.

### Gender

Gender of the creature

| Value | Description |
| ----- | ----------- |
| 0     | Male        |
| 1     | Female      |
| 2     | None        |

Note: do not modify this field without sniffs (ref commit: http://git.io/T7RLmA).

### DisplayID_Other_Gender

Point to Creature\_model\_info.modelid.
When the entry is gender male (0) or female (1), this value can point to the opposite gender counterpart.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
