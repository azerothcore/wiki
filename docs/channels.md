# channels

[<-Back-to:Characters](database-characters)

**The \`channels\` table**

Information and settings for ingame, player-based chat channels (not affecting the default system channels).

**Table: channels's Structure**

| Field                   | Type         |          | Null | Key | Default | Extra          | Comment |
| :---------------------- | :----------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [channelId](#channelid) | INT          | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [name](#name)           | VARCHAR(128) |          | NO   |     |         |                |         |
| [team](#team)           | INT          | UNSIGNED | NO   |     |         |                |         |
| [announce](#announce)   | TINYINT      | UNSIGNED | NO   |     | 1       |                |         |
| [ownership](#ownership) | TINYINT      | UNSIGNED | NO   |     | 1       |                |         |
| [password](#password)   | VARCHAR(32)  |          | YES  |     | NULL    |                |         |
| [lastUsed](#lastused)   | INT          | UNSIGNED | NO   |     |         |                |         |

**Description of the table's fields**

### channelId

The id of channel.

### name

Name of the channel.

### team

Allow access to channel from specified player faction ID.

For multirace channels, two (or more) separate entries must exist with the EXACT same settings for all fields apart from this (it needs a different `team id`).

| Faction  | Value |
| -------- | ----- |
| Horde    | 67    |
| Alliance | 469   |

### announce

Channel announce (0/1).

- 0 = Channel join/part actions will not be sent
- 1 = Channel join/part actions will be sent

### ownership

Channel ownership.

- 0 = No one will ever be an owner.
- 1 = Ownership is the first person in the channel.

### password

Channel password.

Empty, or a standard string-based password (no spaces allowed).

### lastUsed

Used for automated cleaning of unused channels from database. Time is in unixtime.
