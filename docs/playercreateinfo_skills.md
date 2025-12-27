# playercreateinfo\_skills

[<-Back-to:World](database-world)

# playercreateinfo\_skills table

This table holds information on what skills newly created characters should start out with. A character in this table is defined by his/her race and class combination.

## Structure

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [racemask][1]  | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [classmask][2] | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [skill][3]     | SMALLINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rank][4]      | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment][5]   | VARCHAR(255) |            |     | YES  |         |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #rank
[5]: #comment

## Description of the fields

### racemask

One or more character's race. See [ChrRaces.dbc](chrraces).

### classmask

One or more character's class. See [ChrClasses.dbc](chrclasses).

### Spell

Skill id. See [Skill.dbc](skillline)

### Rank

Rank of the skill.

### Comment

A description of the skill.
