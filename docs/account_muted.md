# account\_muted

[<-Back-to:Auth](database-auth.md)

Read in: [English :gb:](account_muted) [Spanish :es:](es/account_muted)

**The \`account\_muted\` table**

This table contains account IDs whose characters are assigned a ban chat (mute).

GM-Command: **.mute [$playerName] $timeInMinutes [$reason]**.

Disable chat messaging for any character from account of character $playerName (or currently selected) at $timeInMinutes minutes. Player can be offline.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [mutedate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [mutetime][3]   | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [mutedby][4]    | VARCHAR(50)  | SIGNED     |     | NO   |         |       |                          |
| [mutereason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |                          |

[1]: #guid
[2]: #mutedate
[3]: #mutetime
[4]: #mutedby
[5]: #mutereason

**Description of the fields**

### guid

ID of muted [account](account#id), taken from muted character. All characters on this account will be muted for [mutetime](#mutetime).

### mutedate

The date then mute started. Used UNIX timestamp.

### mutetime

Mute duration in minutes.

### mutedby

Nickname of GM/moderator who issued the mute.

#### mutereason

Text field with description of mute's reason.
