# character\_spell\_cooldown

[<-返回:Characters](database-characters)

**\`character\_spell\_cooldown\` 表**

保存每个角色来自角色法术或物品法术的剩余冷却时间。

**表结构**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符，低位部分           |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 法术标识符                         |
| [category][6] | INT       | UNSIGNED   |     | YES  | 0       |       | 法术类别                           |
| [item][3]     | INT       | UNSIGNED   |     | NO   | 0       |       | 物品标识符                         |
| [time][4]     | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |
| [needSend][5] | INT       | UNSIGNED   |     | NO   | 1       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #item
[4]: #time
[5]: #needsend
[6]: #category

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### spell

法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### category

该冷却时间所属的法术类别（同一类别的所有法术共享类别冷却时间）。如果法术没有类别，则为 \`0\`。

### item

如果法术是由物品施放的，则为物品 ID。参见 [item\_template.entry](item_template#entry)。

### time

法术冷却时间结束的时间，以 [Unix 时间](http://en.wikipedia.org/wiki/Unix_time) 表示。

### needSend

布尔值（0 或 1）。如果为 1，则下次登录时需要将该冷却条目发送给客户端。
