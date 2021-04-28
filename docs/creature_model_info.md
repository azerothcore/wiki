# creature\_model\_info

[<-Back-to:World](database-world.md)

**The \`creature\_model\_info\` table**

This table contains all models of mobs, their gender and other information that are model related. This means that when a creature uses another model, this information will change as well.

**Structure**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment |
|---------------------------|--------------|------------|-----|------|---------|-------|---------|
| [modelid][1]              | MEDIUMINT(8) | UNSIGNED   | PRI | NO   | 0       |       |         |
| [bounding_radius][2]      | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [combat_reach][3]         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [gender][4]               | TINYINT(3)   | UNSIGNED   |     | NO   | 2       |       |         |
| [modelid_other_gender][5] | MEDIUMINT(8) | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #modelid
[2]: #bounding_radius
[3]: #combat_reach
[4]: #gender
[5]: #modelid_other_gender

**Description of the fields**

### modelid

Display ID from [CreatureDisplayInfo.dbc](CreatureDisplayInfo)

### bounding\_radius

This field is unused. It's purpose is currently unknown. It may or may not be linked to path-finding.

### combat\_reach

This value is the unit's radius in term of game mechanics: The bigger this value is, the higher the unit's range is and also the further away it can get hit from.

### gender

Gender of the creature

| Value | Description |
|-------|-------------|
| 0     | Male        |
| 1     | Female      |
| 2     | None        |

Note: do not modify this field without sniffs or talking to Kinzcool before (ref commit: http://git.io/T7RLmA).

### modelid\_other\_gender

Point to Creature\_model\_info.modelid.
When the entry is gender male (0) or female (1), this value can point to the opposite gender counterpart.
