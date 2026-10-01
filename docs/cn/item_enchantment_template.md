# item\_enchantment\_template

[<-返回至:World](database-world)

**`item\_enchantment\_template` 表**

此表保存了应该附加随机属性（random property）或随机后缀（random suffix）的物品的附魔概率信息。

**表结构**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ench][2]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [chance][3] | FLOAT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #ench
[3]: #chance

**字段说明**

### entry

此字段与 [item\_template](item_template) 表中的 RandomProperty **或** RandomSuffix 字段相关联。一件物品的这两个字段不能同时设置为非零值。

### ench

要应用于物品的附魔。如果当前行的 entry 用于 RandomProperty，则此字段指向 ItemRandomProperties.dbc 中的 ID。如果该 entry 用于 RandomSuffix，则此字段指向 [ItemRandomSuffix.dbc](https://wowdev.wiki/DB/ItemRandomSuffix) 中的 ID。

### chance

随机属性或后缀被应用到物品上的概率。对于此表中的每个 entry，所有属性/后缀的合并概率必须等于 100，否则物品可能无法获得随机附魔。

值必须为 >=0。如果该值不满足条件，SQL 将在 `item_enchantment_template_chk_1` 上失败。
