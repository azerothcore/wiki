# character\_glyphs

[<-返回:Characters](database-characters)

**\`character\_glyphs\` 表**

包含每个角色的所有个人雕文（glyph）数据。

**表结构**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [talentGroup][2] | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [glyph1][3]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph2][4]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph3][5]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph4][6]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph5][7]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph6][8]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |

[1]: #guid
[2]: #talentgroup
[3]: #glyph
[4]: #glyph
[5]: #glyph
[6]: #glyph
[7]: #glyph
[8]: #glyph

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### talentGroup

| ID | 名称               |
| -- | ------------------ |
| 0  | 第一套天赋专精     |
| 1  | 第二套天赋专精     |

### glyph 

该特定专精中 1-6 号雕文对应的 GlyphProperties entry（雕文属性条目）。
