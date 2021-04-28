# character\_spell\_cooldown

[<-Back-to:Characters](database-characters.md)

**The \`character\_spell\_cooldown\` table**

Holds the remaining cooldowns from either character spells or item spells for each character.

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment                            |
|------------|--------------|------------|-----|------|---------|-------|------------------------------------|
| [guid][1]  | INT(10)      | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2] | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       | Spell Identifier                   |
| [item][3]  | INT(10)      | unsigned   |     | NO   | 0       |       | Item Identifier                    |
| [time][4]  | INT(10)      | unsigned   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #item
[4]: #time

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### spell

The spell ID. See Spell.dbc column 1

### item

If the spell was casted from an item, the item ID. See item\_template.entry

### time

The time when the spell cooldown will finish, measured in [Unix time](http://en.wikipedia.org/wiki/Unix_time)
