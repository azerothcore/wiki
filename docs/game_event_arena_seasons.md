# game\_event\_arena\_seasons

[<-Back-to:World](database-world.md)

**The \`game\_event\_arena\_seasons\` table**

This information comes from sniffs and is NOT supposed to be changed.

**Structure**

| Field           | Type       | Attributes | Key | Null | Default | Extra  | Comment                  |
|-----------------|------------|------------|-----|------|---------|--------|--------------------------|
| [eventEntry][1] | TINYINT | UNSIGNED   |     | NO   |         | Unique | Entry of the game event. |
| [season][2]     | TINYINT | UNSIGNED   |     | NO   |         | Unique | Arena season number      |

[1]: #evententry
[2]: #season

**Description of the fields**

### eventEntry

Entry of the event

### season

Arena season number: 1 - 9
