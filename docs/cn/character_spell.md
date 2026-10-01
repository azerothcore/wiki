# character\_spell

[<-返回:Characters](database-characters)

**\`character\_spell\` 表**

保存每个角色法术的相关信息。

**表结构**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 法术标识符               |
| [specMask][3] | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #spell
[3]: #specmask

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### spell

法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### specMask

保存使用该法术的专精（spec）的位掩码。
| Value | Type                              |
| ----- | --------------------------------- |
| 1     | 第一专精                          |
| 2     | 第二专精                          |
| 3     | 两个专精                          |
