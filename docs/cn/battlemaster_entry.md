# battlemaster\_entry

[<-返回:World](database-world)

**\`battlemaster\_entry\` 表**

保存了哪个 NPC 可以开启哪种战场或竞技场的信息。

**表结构**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment                 |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------- |
| [entry][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 生物的 entry     |
| [bg_template][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | 战场模板 id |

[1]: #entry
[2]: #bgtemplate

**字段说明**

### entry

生物的 ID。参见 creature\_template.entry

### bg\_template

battleground\_template.id。
