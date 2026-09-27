# log\_arena\_memberstats

[<-Back-to:Characters](database-characters)

**The \`log\_arena\_memberstats\` table**

**Table Structure**

| Field          | Type     | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [fight_id][1]  | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [member_id][2] | TINYINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [name][3]      | CHAR(20) | SIGNED     |     | NO   |         |       |         |
| [guid][4]      | INT      | UNSIGNED   |     | NO   |         |       |         |
| [team][5]      | INT      | UNSIGNED   |     | NO   |         |       |         |
| [account][6]   | INT      | UNSIGNED   |     | NO   |         |       |         |
| [ip][7]        | CHAR(15) | SIGNED     |     | NO   |         |       |         |
| [damage][8]    | INT      | UNSIGNED   |     | NO   |         |       |         |
| [heal][9]      | INT      | UNSIGNED   |     | NO   |         |       |         |
| [kblows][10]   | INT      | UNSIGNED   |     | NO   |         |       |         |

[1]: #fightid
[2]: #memberid
[3]: #name
[4]: #guid
[5]: #team
[6]: #account
[7]: #ip
[8]: #damage
[9]: #heal
[10]: #kblows

**Description of the fields**

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
