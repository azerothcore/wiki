# creature_template_resistance

[<-返回：世界](database-world)

**\`creature_template_resistance\` 表**

**表结构**

| Field              | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI | NO   |         |       |         |
| [School][2]        | TINYINT   | UNSIGNED  | PRI | NO   |         |       |         |
| [Resistance][3]    | SMALLINT  | SIGNED    |     | YES  | NULL    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |     | YES  | 0       |       |         |

[1]: #creatureid
[2]: #school
[3]: #resistance
[4]: #verifiedbuild

**字段说明**

### CreatureID

来自 [creature_template.entry](creature_template#entry) 的生物条目。

### School

值必须在此范围内。如果高于或低于此范围，SQL 将在 `creature_template_resistance_chk_1` 上失败。

| 值 | 名称                |
| :---- | :------------------ |
| 1     | SPELL_SCHOOL_HOLY   |
| 2     | SPELL_SCHOOL_FIRE   |
| 3     | SPELL_SCHOOL_NATURE |
| 4     | SPELL_SCHOOL_FROST  |
| 5     | SPELL_SCHOOL_SHADOW |
| 6     | SPELL_SCHOOL_ARCANE |

### Resistance

抗性值。

### VerifiedBuild

该字段用于确定模板是否已根据 WDB 文件进行验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用来自该特定客户端构建的 WDB 文件进行解析。

如果值为 -1，则仅为占位符，直到在 WDB 中找到正确的数据。

如果值为 -客户端构建（Client Build），则表示已使用来自该特定客户端构建的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
