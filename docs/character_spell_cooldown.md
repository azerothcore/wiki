# character\_spell\_cooldown

[<-Back-to:Characters](database-characters)

**The \`character\_spell\_cooldown\` table**

Holds the remaining cooldowns from either character spells or item spells for each character.

**Table: character\_spell\_cooldown's Structure**

| Field                 | Type    |          | Null | Key | Default | Extra | Comment                            |
| :-------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [guid](#guid)         | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier, Low part |
| [spell](#spell)       | INT     | UNSIGNED | NO   | PRI | 0       |       | Spell Identifier                   |
| [category](#category) | INT     | UNSIGNED | YES  |     | 0       |       | Spell category                     |
| [item](#item)         | INT     | UNSIGNED | NO   |     | 0       |       | Item Identifier                    |
| [time](#time)         | INT     | UNSIGNED | NO   |     | 0       |       |                                    |
| [needSend](#needsend) | TINYINT | UNSIGNED | NO   |     | 1       |       |                                    |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### category

Spell category the cooldown belongs to (category cooldowns are shared by all spells of the same category). `0` if the spell has no category.

### item

If the spell was casted from an item, the item ID. See [item\_template.entry](item_template#entry).

### time

The time when the spell cooldown will finish, measured in [Unix time](http://en.wikipedia.org/wiki/Unix_time).

### needSend

Boolean (0 or 1). If 1, the cooldown entry needs to be sent to the client on next login.
