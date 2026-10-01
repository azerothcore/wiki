# character\_social

[<-返回:Characters](database-characters)

**\`character\_social\` 表**

包含角色好友 / 屏蔽列表的相关数据。

**表结构**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------- | ----------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]   | INT         | UNSIGNED   | PRI | NO   | 0       |       | 角色全局唯一标识符                 |
| [friend][2] | INT         | UNSIGNED   | PRI | NO   | 0       |       | 好友全局唯一标识符                 |
| [flags][3]  | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       | 好友标志                           |
| [note][4]   | VARCHAR(48) | SIGNED     |     | NO   | ''      |       | 好友备注                           |

[1]: #guid
[2]: #friend
[3]: #flags
[4]: #note

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### friend

好友 / 被屏蔽角色的 GUID。参见 [characters.guid](characters#guid)。

### flags

| Value | Description                                                               |
|------ | ------------------------------------------------------------------------- |
| 0     | 未使用的条目 – 之前被添加为好友或被屏蔽（已移除 / 解除屏蔽）              |
| 1     | 添加为好友                                                               |
| 2     | 添加为被屏蔽的用户                                                       |
| 3     | 同时添加为好友，并且也加入屏蔽列表                                       |

### note

关于好友的备注（在客户端的友好列表中会显示在好友名字旁边）。

重要说明：最多只能有 50 个好友和 50 个被屏蔽的角色。如果遇到好友消失的问题，请先尝试移除其中一些好友。
