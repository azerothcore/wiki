# gameobject_template_locale

[<-返回:World](database-world)

**\`gameobject_template_locale\` 表**

此表用于为本地化客户端提供游戏对象的本地化字符串。

**表结构**

| 字段 | 类型 | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [name](#name) | TEXT |  |  | YES |  |  |  |
| [castBarCaption](#castbarcaption) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**字段说明**

### entry

此值必须与 [gameobject_template.entry](gameobject_template#entry) 匹配。该行提供该 gameobject_template 记录的本地化内容。

### locale

此行的语言环境（语言代码）。每个非默认语言环境对应一行，因此单条记录在这里最多可以有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在主表中，而不是存储在这里。

### name

针对此语言环境翻译的 [gameobject_template.name](gameobject_template#name)。

### castBarCaption

针对此语言环境翻译的 [gameobject_template.castBarCaption](gameobject_template#castbarcaption)。

### VerifiedBuild

验证此行所依据的客户端版本（来自 WDB/ADB 提取）。如果不适用则为 `NULL`。
