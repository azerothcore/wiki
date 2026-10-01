# npc_text_locale

[<-返回:World](database-world)

**\`npc_text_locale\` 表**

此表用于为本地化客户端提供 npc_texts 的本地化字符串。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [Locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Text0_0](#text0_0) | TEXT |  |  | YES |  |  |  |
| [Text0_1](#text0_1) | TEXT |  |  | YES |  |  |  |
| [Text1_0](#text1_0) | TEXT |  |  | YES |  |  |  |
| [Text1_1](#text1_1) | TEXT |  |  | YES |  |  |  |
| [Text2_0](#text2_0) | TEXT |  |  | YES |  |  |  |
| [Text2_1](#text2_1) | TEXT |  |  | YES |  |  |  |
| [Text3_0](#text3_0) | TEXT |  |  | YES |  |  |  |
| [Text3_1](#text3_1) | TEXT |  |  | YES |  |  |  |
| [Text4_0](#text4_0) | TEXT |  |  | YES |  |  |  |
| [Text4_1](#text4_1) | TEXT |  |  | YES |  |  |  |
| [Text5_0](#text5_0) | TEXT |  |  | YES |  |  |  |
| [Text5_1](#text5_1) | TEXT |  |  | YES |  |  |  |
| [Text6_0](#text6_0) | TEXT |  |  | YES |  |  |  |
| [Text6_1](#text6_1) | TEXT |  |  | YES |  |  |  |
| [Text7_0](#text7_0) | TEXT |  |  | YES |  |  |  |
| [Text7_1](#text7_1) | TEXT |  |  | YES |  |  |  |

**字段说明**

### ID

此值必须与 [npc_text.ID](npc_text#id) 一致。

### Locale

此行对应的语言（locale）（语言代码）。每种非默认语言对应一行，因此单条记录在这里最多可以有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在基础表中，不在此处。

### Text0_0 至 Text7_1

与此语言对应的 [npc_text](npc_text) 中 `textN_0` / `textN_1` 列的翻译变体。
