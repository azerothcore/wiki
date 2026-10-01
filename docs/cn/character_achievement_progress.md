# character\_achievement\_progress

[<-返回至:Characters](database-characters)

**\`character\_achievement\_progress\` 表**

**表结构**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [criteria][2] | SMALLINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [counter][3]  | INT         | UNSIGNED   |     | NO   |         |       |         |
| [date][4]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #criteria
[3]: #counter
[4]: #date

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### criteria

来自 [Achievement\_Criteria.dbc](achievement_criteria) 的条件（criteria）。

### counter

当前完成成就条件的进度计数。

### date

该成就获得时的日期。参见 [Unix 时间戳计算器](http://www.unixtimestamp.com/index.php)。
