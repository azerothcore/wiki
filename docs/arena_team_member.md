# arena\_team\_member

[<-Back-to:Characters](database-characters.md)

**The \`arena\_team\_member\` table**

This table holds arena info about specific team members. All arena\_team members have a record in this table.

**Structure**

| Field               | Type        | Attributes | Key | Null | Default | Extra | Comment |
|---------------------|-------------|------------|-----|------|---------|-------|---------|
| [arenaTeamId][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [guid][2]           | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [personalRating][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [weekGames][4]      | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [weekWins][5]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonGames][6]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonWins][7]     | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #arenateamid
[2]: #guid
[3]: #personalrating
[4]: #weekgames
[5]: #weekwins
[6]: #seasongames
[7]: #seasonwins

**Description of the fields**

### arenaTeamId

ID of arena team. See Team Id

### guid

Player's GUID. See characters.guid

### weekGames

Number of games played this **week**.

### weekWins

Number of games won this **week**.

### seasonGames

Number of games played this **season**.

### seasonWins

Number of games won this **season**.
