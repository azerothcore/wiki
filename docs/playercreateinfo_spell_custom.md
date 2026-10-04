# playercreateinfo\_spell\_custom

[<-Back-to:World](database-world)

**The \`playercreateinfo\_spell\_custom\` table**

This table holds information on what spells newly created characters should start with if the PlayerStart.AllSpells setting is enabled in worldserver.conf. A character in this table is defined by his/her race and class combination.

Please note you'll have to set PlayerStart.CustomSpells to 1 in config, if not, this table will not have any effect.

**Table: playercreateinfo\_spell\_custom's Structure**

| Field                   | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [racemask](#racemask)   | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [classmask](#classmask) | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [Spell](#spell)         | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [Note](#note)           | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### racemask

One or more character's race. See [ChrRaces.dbc](chrraces).

### classmask

One or more character's class. See [ChrClasses.dbc](chrclasses)

### Spell

Spell id. See [Spell.dbc](spell)

### Note

Basically a comment of what your query does.
