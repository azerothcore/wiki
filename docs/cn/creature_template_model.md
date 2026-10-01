# creature_template_model

[<-返回：世界](database-world)

**`creature_template_model` 表**

该表描述哪个模型被分配给特定的生物。

**表结构**

| Field                  | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [Idx][2]               | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [CreatureDisplayID][3] | INT      | UNSIGNED   |     | NO   |         |       |         |
| [DisplayScale][4]      | FLOAT    |            |     | NO   | 1       |       |         |
| [Probability][5]       | FLOAT    |            |     | NO   | 0       |       |         |
| [VerifiedBuild][6]     | SMALLINT |            |     | YES  |         |       |         |

[1]: #creatureid
[2]: #idx
[3]: #creaturedisplayid
[4]: #displayscale
[5]: #probability
[6]: #verifiedbuild

**字段说明**

### CreatureID

[creature_template.entry](creature_template#entry)

### Idx

索引 0-3。

### CreatureDisplayID

来自 CreatureDisplayInfo.dbc 的显示 ID。

### DisplayScale

修改模型的缩放比例。

### Probability

0-1

如果超过或低于 1，核心将在启动期间将其修正为等于 1。

### VerifiedBuild

该字段用于确定模板是否已根据 WDB 文件进行验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用来自该特定客户端构建的 WDB 文件进行解析。

如果值为 -1，则仅为占位符，直到在 WDB 中找到正确的数据。

如果值为 [客户端构建](realmlist#gamebuild)，则表示已使用来自该特定客户端构建的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
