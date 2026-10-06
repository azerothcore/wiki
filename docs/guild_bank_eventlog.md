# guild\_bank\_eventlog

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_eventlog\` table**

Logs player actions on the guild bank. The entries are shown in the guild bank log in game.

**Table: guild\_bank\_eventlog's Structure**

| Field                             | Type     |          | Null | Key | Default | Extra | Comment                                     |
| :-------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------ |
| [guildid](#guildid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Guild Identificator                         |
| [LogGuid](#logguid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Log record identificator - auxiliary column |
| [TabId](#tabid)                   | TINYINT  | UNSIGNED | NO   | PRI | 0       |       | Guild bank TabId                            |
| [EventType](#eventtype)           | TINYINT  | UNSIGNED | NO   |     | 0       |       | Event type                                  |
| [PlayerGuid](#playerguid)         | INT      | UNSIGNED | NO   | MUL | 0       |       |                                             |
| [ItemOrMoney](#itemormoney)       | INT      | UNSIGNED | NO   |     | 0       |       |                                             |
| [ItemStackCount](#itemstackcount) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                             |
| [DestTabId](#desttabid)           | TINYINT  | UNSIGNED | NO   |     | 0       |       | Destination Tab Id                          |
| [TimeStamp](#timestamp)           | INT      | UNSIGNED | NO   |     | 0       |       | Event UNIX time                             |

**Description of the table's fields**

### guildid

Guild Identificator.

### LogGuid

Log record identification - auxiliary column.

### TabId

Guild bank TabId.

### EventType

| Value | Description                       |
| ----- | --------------------------------- |
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

GUID of the Player.

### ItemOrMoney

The item entry for item events, or the amount of money in copper for money events.

### ItemStackCount

The number of items for item events.

### DestTabId

Destination Tab Id.

### TimeStamp

Event UNIX time.
