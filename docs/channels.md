# channels

[<-Back-to:Characters](database-characters)

**The \`channels\` table**

Information and settings for ingame, player-based chat channels (not affecting the default system channels).

**Table Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [channelId][1]  | INT          | SIGNED     | PRI | NO   |         | AUTO_INCREMENT |         |
| [name][2]       | VARCHAR(128) | SIGNED     |     | NO   |         |                |         |
| [team][3]       | INT          | UNSIGNED   |     | NO   |         |                |         |
| [announce][4]   | TINYINT      | UNSIGNED   |     | NO   | 1       |                |         |
| [ownership][5]  | TINYINT      | UNSIGNED   |     | NO   | 1       |                |         |
| [password][6]   | VARCHAR(32)  | SIGNED     |     | YES  |         |                |         |
| [lastUsed][7]   | INT          | UNSIGNED   |     | NO   |         |                |         |

[1]: #channelid
[2]: #name
[3]: #team
[4]: #announce
[5]: #ownership
[6]: #password
[7]: #lastused

**Description of the fields**

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
