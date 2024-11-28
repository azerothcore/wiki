# itempurchasegroup_dbc

[<-Back-to:World](database-world)

{% include warning.html content="THIS IS UN-USED AND INFORMATION CAN BE WRONG" %}

**The \`itempurchasegroup_dbc\` table**

**Table Structure**

| Field                             | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                         | INT     | UNSIGNED   | PRI | NO   | 0       |
| [ItemID_1](#itemid1)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_2](#itemid2)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_3](#itemid3)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_4](#itemid4)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_5](#itemid5)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_6](#itemid6)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_7](#itemid7)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_8](#itemid8)             | INT     | UNSIGNED   |     | NO   | 0       |
| [Name_Lang_enUS](#name_lang_enus) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_enGB](#namelangengb) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_koKR](#namelangkokr) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_frFR](#namelangfrfr) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_deDE](#namelangdede) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_enCN](#namelangencn) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_zhCN](#namelangzhcn) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_enTW](#namelangentw) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_zhTW](#namelangzhtw) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_esES](#namelangeses) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_esMX](#namelangesmx) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_ruRU](#namelangruru) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_ptPT](#namelangptpt) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_ptBR](#namelangptbr) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_itIT](#namelangitit) | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_Unk](#namelangunk)   | VARCHAR | UNSIGNED   |     | YES  | NULL    |
| [Name_Lang_Mask](#namelangmask) | INT     | UNSIGNED   |     | NO   | 0       |

### ID

ID that's used in [ItemExtendedCost.dbc](itemextendedcost_dbc#id).

### ItemID_1

[Entry](item_template#entry) of item required to for this entry [ItemID_1](#itemid_1).

### ItemID_2

[Entry](item_template#entry) of item required to for this entry [ItemID_2](#itemid_2).

### ItemID_3

[Entry](item_template#entry) of item required to for this entry [ItemID_3](#itemid_3).

### ItemID_4

[Entry](item_template#entry) of item required to for this entry [ItemID_4](#itemid_3).

### ItemID_5

[Entry](item_template#entry) of item required to for this entry [ItemID_5](#itemid_5).

### ItemID_6

[Entry](item_template#entry) of item required to for this entry [ItemID_6](#itemid_6).

### ItemID_7

[Entry](item_template#entry) of item required to for this entry [ItemID_7](#itemid_7).

### ItemID_8

[Entry](item_template#entry) of item required to for this entry [ItemID_8](#itemid_8).

### Name_Lang_enUS

Pressumed reference name.

Example: "Vengeful Gladiator Ranged Weapon"

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

