# arena\_team

[<-Back-to:Characters](database-characters)

**The \`arena\_team\` table**

This table holds the main ArenaTeam information. All created teams or all teams in the process of being created have a record in this table.

**Table: arena\_team's Structure**

| Field                               | Type        |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [arenaTeamId](#arenateamid)         | INT         | UNSIGNED | NO   | PRI | 0       |       |         |
| [name](#name)                       | VARCHAR(24) |          | NO   |     |         |       |         |
| [captainGuid](#captainguid)         | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [type](#type)                       | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [rating](#rating)                   | SMALLINT    | UNSIGNED | NO   |     | 0       |       |         |
| [seasonGames](#seasongames)         | SMALLINT    | UNSIGNED | NO   |     | 0       |       |         |
| [seasonWins](#seasonwins)           | SMALLINT    | UNSIGNED | NO   |     | 0       |       |         |
| [weekGames](#weekgames)             | SMALLINT    | UNSIGNED | NO   |     | 0       |       |         |
| [weekWins](#weekwins)               | SMALLINT    | UNSIGNED | NO   |     | 0       |       |         |
| [rank](#rank)                       | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [backgroundColor](#backgroundcolor) | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [emblemStyle](#emblemstyle)         | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [emblemColor](#emblemcolor)         | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [borderStyle](#borderstyle)         | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [borderColor](#bordercolor)         | INT         | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### arenaTeamId

The ID of the ArenaTeam. This number is unique to each team and is the main method to identify a team.

### name

Name of the Arena team.

### captainGuid

The GUID of the character who created the ArenaTeam. See [characters.guid](characters#guid).

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

Team-tabard BackgroundColor (same as guild-tabard).

### emblemStyle

Team-tabard Emblem (same as guild-tabard).

### emblemColor

Team-tabard emblemColor (same as guild-tabard).

### borderStyle

Team-tabard Bordertype (same as guild-tabard).

### borderColor

Team-tabard borderColor (same as guild-tabard).
