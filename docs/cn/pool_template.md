# pool\_template

[<-返回至:World](database-world)

**\`pool\_template\` 表**

每个独立的刷新池（pool）都在此表中定义。

**表结构**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                               |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [entry][1]       | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       | Pool entry                            |
| [max_limit][2]   | INT          | UNSIGNED   |     | NO   | 0       |       | Max number of objects (0) is no limit |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |                                       |

[1]: #entry
[2]: #maxlimit
[3]: #description

**字段说明**

### entry

刷新池 ID。这是一个任意数字，仅用于关联此刷新池中的游戏对象、生物或任务。

### max\_limit

此刷新池中应刷新的对象的最大数量。
0 表示无限制。

### description

此字段描述刷新池所指内容的基本信息。示例：Snarlflare (14272)
