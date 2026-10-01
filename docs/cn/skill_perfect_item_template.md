# skill_perfect_item_template

[<-返回至:World](database-world)

**`skill_perfect_item_template` 表**

实现了"完美"制造系统（最初来自《燃烧的远征》）：当施放制造法术时，有可能制造出该物品更高品质的"完美"版本，而非普通版本。每一行定义了一个制造法术的完美制造几率以及替代物品。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spellId](#spellid) | INT | UNSIGNED | PRI | NO | 0 |  | 物品制造法术的 SpellId |
| [requiredSpecialization](#requiredspecialization) | INT | UNSIGNED |  | NO | 0 |  | 专精法术 ID |
| [perfectCreateChance](#perfectcreatechance) | FLOAT | SIGNED |  | NO | 0 |  | 制造完美物品以替代普通物品的几率 |
| [perfectItemType](#perfectitemtype) | INT | UNSIGNED |  | NO | 0 |  | 替代制造的完美物品类型 |

**字段说明**

### spellId

物品制造法术的 SpellId

### requiredSpecialization

专精法术 ID

### perfectCreateChance

制造完美物品以替代普通物品的几率

### perfectItemType

替代制造的完美物品类型
