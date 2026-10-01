# spell\_ranks

[<-返回至:World](database-world)

**\`spell\_ranks\` 表**

核心使用此表将同一法术的不同等级（在有等级的法术上看到的灰色文字）归入同一"法术主干（spell stem）"。这在一定程度上涉及光环叠加的检查（例如同一法术的不同等级）。一个法术不能关联到多个等级链（它们是"唯一的"）。

**表结构**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [first_spell_id][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]       | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [rank][3]           | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #firstspellid
[2]: #spellid
[3]: #rank

**字段说明**

### first\_spell\_id

来自 [Spell.dbc](spell) 的 SpellId，是法术等级链中的第一等级。它标识整个等级链。

### spell\_id

来自 [Spell.dbc](spell) 的 SpellId。

### rank

一个整数，用于在给定 \`spell\_id\` 的法术等级链中对法术进行排序。它可以与游戏中的等级文本不同（例如，客户端中的某些等级从 0 级开始，而服务器始终从 1 级开始）。必须满足以下几个条件：

-   至少需要两个等级
-   等级之间不能有跳跃（例如，一个法术是 3 级，一个是 5 级，而 4 级完全缺失）
-   等级不能有重复。
