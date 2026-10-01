# guild

[<-返回至:Characters](database-characters)

**\`guild\` 表**

此表保存了公会的主要信息。所有已创建的公会或正在创建过程中的公会都会在此表中有一条记录。

**表结构**

| Field                | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]         | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [name][2]            | VARCHAR(24)  | SIGNED     |     | NO   | ''      |       |         |
| [leaderguid][3]      | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [EmblemStyle][4]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [EmblemColor][5]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [BorderStyle][6]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [BorderColor][7]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [BackgroundColor][8] | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [info][9]            | VARCHAR(500) | SIGNED     |     | NO   | ''      |       |         |
| [motd][10]           | VARCHAR(128) | SIGNED     |     | NO   | ''      |       |         |
| [createdate][11]     | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [BankMoney][12]      | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #name
[3]: #leaderguid
[4]: #emblemstyle
[5]: #emblemcolor
[6]: #borderstyle
[7]: #bordercolor
[8]: #backgroundcolor
[9]: #info
[10]: #motd
[11]: #createdate
[12]: #bankmoney

**字段说明**

### guildid

公会的 ID。该编号对每个公会都是唯一的，是识别公会的主要方法。

### name

公会名称。

### leaderguid

创建公会角色的 GUID。参见 [characters.guid](characters#guid)。

### EmblemStyle

公会战袍的徽章样式。

### EmblemColor

公会战袍的徽章颜色。

### BorderStyle

公会战袍的边框样式。

### BorderColor

公会战袍的边框颜色。

### BackgroundColor

公会战袍的背景颜色。

### info

显示在公会信息框中的文本消息。

### motd

显示在每日公告（Message Of The Day）框中的文本。

### createdate

公会创建时的日期。

### BankMoney

公会银行中当前存放的总金额，以铜币为单位。
