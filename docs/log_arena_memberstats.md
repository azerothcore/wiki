# log\_arena\_memberstats

[<-Back-to:Characters](database-characters)

**The \`log\_arena\_memberstats\` table**

Logs the result of each player in the arena matches recorded in [log_arena_fights](log_arena_fights).

**Table: log\_arena\_memberstats's Structure**

| Field                  | Type     |          | Null | Key | Default | Extra | Comment |
| :--------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [fight_id](#fightid)   | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [member_id](#memberid) | TINYINT  | UNSIGNED | NO   | PRI |         |       |         |
| [name](#name)          | CHAR(20) |          | NO   |     |         |       |         |
| [guid](#guid)          | INT      | UNSIGNED | NO   |     |         |       |         |
| [team](#team)          | INT      | UNSIGNED | NO   |     |         |       |         |
| [account](#account)    | INT      | UNSIGNED | NO   |     |         |       |         |
| [ip](#ip)              | CHAR(15) |          | NO   |     |         |       |         |
| [damage](#damage)      | INT      | UNSIGNED | NO   |     |         |       |         |
| [heal](#heal)          | INT      | UNSIGNED | NO   |     |         |       |         |
| [kblows](#kblows)      | INT      | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### fight\_id

The arena match. See [log\_arena\_fights.fight\_id](log_arena_fights#fightid).

### member\_id

Number of the player in the match, starting at 1.

### name

Name of the character.

### guid

GUID of the character. See [characters.guid](characters#guid).

### team

ID of the arena team the player fought for. See [arena\_team.arenaTeamId](arena_team#arenateamid).

### account

Account of the player. See [account.id](account#id).

### ip

IP of the player.

### damage

Damage the player did in the match.

### heal

Healing the player did in the match.

### kblows

Killing blows the player got in the match.
