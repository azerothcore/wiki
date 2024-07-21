# character\_spell\_cooldown

[<-Back-to:Characters](database-characters)

**The \`character\_spell\_cooldown\` table**

Holds the remaining cooldowns from either character spells or item spells for each character.

**Table Structure**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier                   |
| [item][3]     | INT       | UNSIGNED   |     | NO   | 0       |       | Item Identifier                    |
| [time][4]     | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |
| [needSend][5] | INT       | UNSIGNED   |     | NO   | 1       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #item
[4]: #time
[5]: #needsend

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### item

If the spell was casted from an item, the item ID. See [item\_template.entry](item_template#entry).

### time

The time when the spell cooldown will finish, measured in [Unix time](http://en.wikipedia.org/wiki/Unix_time).

### needSend

`field-no-description|5`
