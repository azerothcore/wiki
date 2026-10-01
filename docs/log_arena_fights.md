# log\_arena\_fights

[<-Back-to:Characters](database-characters)

**The \`log\_arena\_fights\` table**

**Table Structure**

| Field                 | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [fight_id][1]         | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [time][2]             | DATETIME | SIGNED     |     | NO   |         |       |         |
| [type][3]             | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [duration][4]         | INT      | UNSIGNED   |     | NO   |         |       |         |
| [winner][5]           | INT      | UNSIGNED   |     | NO   |         |       |         |
| [loser][6]            | INT      | UNSIGNED   |     | NO   |         |       |         |
| [winner_tr][7]        | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [winner_mmr][8]       | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [winner_tr_change][9] | SMALLINT | SIGNED     |     | NO   |         |       |         |
| [loser_tr][10]        | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [loser_mmr][11]       | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [loser_tr_change][12] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [currOnline][13]      | INT      | SIGNED     |     | NO   | 0       |       |         |

[1]: #fightid
[2]: #time
[3]: #type
[4]: #duration
[5]: #winner
[6]: #loser
[7]: #winnertr
[8]: #winnermmr
[9]: #winnertrchange
[10]: #losertr
[11]: #losermmr
[12]: #losertrchange
[13]: #curronline

**Description of the fields**

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
