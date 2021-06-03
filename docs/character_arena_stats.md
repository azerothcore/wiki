# character\_arena\_stats

[<-Back-to:Characters](database-characters.md)

**The \`character\_arena\_stats\` table**

This table holds information about character's matchmaker rating in all team types.

**Structure**

| Field                 | Type        | Attributes | Key | Null | Default | Extra | Comment |
|-----------------------|-------------|------------|-----|------|---------|-------|---------|
| [guid][1]             | INT     | SIGNED     | PRI | NO   |         |       |         |
| [slot][2]             | TINYINT  | SIGNED     | PRI | NO   |         |       |         |
| [matchmakerRating][3] | SMALLINT | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #slot
[3]: #matchmakerrating

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### slot

Arena slot index:

| Value | Description |
|-------|-------------|
| 0     | 2v2         |
| 1     | 3v3         |
| 2     | 5v5         |

### matchmakerRating

Player's matchmaker rating
