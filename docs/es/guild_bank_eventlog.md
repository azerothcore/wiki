# guild\_bank\_eventlog

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../guild_bank_eventlog) [Spanish :es:](guild_bank_eventlog)

**Tabla \`guild\_bank\_eventlog\`**

**Estructura**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment                                     |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------- |
| [guildid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Guild Identificator                         |
| [LogGuid][2]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Log record identificator - auxiliary column |
| [TabId][3]          | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       | Guild bank TabId                            |
| [EventType][4]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       | Event type                                  |
| [PlayerGuid][5]     | INT      | UNSIGNED   |     | NO   | 0       |       |                                             |
| [ItemOrMoney][6]    | INT      | UNSIGNED   |     | NO   | 0       |       |                                             |
| [ItemStackCount][7] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                             |
| [DestTabId][8]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       | Destination Tab Id                          |
| [TimeStamp][9]      | INT      | UNSIGNED   |     | NO   | 0       |       | Event UNIX time                             |

[1]: #guildid
[2]: #logguid
[3]: #tabid
[4]: #eventtype
[5]: #playerguid
[6]: #itemormoney
[7]: #itemstackcount
[8]: #desttabid
[9]: #timestamp

**Descripción de los campos**

### guildid

Identificador de la hermandad.

### LogGuid

Identificación del registro de Log - columna auxiliar.

### TabId

TabId del banco de la hermandad.

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

GUID del personaje.

### ItemOrMoney

`campo-sin-descripción|6`

### ItemStackCount

`campo-sin-descripción|7`

### DestTabId

ID de la pestaña de destino.

### TimeStamp

Hora del envento en UNIX. 
