# creature_template_locale

[<-返回：世界](database-world)

**\`creature_template_locale\` 表**

该表用于为本地化客户端提供生物的本地化字符串。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Name](#name) | TEXT |  |  | YES |  |  |  |
| [Title](#title) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**字段说明**

### entry

必须与 [creature_template.entry](creature_template#entry) 匹配。该行提供该 creature_template 记录的本地化文本。

### locale

该行的区域设置（语言代码）。每种非默认区域设置各有一行，因此单个记录在此最多可有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在基础表中，而不是此处。

### Name

针对该区域设置翻译的 [creature_template.name](creature_template#name)。

### Title

针对该区域设置翻译的 [creature_template.subname](creature_template#subname)（标题）。

### VerifiedBuild

验证该行所依据的客户端构建（来自 WDB/ADB 提取）。如果不适用则为 `NULL`。
