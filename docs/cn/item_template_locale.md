# item_template_locale

[<-返回至:World](database-world)

**\`item_template_locale\` 表**

此表用于为本地化客户端提供物品的本地化字符串。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Name](#name) | TEXT |  |  | YES |  |  |  |
| [Description](#description) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**字段说明**

### ID

必须与 [item_template.entry](item_template#entry) 一致。

### locale

此行的语言区域（语言代码）。每个非默认语言区域对应一行，因此一条记录在此最多可以有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在主表中，不在此处。

### Name

此语言区域的 [item_template.name](item_template#name) 翻译。

### Description

此语言区域的 [item_template.description](item_template#description) 翻译。

### VerifiedBuild

此行已验证的客户端构建（来自 WDB/ADB 提取）。如不适用则为 `NULL`。
