# guild\_eventlog

[<-Back-to:Characters](database-characters)

**The \`guild\_eventlog\` table**

Logs guild events. The entries are shown in the guild log in game.

**Table: guild\_eventlog's Structure**

| Field                       | Type    |          | Null | Key | Default | Extra | Comment                                     |
| :-------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------ |
| [guildid](#guildid)         | INT     | UNSIGNED | NO   | PRI |         |       | Guild Identificator                         |
| [LogGuid](#logguid)         | INT     | UNSIGNED | NO   | PRI |         |       | Log record identificator - auxiliary column |
| [EventType](#eventtype)     | TINYINT | UNSIGNED | NO   |     |         |       | Event type                                  |
| [PlayerGuid1](#playerguid1) | INT     | UNSIGNED | NO   | MUL |         |       | Player 1                                    |
| [PlayerGuid2](#playerguid2) | INT     | UNSIGNED | NO   | MUL |         |       | Player 2                                    |
| [NewRank](#newrank)         | TINYINT | UNSIGNED | NO   |     |         |       | New rank(in case promotion/demotion)        |
| [TimeStamp](#timestamp)     | INT     | UNSIGNED | NO   |     |         |       | Event UNIX time                             |

**Description of the table's fields**

### guildid

Guild Identificator.

### LogGuid

Log record identificator - auxiliary column.

### EventType

| Value | Description                         |
| ----- | ----------------------------------- |
| 1     | GUILD\_EVENT\_LOG\_INVITE\_PLAYER   |
| 2     | GUILD\_EVENT\_LOG\_JOIN\_GUILD      |
| 3     | GUILD\_EVENT\_LOG\_PROMOTE\_PLAYER  |
| 4     | GUILD\_EVENT\_LOG\_DEMOTE\_PLAYER   |
| 5     | GUILD\_EVENT\_LOG\_UNINVITE\_PLAYER |
| 6     | GUILD\_EVENT\_LOG\_LEAVE\_GUILD     |

### PlayerGuid1

GUID of Player1.

### PlayerGuid2

GUID of Player2.

### NewRank

New rank (in case of promotion/demotion).

### timestamp

Event UNIX time.
