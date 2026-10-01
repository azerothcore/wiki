# spell\_group

[<-返回至:World](database-world)

**\`spell\_group\` 表**

此表用于在核心中对法术进行分组，以便进行各种检查。一个法术可以被添加到多个组中，但在同一组中只能出现一次。

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #id
[2]: #spellid

**字段说明**

### id

组标识符
分配 id 的规则：

-   如果该组将被用于核心代码，请使用 1000 以下第一个可用的条目，并在 SpellMgr.h 的 SpellGroup 枚举中添加相应的枚举值
-   如果该组不会被用于核心代码，请使用大于 1000 的最低可用条目

### spell\_id

来自 Spell.dbc 的 SpellId，或以 "-" 为前缀的 spell\_group id。如果法术被添加到 spell\_ranks 中，则 spell\_id 必须是该法术的第一层级的 id。
