# playercreateinfo\_spell\_custom

[<-Back-to:World](database-world.md)

This table holds information on what spells newly created characters should start out with if the PlayerStart.AllSpells setting in enabled in worldserver.conf. A character in this table is defined by his/her race and class combination.

Please note you'll have to set PlayerStart.AllSpells to 1 in config, else this table will not have any effect.

## Structure

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
|----------------|--------------|------------|-----|------|---------|-------|---------|
| [racemask][1]  | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [classmask][2] | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Spell][3]     | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Note][4]      | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #note

## Description of the fields

### racemask

One or more character's race. See [ChrRaces.dbc](chrraces).

### classmask

One or more character's class. See [ChrClasses.dbc](chrclasses)

### Spell

Spell id. See [Spell.dbc](Spell)

### Note

Basically a comment of what your query does.
