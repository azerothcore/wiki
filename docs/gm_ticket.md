# gm_ticket

[<-Back-to:Characters](database-characters.md)

## The `gm_tickets` table

This table stores all tickets.

Note: do not insert directly into most of these columns, else the client won't update the ticket status until table reload and a logout.

## Structure

| Field                  | Type        | Attributes | Key | Null | Default | Extra          | Comment                                    |
|------------------------|-------------|------------|-----|------|---------|----------------|--------------------------------------------|
| [Id][1]                | int(10)     | signed     | PRI | NO   |         | Auto increment |                                            |
| [type][2]              | tinyint(3)  | unsigned   |     | NO   |         |                | 0 open, 1 closed, 2 character deleted      |
| [playerGuid][3]        | int(10)     | unsigned   |     | NO   |         |                | Global Unique Identifier of ticket creator |
| [name][4]              | VARCHAR(12) |            |     | NO   |         |                | Name of ticket creator                     |
| [description][5]       | text        |            |     | NO   |         |                |                                            |
| [createtime][6]        | int(10)     | unsigned   |     | NO   |         |                |                                            |
| [mapId][7]             | SMALLINT(5) | unsigned   |     | NO   |         |                |                                            |
| [posX][8]              | FLOAT       | signed     |     | NO   |         |                |                                            |
| [posY][9]              | FLOAT       | signed     |     | NO   |         |                |                                            |
| [posZ][10]             | FLOAT       | signed     |     | NO   |         |                |                                            |
| [lastModifiedTime][11] | int(10)     | signed     |     | NO   |         |                |                                            |
| [closedBy][12]         | int(10)     | signed     |     | NO   |         |                |                                            |
| [assignedTo][13]       | int(10)     | unsigned   |     | NO   |         |                | GUID of admin to whom ticket is assigned   |
| [comment][14]          | text        |            |     | NO   |         |                |                                            |
| [response][15]         | text        |            |     | NO   |         |                |                                            |
| [completed][16]        | tinyint(3)  | unsigned   |     | NO   |         |                |                                            |
| [escalated][17]        | tinyint(3)  | unsigned   |     | NO   |         |                |                                            |
| [viewed][18]           | tinyint(3)  | unsigned   |     | NO   |         |                |                                            |
| [needMoreHelp][19]     | tinyint(3)  | unsigned   |     | NO   |         |                |                                            |
| [resolvedBy][20]       | int(10)     | unsigned   |     | NO   |         |                | GUID of GM who resolved the ticket         |

[1]: #id
[2]: #type
[3]: #playerguid
[4]: #name
[5]: #description
[6]: #createtime
[7]: #mapid
[8]: #posx
[9]: #posy
[10]: #posz
[11]: #lastmodifiedtime
[12]: #closedby
[13]: #assignedto
[14]: #comment
[15]: #response
[16]: #completed
[17]: #escalated
[18]: #viewed
[19]: #needmorehelp
[20]: #resolvedby

**Description of the fields**

### Id

The ticket global unique identifier. This number must be unique and is the best way to identify separate tickets.

### type

Type of ticket. Variables: 
- 0 = open
- 1 = closed
- 2 = character deleted.

### playerGuid

Player's GUID. See characters.guid

### name

The name of the character who created that ticket

### description

The content of the ticket

### createTime

The creation time of the ticket as linux TIMESTAMP

### mapId

Map where ticket has ben created. See Map.dbc

### posX

Position X Where ticket has ben created.

### posY

Position Y Where ticket has ben created.

### posZ

Position Z Where ticket has ben created.

### lastModifiedTime

The time when the ticket was closed or deleted by the issuer as linux TIMESTAMP

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

Requests further GM interaction on a ticket to which a GM has already responded. Basically means "has a new ticket"

### resolvedBy

- 0 = Open
- ~-1 = Resolved by Console~ (not supported on azerothcore yet cause of datatype in DB)
- > 0 = Character guid of the GM who resolved it (by closing the ticket or by completing the ticket)
