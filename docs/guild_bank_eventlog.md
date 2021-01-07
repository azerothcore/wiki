# guild\_bank\_eventlog

[<-Back-to:Characters](database-characters.md)

**The \`guild\_bank\_eventlog\` table**

`table-no-description`

**Structure**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment                                     |
|---------------------|------------|------------|-----|------|---------|-------|---------------------------------------------|
| [guildid][1]        | int(11)    | unsigned   | PRI | NO   | 0       |       | Guild Identificator                         |
| [LogGuid][2]        | int(11)    | unsigned   | PRI | NO   | 0       |       | Log record identificator - auxiliary column |
| [TabID][3]          | tinyint(3) | unsigned   | PRI | NO   | 0       |       | Guild bank TabId                            |
| [EventType][4]      | tinyint(3) | unsigned   |     | NO   | 0       |       | Event type                                  |
| [PlayerGuid][5]     | int(11)    | unsigned   |     | NO   | 0       |       |                                             |
| [ItemOrMoney][6]    | int(11)    | unsigned   |     | NO   | 0       |       |                                             |
| [ItemStackCount][7] | tinyint(3) | unsigned   |     | NO   | 0       |       |                                             |
| [DestTabId][8]      | tinyint(1) | unsigned   |     | NO   | 0       |       | Destination Tab Id                          |
| [TimeStamp][9]      | bigint(20) | unsigned   |     | NO   | 0       |       | Event UNIX time                             |

[1]: #guildid
[2]: #logguid
[3]: #tabid
[4]: #eventtype
[5]: #playerguid
[6]: #itemormoney
[7]: #itemstackcount
[8]: #desttabid
[9]: #timestamp

**Description of the fields**

### guildid

`Guild Identificator`

### LogGuid

`Log record identificator - auxiliary column`

### TabId

`Guild bank TabId`

### EventType

| Value | Description                       |
|-------|-----------------------------------|
| 1     | GUILD\_BANK\_LOG\_DEPOSIT\_ITEM   |
| 2     | GUILD\_BANK\_LOG\_WITHDRAW\_ITEM  |
| 3     | GUILD\_BANK\_LOG\_MOVE\_ITEM      |
| 4     | GUILD\_BANK\_LOG\_DEPOSIT\_MONEY  |
| 5     | GUILD\_BANK\_LOG\_WITHDRAW\_MONEY |
| 6     | GUILD\_BANK\_LOG\_REPAIR\_MONEY   |
| 7     | GUILD\_BANK\_LOG\_MOVE\_ITEM2     |
| 8     | GUILD\_BANK\_LOG\_UNK1            |
| 9     | GUILD\_BANK\_LOG\_BUY\_SLOT       |

### PlayerGuid

`GUID of the Player`

### ItemOrMoney

`field-no-description|6`

### ItemStackCount

`field-no-description|7`

### DestTabId

`Destination Tab Id`

### TimeStamp

`Event UNIX time`
