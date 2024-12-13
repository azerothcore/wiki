# itemset_dbc

[<-Back-to:World](database-world)

**The \`itemset_dbc\` table**

**Table Structure**

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

### ID

ID references to the [itemset_dbc](#id) entries.

### Name_Lang_enUS

Pressumed reference name.

### Name_Lang_enGB

Pressumed reference name.

### Name_Lang_koKR

Pressumed reference name.

### Name_Lang_frFR

Pressumed reference name.

### Name_Lang_deDE

Pressumed reference name.

### Name_Lang_enCN

Pressumed reference name.

### Name_Lang_zhCN

Pressumed reference name.

### Name_Lang_enTW

Pressumed reference name.

### Name_Lang_zhTW

Pressumed reference name.

### Name_Lang_esES

Pressumed reference name.

### Name_Lang_esMX

Pressumed reference name.

### Name_Lang_ruRU

Pressumed reference name.

### Name_Lang_ptPT

Pressumed reference name.

### Name_Lang_ptBR

Pressumed reference name.

### Name_Lang_itIT

Pressumed reference name.

### Name_Lang_Unk

Pressumed reference name.

### Name_Lang_Mask

Pressumed reference ID for the Language Mask.

### ItemID_1

[Entry](item_template#entry) of the item for the item set [ItemID_1](#itemid_1).

### ItemID_2

[Entry](item_template#entry) of the item for the item set [ItemID_2](#itemid_2).

### ItemID_3

[Entry](item_template#entry) of the item for the item set [ItemID_3](#itemid_3).

### ItemID_4

[Entry](item_template#entry) of the item for the item set [ItemID_4](#itemid_3).

### ItemID_5

[Entry](item_template#entry) of the item for the item set [ItemID_5](#itemid_5).

### ItemID_6

[Entry](item_template#entry) of the item for the item set [ItemID_6](#itemid_6).

### ItemID_7

[Entry](item_template#entry) of the item for the item set [ItemID_7](#itemid_7).

### ItemID_8

[Entry](item_template#entry) of the item for the item set [ItemID_8](#itemid_8).

### ItemID_9

[Entry](item_template#entry) of the item for the item set [ItemID_9](#itemid_9).

### ItemID_10

[Entry](item_template#entry) of the item for the item set [ItemID_10](#itemid_10).

### ItemID_11

[Entry](item_template#entry) of the item for the item set [ItemID_11](#itemid_11).

### ItemID_12

[Entry](item_template#entry) of the item for the item set [ItemID_12](#itemid_12).

### ItemID_13

[Entry](item_template#entry) of the item for the item set [ItemID_13](#itemid_13).

### ItemID_14

[Entry](item_template#entry) of the item for the item set [ItemID_14](#itemid_14).

### ItemID_15

[Entry](item_template#entry) of the item for the item set [ItemID_15](#itemid_15).

### ItemID_16

[Entry](item_template#entry) of the item for the item set [ItemID_16](#itemid_16).

### ItemID_17

[Entry](item_template#entry) of the item for the item set [ItemID_17](#itemid_17).

### SetSpellID_1

[Entry](spell#entry) of the Spell that's used on [ItemID_1](#itemid_1).

### SetSpellID_2

[Entry](spell#entry) of the Spell that's used on [ItemID_2](#itemid_2).

### SetSpellID_3

[Entry](spell#entry) of the Spell that's used on [ItemID_3](#itemid_3).

### SetSpellID_4

[Entry](spell#entry) of the Spell that's used on [ItemID_4](#itemid_4).

### SetSpellID_5

[Entry](spell#entry) of the Spell that's used on [ItemID_5](#itemid_5).

### SetSpellID_6

[Entry](spell#entry) of the Spell that's used on [ItemID_6](#itemid_6).

### SetSpellID_7

[Entry](spell#entry) of the Spell that's used on [ItemID_7](#itemid_7).

### SetSpellID_8

[Entry](spell#entry) of the Spell that's used on [ItemID_8](#itemid_8).

### SetThreshold_1

How many pieces of the Item Set you need refering to [SetSpellID_1](#setspellid_1)

### SetThreshold_2

How many pieces of the Item Set you need refering to [SetSpellID_2](#setspellid_2)

### SetThreshold_3

How many pieces of the Item Set you need refering to [SetSpellID_3](#setspellid_3)

### SetThreshold_4

How many pieces of the Item Set you need refering to [SetSpellID_4](#setspellid_4)

### SetThreshold_5

How many pieces of the Item Set you need refering to [SetSpellID_5](#setspellid_5)

### SetThreshold_6

How many pieces of the Item Set you need refering to [SetSpellID_6](#setspellid_6)

### SetThreshold_7

How many pieces of the Item Set you need refering to [SetSpellID_7](#setspellid_7)

### SetThreshold_8

How many pieces of the Item Set you need refering to [SetSpellID_8](#setspellid_8)

### RequiredSkill

[ID](skillline#id) of the Skill that's required of the Item Set.

### RequiredSkillRank

The required skill rank the player needs to have to use this Item Set.

