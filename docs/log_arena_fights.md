# log\_arena\_fights

[<-Back-to:Characters](database-characters)

**The \`log\_arena\_fights\` table**

Logs each arena match: time, type, duration, the two teams and their rating changes.

**Table: log\_arena\_fights's Structure**

| Field                               | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [fight_id](#fightid)                | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [time](#time)                       | DATETIME |          | NO   |     |         |       |         |
| [type](#type)                       | TINYINT  | UNSIGNED | NO   |     |         |       |         |
| [duration](#duration)               | INT      | UNSIGNED | NO   |     |         |       |         |
| [winner](#winner)                   | INT      | UNSIGNED | NO   |     |         |       |         |
| [loser](#loser)                     | INT      | UNSIGNED | NO   |     |         |       |         |
| [winner_tr](#winnertr)              | SMALLINT | UNSIGNED | NO   |     |         |       |         |
| [winner_mmr](#winnermmr)            | SMALLINT | UNSIGNED | NO   |     |         |       |         |
| [winner_tr_change](#winnertrchange) | SMALLINT |          | NO   |     |         |       |         |
| [loser_tr](#losertr)                | SMALLINT | UNSIGNED | NO   |     |         |       |         |
| [loser_mmr](#losermmr)              | SMALLINT | UNSIGNED | NO   |     |         |       |         |
| [loser_tr_change](#losertrchange)   | SMALLINT |          | NO   |     |         |       |         |
| [currOnline](#curronline)           | INT      | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### fight\_id

The unique ID of the arena match.

### time

The date and time the match ended.

### type

The arena type: 2 for 2v2, 3 for 3v3 and 5 for 5v5.

### duration

Length of the match in seconds, counted from when the gates opened.

### winner

ID of the winning arena team. See [arena\_team.arenaTeamId](arena_team#arenateamid).

### loser

ID of the losing arena team. See [arena\_team.arenaTeamId](arena_team#arenateamid).

### winner\_tr

Team rating of the winning team before the match.

### winner\_mmr

Matchmaker rating of the winning team before the match.

### winner\_tr\_change

How much the team rating of the winning team changed.

### loser\_tr

Team rating of the losing team before the match.

### loser\_mmr

Matchmaker rating of the losing team before the match.

### loser\_tr\_change

How much the team rating of the losing team changed.

### curronline

Number of players online on the server when the match ended.
