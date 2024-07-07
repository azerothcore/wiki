# guild\_eventlog

[<-Back-to:Characters](database-characters)

**The \`guild\_eventlog\` table**

**Table Structure**

| Field            | Type    | Attributes | Key | Null | Default | Extra | Comment                                     |
| ---------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------- |
| [guildid][1]     | INT     | UNSIGNED   | PRI | NO   |         |       | Guild Identificator                         |
| [LogGuid][2]     | INT     | UNSIGNED   | PRI | NO   |         |       | Log record identificator - auxiliary column |
| [EventType][3]   | TINYINT | UNSIGNED   |     | NO   |         |       | Event type                                  |
| [PlayerGuid1][4] | INT     | UNSIGNED   |     | NO   |         |       | Player 1                                    |
| [PlayerGuid2][5] | INT     | UNSIGNED   |     | NO   |         |       | Player 2                                    |
| [NewRank][6]     | TINYINT | UNSIGNED   |     | NO   |         |       | New rank(in case promotion/demotion)        |
| [timestamp][7]   | BIGINT  | UNSIGNED   |     | NO   |         |       | Event UNIX time                             |

[1]: #guildid
[2]: #logguid
[3]: #eventtype
[4]: #playerguid1
[5]: #playerguid2
[6]: #newrank
[7]: #timestamp

**Description of the fields**

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
