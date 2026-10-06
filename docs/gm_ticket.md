# gm\_ticket

[<-Back-to:Characters](database-characters)

**The \`gm\_ticket\` table**

This table stores all tickets.

Note: do not insert directly into most of these columns, else the client won't update the ticket status until table reload and a logout.

**Table: gm\_ticket's Structure**

| Field                                 | Type        |          | Null | Key | Default | Extra          | Comment                                    |
| :------------------------------------ | :---------- | :------- | :--: | :-: | :-----: | :------------: | :----------------------------------------- |
| [id](#id)                             | INT         | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |                                            |
| [type](#type)                         | TINYINT     | UNSIGNED | NO   |     | 0       |                | 0 open, 1 closed, 2 character deleted      |
| [playerGuid](#playerguid)             | INT         | UNSIGNED | NO   |     | 0       |                | Global Unique Identifier of ticket creator |
| [name](#name)                         | VARCHAR(12) |          | NO   |     |         |                | Name of ticket creator                     |
| [description](#description)           | TEXT        |          | NO   |     |         |                |                                            |
| [createTime](#createtime)             | INT         | UNSIGNED | NO   |     | 0       |                |                                            |
| [mapId](#mapid)                       | SMALLINT    | UNSIGNED | NO   |     | 0       |                |                                            |
| [posX](#posx)                         | FLOAT       |          | NO   |     | 0       |                |                                            |
| [posY](#posy)                         | FLOAT       |          | NO   |     | 0       |                |                                            |
| [posZ](#posz)                         | FLOAT       |          | NO   |     | 0       |                |                                            |
| [lastModifiedTime](#lastmodifiedtime) | INT         | UNSIGNED | NO   |     | 0       |                |                                            |
| [closedBy](#closedby)                 | INT         |          | NO   |     | 0       |                | -1 Closed by Console, >0 GUID of GM        |
| [assignedTo](#assignedto)             | INT         | UNSIGNED | NO   |     | 0       |                | GUID of admin to whom ticket is assigned   |
| [comment](#comment)                   | TEXT        |          | NO   |     |         |                |                                            |
| [response](#response)                 | TEXT        |          | NO   |     |         |                |                                            |
| [completed](#completed)               | TINYINT     | UNSIGNED | NO   |     | 0       |                |                                            |
| [escalated](#escalated)               | TINYINT     | UNSIGNED | NO   |     | 0       |                |                                            |
| [viewed](#viewed)                     | TINYINT     | UNSIGNED | NO   |     | 0       |                |                                            |
| [needMoreHelp](#needmorehelp)         | TINYINT     | UNSIGNED | NO   |     | 0       |                |                                            |
| [resolvedBy](#resolvedby)             | INT         |          | NO   |     | 0       |                | -1 Resolved by Console, >0 GUID of GM      |

**Description of the table's fields**

### Id

The ticket global unique identifier. This number must be unique and is the best way to identify separate tickets.

### type

Type of ticket. Variables: 
- 0 = open
- 1 = closed
- 2 = character deleted

### playerGuid

Player's GUID. See [characters.guid](characters#guid).

### name

The name of the character who created that ticket.

### description

The content of the ticket.

### createTime

The creation time of the ticket as linux timestamp.

### mapId

Map where ticket has ben created. See [Map.dbc](map).

### posX

Position X Where ticket has ben created.

### posY

Position Y Where ticket has ben created.

### posZ

Position Z Where ticket has ben created.

### lastModifiedTime

The time when the ticket was closed or deleted by the issuer as linux timestamp.

### closedBy

- 0 = Open
- ~-1 = Closed by Console~ (not implemented on azerothcore yet)
- > 0 = player who abandoned ticket or GM who closed ticket

### assignedTo

Specify account number of GameMaster that have this ticket assigned.

### comment

The comment to the ticket added with `.ticket comment`, only visible to game masters. If the command is used twice, it overwrites the previous comment.

### response

The string the GM inserted with `.ticket response` commands to answer the ticket before completing it. If the command is used twice, it appends the new answer at the end of the previous one.

### completed

- 0 = not completed
- 1 = completed (will inform the user and show what is in `response`)

### escalated

- 0 = ticket is not currently assigned to a gm
- 1 = ticket is assigned to a normal gm
- 2 = ticket has been escalated after completion (a GM is supposed to contact the player back) 

### viewed

- 0 = no one has viewed the ticket.
- > 0 = How many times the ticket has been viewed by GMs

### needMoreHelp

Requests further GM interaction on a ticket to which a GM has already responded. Basically means "has a new ticket".

### resolvedBy

- 0 = Open
- ~-1 = Resolved by Console~ (not supported on azerothcore yet cause of datatype in DB)
- > 0 = Character guid of the GM who resolved it (by closing the ticket or by completing the ticket)
