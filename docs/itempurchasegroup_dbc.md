# itempurchasegroup_dbc

[<-Back-to:World](database-world)

{% include warning.html content="THIS IS UN-USED AND INFORMATION CAN BE WRONG" %}

**The \`itempurchasegroup_dbc\` table**

**Table Structure**

| Field                             | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                         | INT     | UNSIGNED   | PRI | NO   | 0       |
| [ItemID_1](#itemid_1)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_2](#itemid_2)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_3](#itemid_3)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_4](#itemid_4)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_5](#itemid_5)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_6](#itemid_6)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_7](#itemid_7)             | INT     | UNSIGNED   |     | NO   | 0       |
| [ItemID_8](#itemid_8)             | INT     | UNSIGNED   |     | NO   | 0       |
| [Name_Lang_enUS](#name_lang_enus) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_enGB](#name_lang_engb) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_koKR](#name_lang_kokr) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_frFR](#name_lang_frfr) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_deDE](#name_lang_dede) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_enCN](#name_lang_encn) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_zhCN](#name_lang_zhcn) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_enTW](#name_lang_entw) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_zhTW](#name_lang_zhtw) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_esES](#name_lang_eses) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_esMX](#name_lang_esmx) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_ruRU](#name_lang_ruru) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_ptPT](#name_lang_ptpt) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_ptBR](#name_lang_ptbr) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_itIT](#name_lang_itit) | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_Unk](#name_lang_unk)   | VARCHAR | UNSIGNED   |     | NO   | NULL    |
| [Name_Lang_Mask](#name_lang_mask) | INT     | UNSIGNED   |     | NO   | 0       |

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

<details>

<summary>Click to see the content </summary>

| ID  | ItemID_1 | ItemID_2 | ItemID_3 | ItemID_4 | ItemID_5 | ItemID_6 | ItemID_7 | ItemID_8 | Name_Lang_enUS                   | Name_Lang_enGB | Name_Lang_koKR | Name_Lang_frFR | Name_Lang_deDE | Name_Lang_enCN | Name_Lang_zhCN | Name_Lang_enTW | Name_Lang_zhTW | Name_Lang_esES | Name_Lang_esMX | Name_Lang_ruRU | Name_Lang_ptPT | Name_Lang_ptBR | Name_Lang_itIT | Name_Lang_Unk | Name_Lang_Mask |
| --- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------------------------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | ------------- | -------------- |
| 1   | 34529    | 34530    | 33006    | 0        | 0        | 0        | 0        | 0        | Vengeful Gladiator Ranged Weapon |                |                |                |                |                |                |                |                |                |                |                |                |                |                |               | 16712190       |

</details>
