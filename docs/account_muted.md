# account\_muted

[<-Back-to:Auth](database-auth)

**The \`account\_muted\` table**

This table contains account IDs whose characters are assigned a ban chat (mute).

GM-Command: **.mute [$playerName] $timeInMinutes [$reason]**.

Disable chat messaging for any character from account of character $playerName (or currently selected) at $timeInMinutes minutes. Player can be offline.

**Table: account\_muted's Structure**

| Field                     | Type         |          | Null | Key | Default | Extra | Comment                  |
| :------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)             | INT          | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [mutedate](#mutedate)     | INT          | UNSIGNED | NO   | PRI | 0       |       |                          |
| [mutetime](#mutetime)     | INT          | UNSIGNED | NO   |     | 0       |       |                          |
| [mutedby](#mutedby)       | VARCHAR(50)  |          | NO   |     |         |       |                          |
| [mutereason](#mutereason) | VARCHAR(255) |          | NO   |     |         |       |                          |

**Description of the table's fields**

### guid

ID of muted [account](account#id), taken from muted character. All characters on this account will be muted for [mutetime](#mutetime).

### mutedate

The date then mute started. Used UNIX timestamp.

### mutetime

Mute duration in minutes.

### mutedby

Nickname of GM/moderator who issued the mute.

### mutereason

Text field with description of mute's reason.
