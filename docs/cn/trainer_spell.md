# trainer_spell

[<-返回:World](database-world)

**\`trainer_spell\` 表**

此表包含训练师法术条目。

**表结构**

| Field                           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TrainerId](#trainerid)         | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellId](#spellid)             | INT     | UNSIGNED   | PRI | NO   | 2       |       |         |
| [MoneyCost](#moneycost)         | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillLine](#reqskillline)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillRank](#reqskillrank)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility1](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility2](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility3](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqLevel](#reqlevel)           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT     |            |     | YES  | 0       |       |         |

**字段描述**

### TrainerId

[trainer.Id](trainer#id)。

### SpellId

要传授的法术 ID。

### MoneyCost

学习该法术所需的费用，以铜币为单位。

### ReqSkillLine

玩家学习该法术所需掌握的 [SkillLine ID](skillline)。

| ID  | Name           |
| --- | -------------- |
| 129 | First Aid      |
| 164 | Blacksmithing  |
| 165 | Leatherworking |
| 171 | Alchemy        |
| 182 | Herbalism      |
| 185 | Cooking        |
| 186 | Mining         |
| 197 | Tailoring      |
| 202 | Engineering    |
| 333 | Enchanting     |
| 356 | Fishing        |
| 393 | Skinning       |
| 633 | Lockpicking    |
| 755 | Jewelcrafting  |
| 773 | Inscription    |
| 776 | Runeforging    |

### ReqSkillRank

学习该法术所需的 [ReqSkillLine](#reqskillline) 最低技能点数。

### ReqAbility

玩家学习该法术所需的法术 ID。

### ReqLevel

学习该法术所需的玩家等级。

### VerifiedBuild

该字段用于判断此游戏对象是否来自已验证的 sniffs 数据。

如果值为 0，则表示尚未解析，或继承自旧版数据库或其他核心。

如果值大于 0，则表示已使用该特定客户端构建的 sniffs 数据解析。

如果值为负数（-Client Build），则表示使用该特定客户端构建的 WDB 文件解析，后因某些特殊需要而手动编辑。
