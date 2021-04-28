# playercreateinfo\_skills

# playercreateinfo\_skills table

This table holds information on what skills newly created characters should start out with. A character in this table is defined by his/her race and class combination.

## Structure

| Field                                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|---------------------------------------------|--------------|------------|-----|------|---------|-------|---------|
| [racemask](#playercreateinfo_skills-race)   | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [classmask](#playercreateinfo_skills-class) | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [skill](SkillLine)                          | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| rank                                        | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| Comment                                     | VARCHAR(255) | SIGNED     |     | YES  |         |       |         |

 

## Description of the fields

### racemask

One or more character's race. See [ChrRaces](ChrRaces).

### classmask

One or more character's class. See ChrClasses.

### Spell

Skill id. See [Skill.dbc](SkillLine)

### Rank

Rank of the skill.

### Comment

A description of the skill.
