# playercreateinfo\_skills

[<-Back-to:World](database-world)

# playercreateinfo\_skills table

This table holds information on what skills newly created characters should start out with. A character in this table is defined by his/her race and class combination.

**Table: playercreateinfo\_skills's Structure**

| Field                   | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [raceMask](#racemask)   | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [classMask](#classmask) | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [skill](#skill)         | SMALLINT     | UNSIGNED | NO   | PRI |         |       |         |
| [rank](#rank)           | SMALLINT     | UNSIGNED | NO   |     | 0       |       |         |
| [comment](#comment)     | VARCHAR(255) |          | YES  |     | NULL    |       |         |

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
