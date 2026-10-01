# gameobject_questitem

[<-返回:World](database-world)

**\`gameobject_questitem\` 表**

**表结构**

| 字段                               | 类型 | 属性     | 键 | 空 | 默认值 | 额外 | 注释 |
| ----------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [GameObjectEntry](#gameobjectentry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                         | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)                   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)     | INT  | UNSIGNED   |     | YES  | NULL    |       |         |

**字段说明**

### GameObjectEntry

[gameobject_template.entry](gameobject_template#entry)。

### Idx

索引 0-3

### ItemId

[item_template.entry](item_template#entry)。

### VerifiedBuild

此字段用于确定数据是否已通过 WDB 文件验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用该特定客户端版本（client build）的 WDB 文件进行解析。

如果值为 -1，则说明在从 WDB 中找到正确数据之前，它只是一个占位符。

如果值为 -客户端版本（Client Build），则表示已使用该特定[客户端版本](realmlist#gamebuild)的 WDB 文件进行解析，并因某些特殊需要而随后手动编辑。
