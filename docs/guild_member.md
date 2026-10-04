# guild\_member

[<-Back-to:Characters](database-characters)

**The \`guild\_member\` table**

This table holds information on the members of all guilds, their ranks in the guild, and any notes made by them or by guild officers.

**Table: guild\_member's Structure**

| Field               | Type        |          | Null | Key | Default | Extra | Comment             |
| :------------------ | :---------- | :------- | :--: | :-: | :-----: | :---: | :------------------ |
| [guildid](#guildid) | INT         | UNSIGNED | NO   | MUL |         |       | Guild Identificator |
| [guid](#guid)       | INT         | UNSIGNED | NO   | UNI |         |       |                     |
| [rank](#rank)       | TINYINT     | UNSIGNED | NO   |     |         |       |                     |
| [pnote](#pnote)     | VARCHAR(31) |          | NO   |     | ''      |       |                     |
| [offnote](#offnote) | VARCHAR(31) |          | NO   |     | ''      |       |                     |

**Description of the table's fields**

### guildid

The ID of the guild that the member is a part of. See [guild.guildid](guild#guildid).

### guid

The GUID of the player. See [characters.guid](characters#guid).

### rank

The rank that the player has in the guild. See [guild\_rank.rid](guild_rank#rid).

### pnote

The note set by the player that can be read by everyone.

### offnote

The note set by officers in the guild that can only be read by other officers of the guild.
