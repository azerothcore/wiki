# channels

[<-Back-to:Characters](database-characters.md)

# Table: channels

Information and settings for ingame, player-based chat channels (not affecting the default system channels)

## Structure

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|--------------|------------|-----|------|---------|-------|---------|
| [name][1]       | VARCHAR(128) | SIGNED     | PRI | NO   |         |       |         |
| [team][2]       | INT(10)      | UNSIGNED   | PRI | NO   |         |       |         |
| [announce][3]   | TINYINT(3)   | UNSIGNED   |     | NO   | 1       |       |         |
| [ownership][4]  | TINYINT(3)   | UNSIGNED   |     | NO   | 1       |       |         |
| [password][5]   | VARCHAR(32)  | SIGNED     |     | YES  | NULL    |       |         |
| [bannedList][6] | text         | SIGNED     |     | YES  |         |       |         |
| [lastUsed][7]   | INT(10)      | UNSIGNED   |     | NO   |         |       |         |

[1]: #name
[2]: #team
[3]: #announce
[4]: #ownership
[5]: #password
[6]: #bannedlist
[7]: #lastused

## Description of the fields

### name

**Channel name**

Name of the channel

### team

**team id** Allow access to channel from specified player faction ID

For multirace channels, two (or more) separate entries must exist with the EXACT same settings for all fields apart from this (it needs a different **team id**)

| Faction  | Value |
|----------|-------|
| Horde    | 67    |
| Alliance | 469   |

### announce

**Channel announce (0/1)**

- 0 = Channel join/part actions will not be sent
- 1 = Channel join/part actions will be sent

### ownership

**Channel ownership (0/1)**

- 0 = No one will ever be an owner.
- 1 = Ownership is the first person in the channel.

### password

**Channel password**

Empty, or a standard string-based password (no spaces allowed)

### bannedList (NOT IMPLEMENTED FOR NOW)

**Channel banlist**
List of banned player names, separated by spaces

### lastUsed

Used for automated cleaning of unused channels from database. Time is in unixtime.
