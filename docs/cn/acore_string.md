# acore_string

[<-返回:World](database-world)

**\`acore_string\` 表**

此表保存了服务器内部使用的所有字符串。它主要是为翻译目的而提供的。

其他语言的翻译保存在 [acore\_string\_locale](acore_string_locale) 中。

**表结构**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [content_default][2] | text |            |     | NO   |         |       |         |

[1]: #entry
[2]: #contentdefault

**字段描述**

### entry

核心用于标识字符串的 ID。这些 ID 在内部保存和使用，并且必须与核心所期望的对应。如果此表中不包含全部 ID，核心将无法运行。

### content\_default

英文翻译（locale ID 0）。
