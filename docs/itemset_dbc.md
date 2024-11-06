# itemset_dbc

[<-Back-to:World](database-world)

**The \`itemset_dbc\` table**

**Table Structure**

| Field                                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
|-----------------------------------------|---------|------------|-----|------|---------|-------|---------|
| [ID](#id)                               | INT     | SIGNED     | PRI | NO   | 0       |       |         |
| [Name_Lang_enUS](#name_lang_enus)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enGB](#name_lang_engb)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_koKR](#name_lang_kokr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_frFR](#name_lang_frfr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_deDE](#name_lang_dede)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enCN](#name_lang_encn)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_zhCN](#name_lang_zhcn)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_enTW](#name_lang_entw)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_zhTW](#name_lang_zhtw)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_esES](#name_lang_eses)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_esMX](#name_lang_esmx)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ruRU](#name_lang_ruru)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ptPT](#name_lang_ptpt)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_ptBR](#name_lang_ptbr)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_itIT](#name_lang_itit)       | VARCHAR | SIGNED     |     | YES  | NULL    |       |         |
| [Name_Lang_Unk](#name_lang_unk)         | VARCHAR | UNSIGNED   |     | YES  | NULL    |       |         |
| [Name_Lang_Mask](#name_lang_mask)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_1](#itemid_1)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_2](#itemid_2)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_3](#itemid_3)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_4](#itemid_4)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_5](#itemid_5)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_6](#itemid_6)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_7](#itemid_7)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_8](#itemid_8)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_9](#itemid_9)                   | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_10](#itemid_10)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_11](#itemid_11)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_12](#itemid_12)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_13](#itemid_13)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_14](#itemid_14)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_15](#itemid_15)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_16](#itemid_16)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [ItemID_17](#itemid_17)                 | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_1](#setspellid_1)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_2](#setspellid_2)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_3](#setspellid_3)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_4](#setspellid_4)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_5](#setspellid_5)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_6](#setspellid_6)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_7](#setspellid_7)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetSpellID_8](#setspellid_8)           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_1](#setthreshold_1)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_2](#setthreshold_2)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_3](#setthreshold_3)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_4](#setthreshold_4)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_5](#setthreshold_5)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_6](#setthreshold_6)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_7](#setthreshold_7)       | INT     | SIGNED     |     | NO   | 0       |       |         |
| [SetThreshold_8](#setthreshold_8)       | INT     | SIGNED     |     | NO   | 0       |       |         |
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


