# skill\_extra\_item\_template

[<-返回至:World](database-world)

**`skill\_extra\_item\_template` 表**

此表存放的信息与以下情况相关：使用某些专业法术时，你有机会一次制造出多份该物品。

**表结构**

| Field                       | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| --------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [spellId][1]                | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 物品制造法术的 SpellId             |
| [requiredSpecialization][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | 专精法术 ID                        |
| [additionalCreateChance][3] | FLOAT     | SIGNED     |     | NO   | 0       |       | 额外制造几率                       |
| [additionalMaxNum][4]       | TINYINT   | UNSIGNED   |     | NO   | 0       |       | 额外制造的最大数量                 |

[1]: #spellid
[2]: #requiredspecialization
[3]: #additionalcreatechance
[4]: #additionalmaxnum

**字段说明**

### spellId

制造物品的法术 ID。参见 [Spell.dbc](spell)

### requiredSpecialization

所需的专精法术 ID。角色必须已学会此处指定的法术 ID，才有机会立即额外制造一个物品。

### additionalCreateChance

玩家立即额外制造一个物品的几率。

### additionalMaxNum

可以额外制造的最大物品数量。
