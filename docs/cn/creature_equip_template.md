# creature\_equip\_template

[<-返回至:World](database-world)

## **表：creature\_equip\_template**

此表包含可以发送给每个生物的所有装备组合。

## 结构

| 字段               | 类型      | 属性     | 键   | 空   | 默认值 | 额外 | 注释           |
| ------------------ | --------- | -------- | ---- | ---- | ------ | ---- | -------------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED | PRI  | NO   | 0      |      | 唯一 entry     |
| [ID][2]            | TINYINT   | UNSIGNED | PRI  | NO   | 1      |      | 唯一 entry     |
| [ItemID1][3]       | MEDIUMINT | UNSIGNED |      | NO   | 0      |      |                |
| [ItemID2][4]       | MEDIUMINT | UNSIGNED |      | NO   | 0      |      |                |
| [ItemID3][5]       | MEDIUMINT | UNSIGNED |      | NO   | 0      |      |                |
| [VerifiedBuild][6] | INT       |           |      | YES  | NULL   |      |                |

[1]: #creatureid
[2]: #id
[3]: #itemid1
[4]: #itemid2
[5]: #itemid3
[6]: #verifiedbuild

## 字段说明

### CreatureID

与 [creature](creature) 表中的 [id](http://www.azerothcore.org/wiki/creature#id) 或 [creature\_template](creature_template) 表中的 [entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) 直接对应。

### ID

每个单独条目的附加标识符，使一个生物 entry 可以有多种装备。计数**必须**从 1 开始，并相应递增。

### ItemID1

这是来自 [Item.dbc](https://wowdev.wiki/DB/Item) 的、右手使用的装备的物品编号。

### ItemID2

这是来自 [Item.dbc](https://wowdev.wiki/DB/Item) 的、左手使用的装备的物品编号。

### ItemID3

这是来自 [Item.dbc](https://wowdev.wiki/DB/Item) 的、远程栏位使用的装备的物品编号。

### VerifiedBuild

此行所验证的客户端构建版本（来自 WDB/ADB 提取）。如果不适用则为 `NULL`。
