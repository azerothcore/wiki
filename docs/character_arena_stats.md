# character\_arena\_stats

[<-Back-to:Characters](database-characters)

**The \`character\_arena\_stats\` table**

This table holds information about character's matchmaker rating in all team types.

**Table Structure**

| Field                 | Type        | Attributes | Key | Null | Default | Extra | Comment |
| --------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]             | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [slot][2]             | TINYINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [matchmakerRating][3] | SMALLINT    | UNSIGNED   |     | NO   |         |       |         |
| [maxMMR][4]           | SMALLINT    | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #slot
[3]: #matchmakerrating
[4]: #maxmmr

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### slot

Arena slot index:

| Value | Description |
| ----- | ----------- |
| 0     | 2v2         |
| 1     | 3v3         |
| 2     | 5v5         |

### matchmakerRating

Player's matchmaker rating.

### maxMMR

`field-no-description|4`
