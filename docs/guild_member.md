# guild\_member

[<-Back-to:Characters](database-characters)

**The \`guild\_member\` table**

This table holds information on the members of all guilds, their ranks in the guild, and any notes made by them or by guild officers.

**Table Structure**

| Field        | Type        | Attributes | Key    | Null | Default | Extra | Comment             |
| ------------ | ----------- | ---------- | ------ | ---- | ------- | ----- | ------------------- |
| [guildid][1] | INT         | UNSIGNED   |        | NO   |         |       | Guild Identificator |
| [guid][2]    | INT         | UNSIGNED   | Unique | NO   |         |       |                     |
| [rank][3]    | TINYINT     | UNSIGNED   |        | NO   |         |       |                     |
| [pnote][4]   | VARCHAR(31) | SIGNED     |        | NO   |         |       |                     |
| [offnote][5] | VARCHAR(31) | SIGNED     |        | NO   |         |       |                     |

[1]: #guildid
[2]: #guid
[3]: #rank
[4]: #pnote
[5]: #offnote

**Description of the fields**

### guildid

The ID of the guild that the member is a part of. See [guild.guildid](guild#guildid).

### guid

The GUID of the player. See [characters.guid](characters#guid).

### rank

The rank that the player has in the guild. See [guild\_rank.rid](Guild_rank#rid).

### pnote

The note set by the player that can be read by everyone.

### offnote

The note set by officers in the guild that can only be read by other officers of the guild.
