# item_set_names

[<-返回至:World](database-world)

**\`item_set_names\` 表**

`table-no-description`

**表结构**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)                 | MEDIUMINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [name](#name)                   | VARCHAR(255) | SIGNED     |     | NO   |         |       |         |
| [InventoryType](#inventorytype) | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT          |            |     | YES  | NULL    |       |         |

**字段说明**

### Entry

物品 [Entry](item_template#entry) ID，用于 [item_template](item_template)

### Name

物品 [Name](item_template#name)，用于 [item_template](item_template)

### InventoryType

该物品将被装备在哪个槽位。

| ID  | Slot Name                                                                                                                              |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Non equipable                                                                                                                          |
| 1   | Head                                                                                                                                   |
| 2   | Neck                                                                                                                                   |
| 3   | Shoulder                                                                                                                               |
| 4   | Shirt                                                                                                                                  |
| 5   | Chest (see also Robe = 20)                                                                                                             |
| 6   | Waist                                                                                                                                  |
| 7   | Legs                                                                                                                                   |
| 8   | Feet                                                                                                                                   |
| 9   | Wrists                                                                                                                                 |
| 10  | Hands                                                                                                                                  |
| 11  | Finger                                                                                                                                 |
| 12  | Trinket                                                                                                                                |
| 13  | One-Hand (not to confuse with Off-Hand = 22)                                                                                           |
| 14  | Shield (class = armor, not weapon even if in weapon slot)                                                                              |
| 15  | Ranged (Bows) (see also Ranged right = 26)                                                                                             |
| 16  | Back                                                                                                                                   |
| 17  | Two-Hand                                                                                                                               |
| 18  | Bag                                                                                                                                    |
| 19  | Tabard                                                                                                                                 |
| 20  | Robe (see also Chest = 5)                                                                                                              |
| 21  | Main hand                                                                                                                              |
| 22  | Off Hand weapons (see also One-Hand = 13)                                                                                              |
| 23  | Held in Off-Hand (tome, cane, flowers, torches, orbs etc... See also Off-Hand = 22) (class = armor, not weapon even if in weapon slot) |
| 24  | Ammo                                                                                                                                   |
| 25  | Thrown                                                                                                                                 |
| 26  | Ranged right (Wands, Guns) (see also Ranged = 15)                                                                                      |
| 27  | Quiver                                                                                                                                 |
| 28  | Relic (class = armor, not weapon even if in weapon slot)                                                                               |                                                                             

### VerifiedBuild

该字段用于确定模板是否已通过 WDB 文件验证。

如果值为 0，则说明尚未解析。

如果值大于 0，则说明已使用来自该特定客户端构建的 WDB 文件进行解析。

如果值为 -1，则说明在 WDB 中找到正确数据之前，它只是一个占位符。

如果值为 -客户端构建（Client Build），则说明已使用来自该特定客户端构建的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
