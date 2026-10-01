# item\_instance

[<-返回至:物品实例](item_instance)

**`item\_instance\enchantments` 字段**

此字段实际上是一个独立的表。

有 36 个以空格分隔的数字。

每个数字都是三元组（Tuple）数字的一部分，代表应用于物品的一个附魔。

- 三元组中的第一个数字

    SpellItemEnchantment.dbc 中的 ID

- 三元组中的第二个数字

    附魔的持续时间（可选 - 某些法术使用）

- 三元组中的第三个数字

    充能次数（可选 - 某些法术使用）

每组按顺序排列的 3 个 ID 用于不同的用途。

| Purpose                    | Ordinal |
| -------------------------- | ------- |
| PERM_ENCHANTMENT_SLOT      | 0       |
| TEMP_ENCHANTMENT_SLOT      | 1       |
| SOCK_ENCHANTMENT_SLOT      | 2       |
| SOCK_ENCHANTMENT_SLOT_2    | 3       |
| SOCK_ENCHANTMENT_SLOT_3    | 4       |
| BONUS_ENCHANTMENT_SLOT     | 5       |
| PRISMATIC_ENCHANTMENT_SLOT | 6       |
| PROP_ENCHANTMENT_SLOT_0    | 7       |
| PROP_ENCHANTMENT_SLOT_1    | 8       |
| PROP_ENCHANTMENT_SLOT_2    | 9       |
| PROP_ENCHANTMENT_SLOT_3    | 10      |
| PROP_ENCHANTMENT_SLOT_4    | 11      |

### PERM_ENCHANTMENT_SLOT
  此附魔是物品设计的一部分。

### TEMP_ENCHANTMENT_SLOT
### SOCK_ENCHANTMENT_SLOT
  通过铁匠插槽（blacksmithing sockets）等专业技能应用到物品上的附魔。

### BONUS_ENCHANTMENT_SLOT
### PRISMATIC_ENCHANTMENT_SLOT
### PROP_ENCHANTMENT_SLOT
  某些物品在创建时获得的随机附魔。

  这些插槽依赖于 [item_template](item_template) 中的随机后缀（Random Suffix）或随机属性（RandomProperty）。

  如果在创建实例时应用了随机后缀，则它基于 [item_enchantment_template](item_enchantment_template) 表。物品附魔模板表给出了可能应用于给定物品的不同随机后缀及其被应用的概率。

  一旦选择了附魔，ItemRandomSuffix.dbc 中的值将用于确定附魔在指定插槽中的强度。

  如果将附魔放置在这 5 个插槽之一，但在 ItemRandom_Suffix dbc 中没有匹配的 AllocationPct_#，则该附魔对物品不会产生任何效果。
