# points\_of\_interest\_locale

[<-返回至:World](database-world)

**\`locales\_points\_of\_interest\` 表**

`table-no-description`

**表结构**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            |     |      |         |       |         |
| [Name](#name)                   | TEXT       |            |     | YES  | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | NULL    |       |         |

**字段说明**

### ID

`field-no-description|1`

### locale

`field-no-description|2`

### Name

`field-no-description|3`

### VerifiedBuild

### VerifiedBuild

此字段用于确定数据是否来自已验证的 sniff（数据嗅探/抓包）。

如果值为 0，则表示尚未解析，或者是从旧数据库或其他核心继承而来。

如果值大于 0，则表示已使用该特定客户端 build 的 sniff 数据进行了解析。

如果值为 -Client Build，则表示已使用该特定客户端 build 的 WDB 文件进行了解析，并出于某些特殊需要稍后进行了手动编辑。
