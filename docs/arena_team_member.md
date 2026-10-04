# arena\_team\_member

[<-Back-to:Characters](database-characters)

**The \`arena\_team\_member\` table**

This table holds arena info about specific team members. All arena\_team members have a record in this table.

**Table: arena\_team\_member's Structure**

| Field                             | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [arenaTeamId](#arenateamid)       | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [guid](#guid)                     | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [weekGames](#weekgames)           | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [weekWins](#weekwins)             | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [seasonGames](#seasongames)       | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [seasonWins](#seasonwins)         | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [personalRating](#personalrating) | SMALLINT |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### arenaTeamId

ID of arena team. See [arena\_team#arenateamid].

### guid

Player's GUID. See [characters.guid](characters#guid).

### weekGames

Number of games played this **week**.

### weekWins

Number of games won this **week**.

### seasonGames

Number of games played this **season**.

### seasonWins

Number of games won this **season**.

### personalrating

The player's personal arena rating.
