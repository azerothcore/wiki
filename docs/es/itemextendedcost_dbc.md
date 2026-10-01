# itemextendedcost_dbc

[<-Volver a: World](database-world)

**Tabla \`itemextendedcost_dbc\`**

**Estructura**

| Field                                       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                   | INT  | UNSIGNED   | PRI | NO   | 0       |
| [HonorPoints](#honorpoints)                 | INT  | UNSIGNED   |     | NO   | 0       |
| [ArenaPoints](#arenapoints)                 | INT  | UNSIGNED   |     | NO   | 0       |
| [ArenaBracket](#arenabracket)               | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_1](#itemid1)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_2](#itemid2)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_3](#itemid3)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_4](#itemid4)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemID_5](#itemid5)                        | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_1](#itemcount1)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_2](#itemcount2)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_3](#itemcount3)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_4](#itemcount4)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemCount_5](#itemcount5)                  | INT  | UNSIGNED   |     | NO   | 0       |
| [RequiredArenaRating](#requiredarenarating) | INT  | UNSIGNED   |     | NO   | 0       |
| [ItemPurchaseGroup](#itempurchasegroup)     | INT  | UNSIGNED   |     | NO   | 0       |

**Descripción de los campos**

### ID

ID que se usa en [npc_vendor](npc_vendor#extendedcost)

### HonorPoints

La cantidad de puntos de honor requeridos.

### ArenaPoints

La cantidad de puntos de arena requeridos.

### ArenaBracket

| Value | Format |
| :-----: | :------: |
| 0     | 2 v 2  |
| 1     | 3 v 3  |
| 2     | 5 v 5  |

### ItemID_1

[Entry](item_template#entry) del objeto requerido para comprar [ItemID_1](#itemid1).

### ItemID_2

[Entry](item_template#entry) del objeto requerido para comprar [ItemID_2](#itemid2).

### ItemID_3

[Entry](item_template#entry) del objeto requerido para comprar [ItemID_3](#itemid3).

### ItemID_4

[Entry](item_template#entry) del objeto requerido para comprar [ItemID_4](#itemid4).

### ItemID_5

[Entry](item_template#entry) del objeto requerido para comprar [ItemID_5](#itemid5).

### ItemCount_1

La cantidad requerida de [ItemID_1](#itemid1).

### ItemCount_2

La cantidad requerida de [ItemID_2](#itemid2).

### ItemCount_3

La cantidad requerida de [ItemID_3](#itemid3).

### ItemCount_4

La cantidad requerida de [ItemID_4](#itemid4).

### ItemCount_5

La cantidad requerida de [ItemID_5](#itemid5).

### RequiredArenaRating

La cantidad de rating personal de arena requerido.

### ItemPurchaseGroup 

ESTO NO SE USA

