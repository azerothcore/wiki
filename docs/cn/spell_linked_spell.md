# spell\_linked\_spell

[<-返回至:World](database-world)

**\`spell\_linked\_spell\` 表**

此表为法术联动系统提供数据，告诉系统哪些法术在何种条件下触发什么。

**表结构**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_trigger][1] | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [spell_effect][2]  | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [type][3]          | SMALLINT  | UNSIGNED   |     | NO   |         |       |         |
| [comment][4]       | text      |            |     | NO   |         |       |         |

[1]: #spelltrigger
[2]: #spelleffect
[3]: #type
[4]: #comment

**字段说明**

### spell\_trigger

该法术被施放时，将触发 [spell\_effect](#spell_effect) 中列出的法术

### spell\_ effect

你想要被触发的法术。该法术如何运作由 [type](#type) 字段决定。

### type

有三种可能的值（0、1、2）。参见下文。

### comment

用于解释该联动的可选注释。

# **联动效果说明**

### type 0 (施放/CAST)

**触发模式**

- \***spell\_trigger > 0:** "当 *spell\_trigger* 被施放时..."
- \***spell\_trigger < 0:** "当 *spell\_trigger* 产生的光环被移除时..."

**效果**

- \***spell\_effect > 0:** *spell\_effect* 也会（带触发标记）作用于相同目标；如果 *spell\_trigger* 没有目标，则作用于施法者。
- \***spell\_effect < 0:** 移除 *spell\_effect* 产生的光环。

### type 1 (命中/HIT)

**触发模式**

- \***spell\_trigger > 0:** "当 *spell\_trigger* 命中一个目标时执行效果。我认为如果 *spell\_trigger* 命中了多个目标，效果会对每个被命中的目标分别执行。"

**效果**

- \***spell\_effect > 0:** *spell\_effect*（带触发标记）作用于同一目标。
- \***spell\_effect < 0:** 移除 *spell\_effect* 产生的光环。

### type 2 (光环/AURA)

**触发模式**

- \***spell\_trigger > 0:** "当光环 *spell\_trigger* 被施加到目标上 **并且** 从目标身上移除时执行效果。"

**效果**

\***spell\_effect > 0 (添加/移除光环)**

-   施加时：在同一目标上添加光环 *spell\_effect*。
-   移除时：在同一目标上移除光环 *spell\_effect*。

\***spell\_effect < 0 (免疫)**

-   施加时：使目标对 *spell\_effect* 免疫。
-   移除时：清除目标对 *spell\_effect* 的免疫。
