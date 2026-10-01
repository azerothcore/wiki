# creature_template_spell

[<-返回：世界](database-world)

**\`creature_template_spell\` 表**

**表结构**

| Field              | Type      | Attribute | Key  | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | ---- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI  | NO   |         |       |         |
| [Index][2]         | TINYINT   | UNSIGNED  | PRI  | NO   | 0       |       |         |
| [Spell][3]         | MEDIUMINT | UNSIGNED  |      | YES  | Null    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |      | YES  | 0       |       |         |

[1]: #creatureid
[2]: #index
[3]: #spell
[4]: #verifiedbuild

**字段说明**

### CreatureID

来自 [creature_template.entry](creature_template#entry) 的生物条目。

### Index

值必须在此范围内。如果高于或低于此范围，SQL 将在 `creature_template_spell_chk_1` 上失败。

索引 0 - 7。

载具生物在动作条上的法术位置。

### Spell

可用于对一个生物进行精神控制（Mind Control）的法术 ID。

### VerifiedBuild

该字段用于确定模板是否已根据 WDB 文件进行验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用来自该特定客户端构建的 WDB 文件进行解析。

如果值为 -1，则仅为占位符，直到在 WDB 中找到正确的数据。

如果值为 -客户端构建（Client Build），则表示已使用来自该特定客户端构建的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
