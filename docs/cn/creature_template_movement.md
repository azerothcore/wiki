# creature_template_movement

[<-返回：世界](database-world)

该表包含生物移动的描述，即生物可以移动和攻击的地方。

该表可以被 \`creature_movement_override\` 覆盖

**表结构**

| Field                      | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureId][1]            | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Ground][2]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Swim][3]                  | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Flight][4]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Rooted][5]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Chase][6]                 | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Random][7]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [InteractionPauseTimer][8] | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |

[1]: #creatureid
[2]: #ground
[3]: #swim
[4]: #flight
[5]: #rooted
[6]: #chase
[7]: #random
[8]: #interactionpausetimer

**字段说明**

#### CreatureId

这是脚本所链接的 [creature\_template.entry](creature_template#entry)。

#### Ground

| 状态 | 值 |
| ----- | ----- |
| 无  | 0     |
| 奔跑   | 1     |
| 悬停 | 2     |

#### Swim

| 状态 | 值 |
| ----- | ----- |
| 无  | 0     |
| 游泳  | 1     |

#### Flight

| 状态          | 值 |
| -------------- | ----- |
| 无           | 0     |
| 禁用重力 | 1     |
| 可飞行         | 2     |

#### Rooted

| 状态  | 值 |
| ------ | ----- |
| 无   | 0     |
| 定身 | 1     |

注意：

死亡后不会倒下的定身生物必须使用 \`Ground\`=1、\`Swim\`=0、\`Flight\`=0、\`Rooted\`=1（如果在水中则为 \`Swim\`=1）

死亡后会倒下的定身生物必须使用 \`Ground\`=0、\`Swim\`=0、\`Flight\`=1、\`Rooted\`=1

#### Chase

| 状态      | 值 |
| ---------- | ----- |
| 奔跑        | 0     |
| 可行走    | 1     |
| 始终行走 | 2     |

#### Random

| 状态     | 值 |
| --------- | ----- |
| 行走      | 0     |
| 可奔跑    | 1     |
| 始终奔跑 | 2     |

#### InteractionPauseTimer

在与玩家互动后生物将保持不移动的时间（以毫秒为单位）。
