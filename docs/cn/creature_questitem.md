# creature_questitem

[<-返回：世界](database-world)

**\`creature_questitem\` 表**

保存 NPC 任务物品关系，即哪些 NPC 给予哪些任务物品。
| Field                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureEntry](#creatureEntry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)               | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT  |            |     | YES  | NULL    |       |         |

**字段说明**

### CreatureEntry

[creature_template.entry](creature_template#entry)。

### Idx

索引 0-3

### ItemId

[item_template.entry](item_template#entry)。

### VerifiedBuild

该字段用于确定数据是否源自经过验证的嗅探（sniff）。

如果值为 0，则表示尚未解析，或者继承自较旧的数据库或其他核心（Core）。

如果值大于 0，则表示已使用来自该特定客户端构建的嗅探进行解析。

如果值为 -客户端构建（Client Build），则表示已使用来自该特定客户端构建的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
