# itemset_dbc

[<-Volver a: World](database-world)

**Tabla \`itemset_dbc\`**

**Estructura**

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

ID que referencia a las entradas de [itemset_dbc](#id).

### Name_Lang_enUS

Nombre de referencia presumido.

### Name_Lang_enGB

Nombre de referencia presumido.

### Name_Lang_koKR

Nombre de referencia presumido.

### Name_Lang_frFR

Nombre de referencia presumido.

### Name_Lang_deDE

Nombre de referencia presumido.

### Name_Lang_enCN

Nombre de referencia presumido.

### Name_Lang_zhCN

Nombre de referencia presumido.

### Name_Lang_enTW

Nombre de referencia presumido.

### Name_Lang_zhTW

Nombre de referencia presumido.

### Name_Lang_esES

Nombre de referencia presumido.

### Name_Lang_esMX

Nombre de referencia presumido.

### Name_Lang_ruRU

Nombre de referencia presumido.

### Name_Lang_ptPT

Nombre de referencia presumido.

### Name_Lang_ptBR

Nombre de referencia presumido.

### Name_Lang_itIT

Nombre de referencia presumido.

### Name_Lang_Unk

Nombre de referencia presumido.

### Name_Lang_Mask

ID de referencia presumido para la máscara de idioma (Language Mask).

### ItemID_1

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_1](#itemid1).

### ItemID_2

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_2](#itemid2).

### ItemID_3

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_3](#itemid3).

### ItemID_4

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_4](#itemid4).

### ItemID_5

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_5](#itemid5).

### ItemID_6

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_6](#itemid6).

### ItemID_7

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_7](#itemid7).

### ItemID_8

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_8](#itemid8).

### ItemID_9

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_9](#itemid9).

### ItemID_10

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_10](#itemid10).

### ItemID_11

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_11](#itemid11).

### ItemID_12

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_12](#itemid12).

### ItemID_13

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_13](#itemid13).

### ItemID_14

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_14](#itemid14).

### ItemID_15

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_15](#itemid15).

### ItemID_16

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_16](#itemid16).

### ItemID_17

[Entry](item_template#entry) del objeto para el conjunto de objetos [ItemID_17](#itemid17).

### SetSpellID_1

[Entry](spell#entry) del hechizo que se usa en [ItemID_1](#itemid1).

### SetSpellID_2

[Entry](spell#entry) del hechizo que se usa en [ItemID_2](#itemid2).

### SetSpellID_3

[Entry](spell#entry) del hechizo que se usa en [ItemID_3](#itemid3).

### SetSpellID_4

[Entry](spell#entry) del hechizo que se usa en [ItemID_4](#itemid4).

### SetSpellID_5

[Entry](spell#entry) del hechizo que se usa en [ItemID_5](#itemid5).

### SetSpellID_6

[Entry](spell#entry) del hechizo que se usa en [ItemID_6](#itemid6).

### SetSpellID_7

[Entry](spell#entry) del hechizo que se usa en [ItemID_7](#itemid7).

### SetSpellID_8

[Entry](spell#entry) del hechizo que se usa en [ItemID_8](#itemid8).

### SetThreshold_1

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_1](#setspellid1)

### SetThreshold_2

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_2](#setspellid2)

### SetThreshold_3

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_3](#setspellid3)

### SetThreshold_4

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_4](#setspellid4)

### SetThreshold_5

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_5](#setspellid5)

### SetThreshold_6

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_6](#setspellid6)

### SetThreshold_7

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_7](#setspellid7)

### SetThreshold_8

Cuántas piezas del conjunto de objetos necesitas en referencia a [SetSpellID_8](#setspellid8)

### RequiredSkill

[ID](skillline#id) de la habilidad requerida por el conjunto de objetos.

### RequiredSkillRank

El rango de habilidad requerido que el jugador necesita tener para usar este conjunto de objetos.
