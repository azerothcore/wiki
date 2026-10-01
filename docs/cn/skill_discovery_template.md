# skill\_discovery\_template

[<-返回至:World](database-world)

**`skill\_discovery\_template` 表**

此表控制学习法术时所谓的"领悟（discovery）"系统。该系统仅由炼金术专业使用，控制玩家在使用其他配方制作物品时"领悟"另一个配方的几率。![(question)](images/icons/emoticons/help_16.png){.emoticon .emoticon-question}

**表结构**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [spellId][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 可领悟法术的 SpellId               |
| [reqSpell][2]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 法术需求                           |
| [reqSkillValue][3] | SMALLINT  | UNSIGNED   |     | NO   | 0       |       | 技能点数需求                       |
| [chance][4]        | FLOAT     | SIGNED     |     | NO   | 0       |       | 领悟几率                           |

[1]: #spellid
[2]: #reqspell
[3]: #reqskillvalue
[4]: #chance

**字段说明**

### spellId

有机会被自动领悟的配方法术 ID。参见 Spell.dbc

### reqSpell

若为非零值，此字段控制必须具体使用哪个法术来触发领悟（例如，法术 41458 只有在使用法术 28575 时才会被领悟）。若为零，则任何配方的使用都可能触发领悟。参见 Spell.dbc

### reqSkillValue

在相关专业中能够领悟此配方所需的最低技能等级。

### chance

配方被自动"领悟"的几率（百分比），无论是通过任意配方的使用，还是通过 [reqSpell](#reqspell) 中定义的特定配方使用触发。
