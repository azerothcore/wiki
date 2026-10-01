# pool\_quest

[<-返回至:World](database-world)

**\`pool\_quest\` 表**

此表包含关联到特定刷新池（pool）的任务列表。

**表结构**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #poolentry
[3]: #description

**字段说明**

### entry

任务 [id](quest_template#id)。

### pool\_entry

该任务所属的 [刷新池](pool_template#entry)。指向 [pool\_template entry](pool_template#entry)。

### description

针对此刷新池任务条目的可读描述或注释。
