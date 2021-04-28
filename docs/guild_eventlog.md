# guild\_eventlog

[<-Back-to:Characters](database-characters.md)

**The \`guild\_eventlog\` table**

`table-no-description`

**Structure**

| Field            | Type       | Attributes | Key | Null | Default | Extra | Comment                                     |
|------------------|------------|------------|-----|------|---------|-------|---------------------------------------------|
| [guildid][1]     | INT    | SIGNED     | PRI | NO   | NULL    |       | Guild Identificator                         |
| [LogGuid][2]     | INT    | SIGNED     | PRI | NO   | NULL    |       | Log record identificator - auxiliary column |
| [EventType][3]   | TINYINT | SIGNED     |     | NO   | NULL    |       | Event type                                  |
| [PlayerGuid1][4] | INT    | SIGNED     |     | NO   | NULL    |       | Player 1                                    |
| [PlayerGuid2][5] | INT    | SIGNED     |     | NO   | NULL    |       | Player 2                                    |
| [NewRank][6]     | TINYINT | SIGNED     |     | NO   | NULL    |       | New rank(in case promotion/demotion)        |
| [timestamp][7]   | BIGINT | SIGNED     |     | NO   | NULL    |       | Event UNIX time                             |

[1]: #guildid
[2]: #logguid
[3]: #eventtype
[4]: #playerguid1
[5]: #playerguid2
[6]: #newrank
[7]: #timestamp

**Description of the fields**

### guildid

`Guild Identificator`

### LogGuid

`Log record identificator - auxiliary column`

### EventType

| Value | Description                         |
|-------|-------------------------------------|
| 1     | GUILD\_EVENT\_LOG\_INVITE\_PLAYER   |
| 2     | GUILD\_EVENT\_LOG\_JOIN\_GUILD      |
| 3     | GUILD\_EVENT\_LOG\_PROMOTE\_PLAYER  |
| 4     | GUILD\_EVENT\_LOG\_DEMOTE\_PLAYER   |
| 5     | GUILD\_EVENT\_LOG\_UNINVITE\_PLAYER |
| 6     | GUILD\_EVENT\_LOG\_LEAVE\_GUILD     |

### PlayerGuid1

`GUID of Player1`

### PlayerGuid2

`GUID of Player2`

### NewRank

`New rank (in case of promotion/demotion)`

### timestamp

`Event UNIX time`
