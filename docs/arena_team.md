# arena\_team

[<-Back-to:Characters](database-characters.md)

**The \`arena\_team\` table**

This table holds the main ArenaTeam information. All created teams or all teams in the process of being created have a record in this table.

**Structure**

| Field                 | Type        | Attributes | Key | Null | Default | Extra  | Comment |
|-----------------------|-------------|------------|-----|------|---------|--------|---------|
| [arenaTeamId][1]      | INT(10)     | UNSIGNED   | PRI | NO   |         | Unique |         |
| [name][2]             | VARCHAR(24) |            |     | NO   |         |        |         |
| [captainGuid][3]      | INT(10)     | UNSIGNED   |     | NO   |         |        |         |
| [type][4]             | TINYINT(3)  | UNSIGNED   |     | NO   |         |        |         |
| [rating][5]           | SMALLINT(5) | UNSIGNED   |     | NO   |         |        |         |
| [seasonGames][6]      | SMALLINT(5) | UNSIGNED   |     | NO   |         |        |         |
| [seasonWins][7]       | SMALLINT(5) | UNSIGNED   |     | NO   |         |        |         |
| [weekGames][8]        | SMALLINT(5) | UNSIGNED   |     | NO   |         |        |         |
| [weekWins][9]         | SMALLINT(5) | UNSIGNED   |     | NO   |         |        |         |
| [rank][10]            | INT(10)     | UNSIGNED   |     | NO   |         |        |         |
| [BackgroundColor][11] | INT(10)     | UNSIGNED   |     | NO   |         |        |         |
| [EmblemStyle][12]     | TINYINT(3)  | UNSIGNED   |     | NO   |         |        |         |
| [EmblemColor][13]     | INT(10)     | UNSIGNED   |     | NO   |         |        |         |
| [BorderStyle][14]     | TINYINT(3)  | UNSIGNED   |     | NO   |         |        |         |
| [BorderColor][15]     | INT(10)     | UNSIGNED   |     | NO   |         |        |         |

[1]: #arenateamid
[2]: #name
[3]: #captainguid
[4]: #type
[5]: #rating
[6]: #seasongames
[7]: #seasonwins
[8]: #weekgames
[9]: #weekwins
[10]: #rank
[11]: #backgroundcolor
[12]: #emblemstyle
[13]: #emblemcolor
[14]: #borderstyle
[15]: #bordercolor

**Description of the fields**

### arenaTeamId

The ID of the ArenaTeam. This number is unique to each team and is the main method to identify a team.1

### name

Name of the Arena team

### captainGuid

The GUID of the character who created the ArenaTeam. See [characters.guid](2129969.html#characters(table)-guid)

### type

Defines the ArenaType:

- 2 – 2vs2 Team
- 3 – 3vs3 Team
- 5 – 5vs5 Team

### rating

Rating of arena team.

### seasonGames

Number of games played this **season**.

### seasonWins

Number of games won this **season**.

### weekGames

Number of games played this **week**.

### weekWins

Number of games won this **week**.

### rank

Rank of teams in the competition by rating.

### BackgroundColor

Team-tabard BackgroundColor (same as guild-tabard)

### EmblemStyle

Team-tabard Emblem (same as guild-tabard)

### EmblemColor

Team-tabard EmblemColor (same as guild-tabard)

### BorderStyle

Team-tabard Bordertype (same as guild-tabard)

### BorderColor

Team-tabard BorderColor (same as guild-tabard)
