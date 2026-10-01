# guild\_bank\_tab

[<-返回至:Characters](database-characters)

**\`guild\_bank\_tab\` 表**

此表保存了所有使用公会银行的公会当前在用的全部标签页信息。

**表结构**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1] | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]   | TINYINT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabName][3] | VARCHAR(16)  | SIGNED     |     | NO   | "       |       |         |
| [TabIcon][4] | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| [TabText][5] | VARCHAR(500) | SIGNED     |     | YES  |         |       |         |

[1]: #guildid
[2]: #tabid
[3]: #tabname
[4]: #tabicon
[5]: #tabtext

**字段说明**

### guildid

该公会银行所属公会的 ID。

### TabId

标签页 ID。

### TabName

分配给标签页的名称。

### TabIcon

分配给标签页的图标。

### TabText

分配给标签页的文本。
