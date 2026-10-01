# spell\_required

[<-返回:世界数据库](database-world)

**\`spell\_required\` 表**

用于添加从训练师学习法术的限制条件。玩家在学会 'req\_spell' 之前无法学习 'spell\_id' 法术，当玩家失去 'req\_spell' 时，'spell\_id' 也会一并失去。该表同样用于专业分支（specialisation），因为学习专业分支需要先掌握对应等级的专业。

**表结构**

| Field          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_id][1]  | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [req_spell][2] | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |

[1]: #spellid
[2]: #reqspell

**字段说明**

### spell\_id

来自 [Spell.dbc](spell) 的法术 ID，表示在从训练师处学习该法术之前，需要先学会 \`req\_spell\`。

### req\_spell

来自 [Spell.dbc](spell) 的法术 ID，表示在学习 \`spell\_id\` 之前必须已经学会的法术。
