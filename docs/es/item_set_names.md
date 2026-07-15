# item_set_names

[<-Volver a: World](database-world)

**Tabla \`item_set_names\`**

`tabla-sin-descripción`

**Estructura**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)                 | MEDIUMINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [name](#name)                   | VARCHAR(255) | SIGNED     |     | NO   |         |       |         |
| [InventoryType](#inventorytype) | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [WDBVerified](#wdbverified)     | SMALLINT     | UNSIGNED   |     | NO   | 1       |       |         |

**Descripción de los campos**

### Entry

ID del [Entry](item_template#entry) del objeto usado en [item_template](item_template)

### Name

[Nombre](item_template#name) del objeto usado en [item_template](item_template)

### InventoryType

En qué ranura (slot) se equipará el objeto.

| ID  | Slot Name                                                                                                                              |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Non equipable                                                                                                                          |
| 1   | Head                                                                                                                                   |
| 2   | Neck                                                                                                                                   |
| 3   | Shoulder                                                                                                                               |
| 4   | Shirt                                                                                                                                  |
| 5   | Chest (ver también Robe = 20)                                                                                                          |
| 6   | Waist                                                                                                                                  |
| 7   | Legs                                                                                                                                   |
| 8   | Feet                                                                                                                                   |
| 9   | Wrists                                                                                                                                 |
| 10  | Hands                                                                                                                                  |
| 11  | Finger                                                                                                                                 |
| 12  | Trinket                                                                                                                                |
| 13  | One-Hand (no confundir con Off-Hand = 22)                                                                                              |
| 14  | Shield (clase = armadura, no arma aunque esté en ranura de arma)                                                                       |
| 15  | Ranged (arcos) (ver también Ranged right = 26)                                                                                         |
| 16  | Back                                                                                                                                   |
| 17  | Two-Hand                                                                                                                               |
| 18  | Bag                                                                                                                                    |
| 19  | Tabard                                                                                                                                 |
| 20  | Robe (ver también Chest = 5)                                                                                                           |
| 21  | Main hand                                                                                                                              |
| 22  | Off Hand weapons (ver también One-Hand = 13)                                                                                           |
| 23  | Held in Off-Hand (tomo, bastón, flores, antorchas, orbes, etc... Ver también Off-Hand = 22) (clase = armadura, no arma aunque esté en ranura de arma) |
| 24  | Ammo                                                                                                                                   |
| 25  | Thrown                                                                                                                                 |
| 26  | Ranged right (varitas, armas de fuego) (ver también Ranged = 15)                                                                       |
| 27  | Quiver                                                                                                                                 |
| 28  | Relic (clase = armadura, no arma aunque esté en ranura de arma)                                                                        |                                                                             

### WDBVerified

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no ha sido parseada.

Si el valor es mayor que 0, entonces ha sido parseada con archivos WDB de esa build de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.

Si el valor es -Client Build, entonces fue parseada con archivos WDB de esa build de cliente específica y editada manualmente después por alguna necesidad especial.
