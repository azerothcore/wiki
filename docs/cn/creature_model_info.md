# creature\_model\_info

[<-返回至:World](database-world)

**`creature\_model\_info` 表**

此表包含所有怪物模型、它们的性别以及其他与模型相关的信息。这意味着当生物使用另一个模型时，这些信息也会随之改变。

**表结构**

| 字段                         | 类型      | 属性     | 键   | 空   | 默认值 | 额外 | 注释 |
| ---------------------------- | --------- | -------- | ---- | ---- | ------ | ---- | ---- |
| [DisplayID][1]               | int       | unsigned | PRI  | NO   | 0      |      |      |
| [BoundingRadius][2]          | float     |          |      | NO   | 0      |      |      |
| [CombatReach][3]             | float     |          |      | NO   | 0      |      |      |
| [Gender][4]                  | tinyint   | unsigned |      | NO   | 2      |      |      |
| [DisplayID_Other_Gender][5]  | int       | unsigned |      | NO   | 0      |      |      |
| [VerifiedBuild][6]           | mediumint |          |      | YES  | NULL   |      |      |

[1]: #displayid
[2]: #boundingradius
[3]: #combatreach
[4]: #gender
[5]: #displayidothergender
[6]: #verifiedbuild

**字段说明**

### DisplayID

来自 [CreatureDisplayInfo.dbc](https://wowdev.wiki/DB/CreatureDisplayInfo) 的显示 ID。

### BoundingRadius

此字段未被使用。其用途目前未知。它可能与寻路（path-finding）有关，也可能无关。

### CombatReach

此值是单位在游戏机制层面的半径：该值越大，单位的射程就越高，同时也越容易被更远地攻击到。

### Gender

生物的性别

| 值   | 描述   |
| ----- | ------ |
| 0     | 男性   |
| 1     | 女性   |
| 2     | 无     |

注意：没有嗅探数据不要修改此字段（参见提交：http://git.io/T7RLmA）。

### DisplayID_Other_Gender

指向 Creature\_model\_info.modelid。
当 entry 的性别为男性（0）或女性（1）时，此值可以指向相反的性别对应模型。

### VerifiedBuild

此行所验证的客户端构建版本（来自 WDB/ADB 提取）。如果不适用则为 `NULL`。
