# account\_muted

[<-返回至:Auth](database-auth)

**`account\_muted` 表**

此表包含被分配了聊天禁言（mute）的角色的账号 ID。

GM 命令：**.mute [$playerName] $timeInMinutes [$reason]**。

禁止角色 $playerName（或当前选中的角色）所在账号的任何角色在 $timeInMinutes 分钟内发送聊天消息。玩家可以离线。

**表结构**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [mutedate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [mutetime][3]   | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [mutedby][4]    | VARCHAR(50)  | SIGNED     |     | NO   |         |       |                          |
| [mutereason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |                          |

[1]: #guid
[2]: #mutedate
[3]: #mutetime
[4]: #mutedby
[5]: #mutereason

**字段说明**

### guid

被禁言 [account](account#id) 的 ID，取自被禁言的角色。此账号上的所有角色都将在 [mutetime](#mutetime) 期间被禁言。

### mutedate

禁言开始的日期。使用 UNIX 时间戳。

### mutetime

禁言时长，以分钟为单位。

### mutedby

发出禁言的 GM/版主昵称。

#### mutereason

包含禁言原因描述的文本字段。
