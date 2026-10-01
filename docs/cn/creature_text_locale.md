# creature_text_locale

[<-返回:世界](database-world)

**\`creature_text_locale\` 表**

此表用于为本地化客户端提供生物文本的本地化字符串。

**表结构**

| 字段           | 类型       | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
|-----------------|------------|------------|-----|------|---------|-------|---------|
| [CreatureID][1] | MEDIUMINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [GroupID][2]    | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ID][3]         | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Locale][4]     | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Text][5]       | TEXT       |            |     | YES  | NULL    |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #locale
[5]: #text

**字段说明**

### CreatureID

这是脚本所关联的 [creature\_template.entry](creature_template#entry)。

### GroupID

如果同一个 entry 有多个条目（生物说的文本不止一条），此列用于决定是随机说还是按顺序列出。如果一个生物有多个需要按给定顺序显示的文本，那么每个匹配的新条目都必须递增（例如 0、1、2、3...）。如果只有一个条目或只有一个组，此值应为 0。如果有多个文本组，此值在组内保持不变，而 id 在同一组内递增。

### ID

每个文本组的条目。当 entry（生物）相同且 groupid 不变时，这是唯一标识符，必须递增（例如 0、1、2、3...）。将根据其所属的 groupid 从该列表中随机选择生物要说的话。

### Locale

这是你想要进行翻译的语言。
你可以从以下选项中选择：

| ID | 语言 |
|----|----------|
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |

### Text

生物将要说出的翻译后的文本。
