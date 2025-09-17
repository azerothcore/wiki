# creature\_model\_info

[<-Back-to:World](database-world)

**The \`creature\_model\_info\` table**

This table contains all models of mobs, their gender and other information that are model related. This means that when a creature uses another model, this information will change as well.

**Table Structure**

| Field                       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [DisplayID][1]              | int     | unsigned   | PRI | NO   | 0       |       |         |
| [BoundingRadius][2]         | float   |            |     | NO   | 0       |       |         |
| [CombatReach][3]            | float   |            |     | NO   | 0       |       |         |
| [Gender][4]                 | tinyint | unsigned   |     | NO   | 2       |       |         |
| [DisplayID_Other_Gender][5] | int     | unsigned   |     | NO   | 0       |       |         |

[1]: #displayid
[2]: #boundingradius
[3]: #combatreach
[4]: #gender
[5]: #displayidothergender

**Description of the fields**

### DisplayID

Display ID from [CreatureDisplayInfo.dbc](CreatureDisplayInfo)

### BoundingRadius

This field is unused. It's purpose is currently unknown. It may or may not be linked to path-finding.

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
