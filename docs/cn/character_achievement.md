# character\_achievement

[<-返回至:Characters](database-characters)

**\`character\_achievement\` 表**

该表保存角色已获得/完成的成就信息。

**注意：** 如果你从角色数据库中删除了一个“服务器首杀”成就，你必须重启服务器才能使其生效。

**表结构**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [achievement][2] | SMALLINT | UNSIGNED   | PRI | NO   |         |       |         |
| [date][3]        | INT      | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #achievement
[3]: #date

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### achievement

来自 [Achievement.dbc](achievement) 的成就 ID。

### date

该成就获得时的日期/时间，以 Unix 时间表示。参见 [Unix 时间戳计算器](http://www.unixtimestamp.com/index.php)
