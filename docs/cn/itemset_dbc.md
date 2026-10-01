# itemset_dbc

[<-返回至:World](database-world)

**\`itemset_dbc\` 表**

**表结构**

| Field                                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                               | INT     | SIGNED     | PRI | NO   | 0       |       |         |
| [Name_Lang_enUS](#namelangenus)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enGB](#namelangengb)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_koKR](#namelangkokr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_frFR](#namelangfrfr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_deDE](#namelangdede)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enCN](#namelangencn)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_zhCN](#namelangzhcn)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enTW](#namelangentw)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_zhTW](#namelangzhtw)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_esES](#namelangeses)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_esMX](#namelangesmx)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ruRU](#namelangruru)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ptPT](#namelangptpt)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ptBR](#namelangptbr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_itIT](#namelangitit)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_Unk](#namelangunk)         | VARCHAR | UNSIGNED   |     | YES  | NULL    |       |         |
| [Name_Lang_Mask](#namelangmask)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_1](#itemid1)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_2](#itemid2)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_3](#itemid3)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_4](#itemid4)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_5](#itemid5)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_6](#itemid6)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_7](#itemid7)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_8](#itemid8)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_9](#itemid9)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_10](#itemid10)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_11](#itemid11)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_12](#itemid12)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_13](#itemid13)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_14](#itemid14)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_15](#itemid15)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_16](#itemid16)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_17](#itemid17)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_1](#setspellid1)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_2](#setspellid2)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_3](#setspellid3)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_4](#setspellid4)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_5](#setspellid5)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_6](#setspellid6)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_7](#setspellid7)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_8](#setspellid8)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_1](#setthreshold1)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_2](#setthreshold2)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_3](#setthreshold3)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_4](#setthreshold4)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_5](#setthreshold5)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_6](#setthreshold6)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_7](#setthreshold7)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_8](#setthreshold8)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [RequiredSkill](#requiredskill)         | INT     | SIGNED     |     | NO   | 0       |       |         |
| [RequiredSkillRank](#requiredskillrank) | INT     | SIGNED     |     | NO   | 0       |

**字段说明**

### ID

ID 引用 [itemset_dbc](#id) 条目。

### Name_Lang_enUS

推测为引用名称。

### Name_Lang_enGB

推测为引用名称。

### Name_Lang_koKR

推测为引用名称。

### Name_Lang_frFR

推测为引用名称。

### Name_Lang_deDE

推测为引用名称。

### Name_Lang_enCN

推测为引用名称。

### Name_Lang_zhCN

推测为引用名称。

### Name_Lang_enTW

推测为引用名称。

### Name_Lang_zhTW

推测为引用名称。

### Name_Lang_esES

推测为引用名称。

### Name_Lang_esMX

推测为引用名称。

### Name_Lang_ruRU

推测为引用名称。

### Name_Lang_ptPT

推测为引用名称。

### Name_Lang_ptBR

推测为引用名称。

### Name_Lang_itIT

推测为引用名称。

### Name_Lang_Unk

推测为引用名称。

### Name_Lang_Mask

推测为语言掩码的引用 ID。

### ItemID_1

物品套装 [ItemID_1](#itemid1) 的物品 [Entry](item_template#entry)。

### ItemID_2

物品套装 [ItemID_2](#itemid2) 的物品 [Entry](item_template#entry)。

### ItemID_3

物品套装 [ItemID_3](#itemid3) 的物品 [Entry](item_template#entry)。

### ItemID_4

物品套装 [ItemID_4](#itemid4) 的物品 [Entry](item_template#entry)。

### ItemID_5

物品套装 [ItemID_5](#itemid5) 的物品 [Entry](item_template#entry)。

### ItemID_6

物品套装 [ItemID_6](#itemid6) 的物品 [Entry](item_template#entry)。

### ItemID_7

物品套装 [ItemID_7](#itemid7) 的物品 [Entry](item_template#entry)。

### ItemID_8

物品套装 [ItemID_8](#itemid8) 的物品 [Entry](item_template#entry)。

### ItemID_9

物品套装 [ItemID_9](#itemid9) 的物品 [Entry](item_template#entry)。

### ItemID_10

物品套装 [ItemID_10](#itemid10) 的物品 [Entry](item_template#entry)。

### ItemID_11

物品套装 [ItemID_11](#itemid11) 的物品 [Entry](item_template#entry)。

### ItemID_12

物品套装 [ItemID_12](#itemid12) 的物品 [Entry](item_template#entry)。

### ItemID_13

物品套装 [ItemID_13](#itemid13) 的物品 [Entry](item_template#entry)。

### ItemID_14

物品套装 [ItemID_14](#itemid14) 的物品 [Entry](item_template#entry)。

### ItemID_15

物品套装 [ItemID_15](#itemid15) 的物品 [Entry](item_template#entry)。

### ItemID_16

物品套装 [ItemID_16](#itemid16) 的物品 [Entry](item_template#entry)。

### ItemID_17

物品套装 [ItemID_17](#itemid17) 的物品 [Entry](item_template#entry)。

### SetSpellID_1

在 [ItemID_1](#itemid1) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_2

在 [ItemID_2](#itemid2) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_3

在 [ItemID_3](#itemid3) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_4

在 [ItemID_4](#itemid4) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_5

在 [ItemID_5](#itemid5) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_6

在 [ItemID_6](#itemid6) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_7

在 [ItemID_7](#itemid7) 上使用的法术的 [Entry](spell#entry)。

### SetSpellID_8

在 [ItemID_8](#itemid8) 上使用的法术的 [Entry](spell#entry)。

### SetThreshold_1

关于 [SetSpellID_1](#setspellid1)，你需要的物品套装件数

### SetThreshold_2

关于 [SetSpellID_2](#setspellid2)，你需要的物品套装件数

### SetThreshold_3

关于 [SetSpellID_3](#setspellid3)，你需要的物品套装件数

### SetThreshold_4

关于 [SetSpellID_4](#setspellid4)，你需要的物品套装件数

### SetThreshold_5

关于 [SetSpellID_5](#setspellid5)，你需要的物品套装件数

### SetThreshold_6

关于 [SetSpellID_6](#setspellid6)，你需要的物品套装件数

### SetThreshold_7

关于 [SetSpellID_7](#setspellid7)，你需要的物品套装件数

### SetThreshold_8

关于 [SetSpellID_8](#setspellid8)，你需要的物品套装件数

### RequiredSkill

物品套装所需的技能 [ID](skillline#id)。

### RequiredSkillRank

玩家使用此物品套装所需拥有的技能等级。
