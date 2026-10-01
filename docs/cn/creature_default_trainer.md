# creature_default_trainer

[<-返回至:World](database-world)

**`creature_default_trainer` 表**

**表结构**

| 字段                       | 类型 | 属性     | 键   | 空   | 默认值 | 额外 | 注释 |
| -------------------------- | ---- | -------- | ---- | ---- | ------ | ---- | ---- |
| [CreatureId](#creatureid)  | INT  | UNSIGNED | PRI  | NO   |        |      |      |
| [TrainerId](#trainerid)    | INT  | UNSIGNED |      | NO   | 0      |      |      |

**字段说明**

### CreatureId

[creature_template.entry](creature_template#entry)。

### TrainerId

[trainer.Id](trainer#id)。

| ID  | 注释                 |
| --- | -------------------- |
| 1   | 战士训练师           |
| 3   | 圣骑士训练师         |
| 7   | 猎人训练师           |
| 9   | 潜行者训练师         |
| 11  | 牧师训练师           |
| 13  | 死亡骑士训练师       |
| 14  | 萨满祭司训练师       |
| 16  | 法师训练师           |
| 31  | 术士训练师           |
| 33  | 德鲁伊训练师         |
| 36  | 坐骑与飞行训练师     |
