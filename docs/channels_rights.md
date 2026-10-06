# channels\_rights

[<-Back-to:Characters](database-characters)

**The \`channels\_rights\` table**

Holds settings applied to chat channels by name: flags, speak delay, join message, delay message and moderators.

**Table: channels\_rights's Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [name][1]         | VARCHAR(128) |            | PRI | NO   |         |       |         |
| [flags][2]        | INT          | UNSIGNED   |     | NO   |         |       |         |
| [speakdelay][3]   | INT          | UNSIGNED   |     | NO   |         |       |         |
| [joinmessage][4]  | VARCHAR(255) |            |     | NO   | ''      |       |         |
| [delaymessage][5] | VARCHAR(255) |            |     | NO   | ''      |       |         |
| [moderators][6]   | TEXT         |            |     | YES  | NULL    |       |         |

[1]: #name
[2]: #flags
[3]: #speakdelay
[4]: #joinmessage
[5]: #delaymessage
[6]: #moderators

**Description of the table's fields**

### name

Name of the channel the rights apply to.

### flags

| Flag | Name                               | Description                                          |
| ---- | ---------------------------------- | ---------------------------------------------------- |
| 1    | CHANNEL_RIGHT_FORCE_NO_ANNOUNCEMENTS | Join and leave announcements are turned off.        |
| 2    | CHANNEL_RIGHT_FORCE_ANNOUNCEMENTS  | Join and leave announcements are turned on.          |
| 4    | CHANNEL_RIGHT_NO_OWNERSHIP         | The channel has no owner.                            |
| 8    | CHANNEL_RIGHT_CANT_SPEAK           | Only moderators can speak.                           |
| 16   | CHANNEL_RIGHT_CANT_BAN             | Nobody can be banned from the channel.               |
| 32   | CHANNEL_RIGHT_CANT_KICK            | Nobody can be kicked from the channel.               |
| 64   | CHANNEL_RIGHT_CANT_MUTE            | Nobody can be muted in the channel.                  |
| 128  | CHANNEL_RIGHT_CANT_CHANGE_PASSWORD | The password can not be changed.                     |
| 256  | CHANNEL_RIGHT_DONT_PRESERVE        | The channel is not saved to the database.            |

### speakdelay

Loaded by the core, but not used.

### joinmessage

Message sent to a player when they join the channel.

### delaymessage

Loaded by the core, but not used.

### moderators

Account IDs, separated by spaces, that are always moderators of the channel.
