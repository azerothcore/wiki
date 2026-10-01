# trainer_locale

[<-返回:世界数据库](database-world)

**\`trainer_locale\` 表**

该表保存训练师模板的本地化（locale）文本。

**表结构**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Greeting_lang](#greetinglang)  | MEDIUMTEXT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**字段说明**

### ID

[trainer.Id](trainer#id)。

### locale

| Locale |
| ------ |
| koKR   |
| frFR   |
| deDE   |
| zhCN   |
| zhTW   |
| esES   |
| esMX   |
| ruRU   |

### Greeting_lang

[trainer.Greeting](trainer#greeting) 的本地化版本。

### VerifiedBuild

该字段用于确定此游戏物体是否来源于经过验证的嗅探（sniff）数据。

如果值为 0，则表示它尚未被解析，或者继承自旧的数据库或其他核心。

如果值大于 0，则表示它是使用该特定客户端构建版本的嗅探数据解析的。

如果值为 -Client Build，则表示它是使用该特定客户端构建版本的 WDB 文件解析的，后来因某些特殊需要而被手动编辑。
