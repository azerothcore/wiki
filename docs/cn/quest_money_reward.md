# quest\_money\_reward

[<-返回至:World](database-world)

**`quest\_money\_reward` 表**

该表用于根据玩家等级动态发放金钱奖励。

**表结构**

| Field             | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Level](#Level)   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Money0](#Money0) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money1](#Money1) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money2](#Money2) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money3](#Money3) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money4](#Money4) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money5](#Money5) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money6](#Money6) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money7](#Money7) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money8](#Money8) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Money9](#Money9) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

**字段说明：**

### Level

玩家等级

### Money0

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 0 时，玩家在特定等级获得的金钱奖励数量。

### Money1

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 1 时，玩家在特定等级获得的金钱奖励数量。

### Money2

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 2 时，玩家在特定等级获得的金钱奖励数量。

### Money3

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 3 时，玩家在特定等级获得的金钱奖励数量。

### Money4

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 4 时，玩家在特定等级获得的金钱奖励数量。

### Money5

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 5 时，玩家在特定等级获得的金钱奖励数量。

### Money6

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 6 时，玩家在特定等级获得的金钱奖励数量。

### Money7

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 7 时，玩家在特定等级获得的金钱奖励数量。

### Money8

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 8 时，玩家在特定等级获得的金钱奖励数量。

### Money9

当 [RewardMoneyDifficulty](quest_template#rewardmoneydifficulty) 设为 9 时，玩家在特定等级获得的金钱奖励数量。
