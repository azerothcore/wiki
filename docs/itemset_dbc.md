# itemset\_dbc

[<-Back-to:World](database-world)

**The \`itemset\_dbc\` table**

Holds rows that override or add to the data the core loads from ItemSet.dbc.

**Table: itemset\_dbc's Structure**

| Field                                   | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                               | INT          |          | NO   | PRI | 0       |       |         |
| [Name_Lang_enUS](#namelangenus)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enGB](#namelangengb)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_koKR](#namelangkokr)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_frFR](#namelangfrfr)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_deDE](#namelangdede)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enCN](#namelangencn)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhCN](#namelangzhcn)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_enTW](#namelangentw)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_zhTW](#namelangzhtw)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esES](#namelangeses)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_esMX](#namelangesmx)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ruRU](#namelangruru)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptPT](#namelangptpt)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_ptBR](#namelangptbr)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_itIT](#namelangitit)         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Unk](#namelangunk)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Name_Lang_Mask](#namelangmask)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [ItemID_1](#itemid1)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_2](#itemid2)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_3](#itemid3)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_4](#itemid4)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_5](#itemid5)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_6](#itemid6)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_7](#itemid7)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_8](#itemid8)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_9](#itemid9)                    | INT          |          | NO   |     | 0       |       |         |
| [ItemID_10](#itemid10)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_11](#itemid11)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_12](#itemid12)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_13](#itemid13)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_14](#itemid14)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_15](#itemid15)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_16](#itemid16)                  | INT          |          | NO   |     | 0       |       |         |
| [ItemID_17](#itemid17)                  | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_1](#setspellid1)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_2](#setspellid2)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_3](#setspellid3)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_4](#setspellid4)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_5](#setspellid5)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_6](#setspellid6)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_7](#setspellid7)            | INT          |          | NO   |     | 0       |       |         |
| [SetSpellID_8](#setspellid8)            | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_1](#setthreshold1)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_2](#setthreshold2)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_3](#setthreshold3)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_4](#setthreshold4)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_5](#setthreshold5)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_6](#setthreshold6)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_7](#setthreshold7)        | INT          |          | NO   |     | 0       |       |         |
| [SetThreshold_8](#setthreshold8)        | INT          |          | NO   |     | 0       |       |         |
| [RequiredSkill](#requiredskill)         | INT          |          | NO   |     | 0       |       |         |
| [RequiredSkillRank](#requiredskillrank) | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

ID references to the [itemset_dbc](#id) entries.

### Name_Lang_enUS

The name of the item set in the enUS locale. The core reads the locale columns by position, not by name, and this is column 1 of the 16, which is the slot for enUS.

### Name_Lang_enGB

The name of the item set in the koKR locale. The core reads the locale columns by position, not by name, and this is column 2 of the 16, which is the slot for koKR.

### Name_Lang_koKR

The name of the item set in the frFR locale. The core reads the locale columns by position, not by name, and this is column 3 of the 16, which is the slot for frFR.

### Name_Lang_frFR

The name of the item set in the deDE locale. The core reads the locale columns by position, not by name, and this is column 4 of the 16, which is the slot for deDE.

### Name_Lang_deDE

The name of the item set in the zhCN locale. The core reads the locale columns by position, not by name, and this is column 5 of the 16, which is the slot for zhCN.

### Name_Lang_enCN

The name of the item set in the zhTW locale. The core reads the locale columns by position, not by name, and this is column 6 of the 16, which is the slot for zhTW.

### Name_Lang_zhCN

The name of the item set in the esES locale. The core reads the locale columns by position, not by name, and this is column 7 of the 16, which is the slot for esES.

### Name_Lang_enTW

The name of the item set in the esMX locale. The core reads the locale columns by position, not by name, and this is column 8 of the 16, which is the slot for esMX.

### Name_Lang_zhTW

The name of the item set in the ruRU locale. The core reads the locale columns by position, not by name, and this is column 9 of the 16, which is the slot for ruRU.

### Name_Lang_esES

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_esMX

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_ruRU

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_ptPT

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_ptBR

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_itIT

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_Unk

Not supported in 3.3.5a and not used. The core's `LocaleConstant` list has only nine locales (enUS, koKR, frFR, deDE, zhCN, zhTW, esES, esMX, ruRU), and they are the first nine text columns.

### Name_Lang_Mask

The locale mask of the name. Not used by the core.

### ItemID_1

[Entry](item_template#entry) of the item for the item set [ItemID_1](#itemid1).

### ItemID_2

[Entry](item_template#entry) of the item for the item set [ItemID_2](#itemid2).

### ItemID_3

[Entry](item_template#entry) of the item for the item set [ItemID_3](#itemid3).

### ItemID_4

[Entry](item_template#entry) of the item for the item set [ItemID_4](#itemid4).

### ItemID_5

[Entry](item_template#entry) of the item for the item set [ItemID_5](#itemid5).

### ItemID_6

[Entry](item_template#entry) of the item for the item set [ItemID_6](#itemid6).

### ItemID_7

[Entry](item_template#entry) of the item for the item set [ItemID_7](#itemid7).

### ItemID_8

[Entry](item_template#entry) of the item for the item set [ItemID_8](#itemid8).

### ItemID_9

[Entry](item_template#entry) of the item for the item set [ItemID_9](#itemid9).

### ItemID_10

[Entry](item_template#entry) of the item for the item set [ItemID_10](#itemid10).

### ItemID_11

[Entry](item_template#entry) of the item for the item set [ItemID_11](#itemid11).

### ItemID_12

[Entry](item_template#entry) of the item for the item set [ItemID_12](#itemid12).

### ItemID_13

[Entry](item_template#entry) of the item for the item set [ItemID_13](#itemid13).

### ItemID_14

[Entry](item_template#entry) of the item for the item set [ItemID_14](#itemid14).

### ItemID_15

[Entry](item_template#entry) of the item for the item set [ItemID_15](#itemid15).

### ItemID_16

[Entry](item_template#entry) of the item for the item set [ItemID_16](#itemid16).

### ItemID_17

[Entry](item_template#entry) of the item for the item set [ItemID_17](#itemid17).

### SetSpellID_1

[Entry](spell) of the Spell that's used on [ItemID_1](#itemid1).

### SetSpellID_2

[Entry](spell) of the Spell that's used on [ItemID_2](#itemid2).

### SetSpellID_3

[Entry](spell) of the Spell that's used on [ItemID_3](#itemid3).

### SetSpellID_4

[Entry](spell) of the Spell that's used on [ItemID_4](#itemid4).

### SetSpellID_5

[Entry](spell) of the Spell that's used on [ItemID_5](#itemid5).

### SetSpellID_6

[Entry](spell) of the Spell that's used on [ItemID_6](#itemid6).

### SetSpellID_7

[Entry](spell) of the Spell that's used on [ItemID_7](#itemid7).

### SetSpellID_8

[Entry](spell) of the Spell that's used on [ItemID_8](#itemid8).

### SetThreshold_1

How many pieces of the Item Set you need referring to [SetSpellID_1](#setspellid1)

### SetThreshold_2

How many pieces of the Item Set you need referring to [SetSpellID_2](#setspellid2)

### SetThreshold_3

How many pieces of the Item Set you need referring to [SetSpellID_3](#setspellid3)

### SetThreshold_4

How many pieces of the Item Set you need referring to [SetSpellID_4](#setspellid4)

### SetThreshold_5

How many pieces of the Item Set you need referring to [SetSpellID_5](#setspellid5)

### SetThreshold_6

How many pieces of the Item Set you need referring to [SetSpellID_6](#setspellid6)

### SetThreshold_7

How many pieces of the Item Set you need referring to [SetSpellID_7](#setspellid7)

### SetThreshold_8

How many pieces of the Item Set you need referring to [SetSpellID_8](#setspellid8)

### RequiredSkill

[ID](skillline) of the Skill that's required of the Item Set.

### RequiredSkillRank

The required skill rank the player needs to have to use this Item Set.

