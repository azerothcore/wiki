# playercreateinfo\_skills

[<-Back-to:World](database-world)

# playercreateinfo\_skills table

This table holds information on what skills newly created characters should start out with. A character in this table is defined by his/her race and class combination.

**Table: playercreateinfo\_skills's Structure**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [raceMask][1]  | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [classMask][2] | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [skill][3]     | SMALLINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rank][4]      | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [comment][5]   | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #racemask
[2]: #classmask
[3]: #skill
[4]: #rank
[5]: #comment

**Description of the table's fields**

### racemask

One or more character's race. See [ChrRaces.dbc](chrraces).

### classmask

One or more character's class. See [ChrClasses.dbc](chrclasses).

### skill

Skill id. See [Skill.dbc](skillline)

### Rank

Rank of the skill.

### Comment

A description of the skill.
