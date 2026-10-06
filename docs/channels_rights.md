# channels\_rights

[<-Back-to:Characters](database-characters)

**The \`channels\_rights\` table**

Holds settings applied to chat channels by name: flags, speak delay, join message, delay message and moderators.

**Table: channels\_rights's Structure**

| Field                         | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [name](#name)                 | VARCHAR(128) |          | NO   | PRI |         |       |         |
| [flags](#flags)               | INT          | UNSIGNED | NO   |     |         |       |         |
| [speakdelay](#speakdelay)     | INT          | UNSIGNED | NO   |     |         |       |         |
| [joinmessage](#joinmessage)   | VARCHAR(255) |          | NO   |     | ''      |       |         |
| [delaymessage](#delaymessage) | VARCHAR(255) |          | NO   |     | ''      |       |         |
| [moderators](#moderators)     | TEXT         |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### name

Name of the channel the rights apply to.

### flags

| Value | Hex      | Flag                                 | Comment                                      |
| :---- | :------: | :----------------------------------- | :------------------------------------------- |
| 1     | `0x0001` | CHANNEL_RIGHT_FORCE_NO_ANNOUNCEMENTS | Join and leave announcements are turned off. |
| 2     | `0x0002` | CHANNEL_RIGHT_FORCE_ANNOUNCEMENTS    | Join and leave announcements are turned on.  |
| 4     | `0x0004` | CHANNEL_RIGHT_NO_OWNERSHIP           | The channel has no owner.                    |
| 8     | `0x0008` | CHANNEL_RIGHT_CANT_SPEAK             | Only moderators can speak.                   |
| 16    | `0x0010` | CHANNEL_RIGHT_CANT_BAN               | Nobody can be banned from the channel.       |
| 32    | `0x0020` | CHANNEL_RIGHT_CANT_KICK              | Nobody can be kicked from the channel.       |
| 64    | `0x0040` | CHANNEL_RIGHT_CANT_MUTE              | Nobody can be muted in the channel.          |
| 128   | `0x0080` | CHANNEL_RIGHT_CANT_CHANGE_PASSWORD   | The password can not be changed.             |
| 256   | `0x0100` | CHANNEL_RIGHT_DONT_PRESERVE          | The channel is not saved to the database.    |

### speakdelay

Loaded by the core, but not used.

### joinmessage

Message sent to a player when they join the channel.

### delaymessage

Loaded by the core, but not used.

### moderators

Account IDs, separated by spaces, that are always moderators of the channel.
