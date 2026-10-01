# page_text_locale

[<-返回至:World](database-world)

**`page_text_locale` 表**

该表用于为本地化客户端提供 page_text 的本地化字符串。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Text](#text) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

## 字段说明

### ID

必须与 [page_text.ID](page_text#id) 匹配。

### locale

此行对应的语言区域（语言代码）。每个非默认语言区域对应一行，因此单条记录在此处最多可有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在基础表中，而不是此处。

### Text

针对该语言区域翻译的 [page_text.Text](page_text#text)。

### VerifiedBuild

此行的验证所针对的客户端版本（从 WDB/ADB 提取）。如不适用则为 `NULL`。
