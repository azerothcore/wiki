# creature\_formations

[<-返回至:World](database-world)

**`creature\_formations` 表**

此表允许将怪物分组。组内成员会跟随其他成员，并攻击他们的目标。

**表结构**

| 字段           | 类型  | 属性     | 键   | 空   | 默认值 | 额外 | 注释 |
| -------------- | ----- | -------- | ---- | ---- | ------ | ---- | ---- |
| [leaderGUID][1]| INT   | UNSIGNED |      | NO   | NULL   |      |      |
| [memberGUID][2]| INT   | UNSIGNED | PRI  | NO   | NULL   |      |      |
| [dist][3]      | FLOAT | UNSIGNED |      | NO   | NULL   |      |      |
| [angle][4]     | FLOAT | UNSIGNED |      | NO   | NULL   |      |      |
| [groupAI][5]   | INT   | UNSIGNED |      | NO   | NULL   |      |      |
| [point_1][6]   | INT   | UNSIGNED |      | NO   | 0      |      |      |
| [point_2][7]   | INT   | UNSIGNED |      | NO   | 0      |      |      |

[1]: #leaderguid
[2]: #memberguid
[3]: #dist
[4]: #angle
[5]: #groupai
[6]: #point1
[7]: #point2

## leaderGUID

组长的 GUID

## memberGUID

组成员的 GUID。注意：为了确保分组正常工作，需要有一条同时包含 `leaderGUID` 和 `memberGUID` 且两者相等的记录（即以组长自身作为成员）。
示例：

* 组长 = 1
* 成员 = 2 和 3

| leaderGUID | memberGUID |
| ---------- | ---------- |
| 1          | 1          |
| 1          | 2          |
| 1          | 3          |

## dist

组长与成员之间的最大距离

值必须 >=0。如果值不满足该条件，SQL 将在 `creature_formations_chk_1` 上失败。

## angle

组长与成员之间的角度
注意：仅使用度数！值应在 0 到 360 之间。

![angle](assets/images/angle.png)

值必须 >=0。如果值不满足该条件，SQL 将在 `creature_formations_chk_1` 上失败。

## groupAI

设置组成员的行为，取值如下：

| 标志  | 位   | 名称                                           | 注释                                                                 |
| ----- | ---- | ---------------------------------------------- | -------------------------------------------------------------------- |
|       | 0    |                                                | 没有人协助任何人，且成员不跟随组长                                   |
| 0x001 | 1    | GROUP_AI_FLAG_MEMBER_ASSIST_LEADER             | 如果组长进入战斗（aggro），成员也会进入战斗                           |
| 0x002 | 2    | GROUP_AI_FLAG_LEADER_ASSIST_MEMBER             | 如果成员进入战斗（aggro），组长也会进入战斗                           |
|       | 3    |                                                | 每个人都互相协助，且成员不跟随组长                                   |
| 0x004 | 4    | GROUP_AI_FLAG_EVADE_TOGETHER                   | 如果任何成员脱离战斗（进入 evade 模式），所有人都会脱离战斗           |
| 0x008 | 8    | GROUP_AI_FLAG_RESPAWN_ON_EVADE                 | 如果成员脱离战斗（进入 evade 模式），所有人都会重新刷新               |
| 0x010 | 16   | GROUP_AI_FLAG_DONT_RESPAWN_LEADER_ON_EVADE     | 与标志 0x008 一起使用，防止组长重新刷新                               |
|       | 24   |                                                | 如果成员脱离战斗，除组长外的所有人都会重新刷新                       |
| 0x200 | 512  | GROUP_AI_FLAG_FOLLOW_LEADER                    | 没有人协助任何人，且成员跟随组长                                     |
|       | 515  |                                                | 每个人都互相协助，且成员跟随组长                                     |

## point\_1

## point\_2

这些值用于为 memberGUID 设置 leaderGUID 路径结束前的路径点，适用于路径是直线往返路径、且 memberGUID 不应在方向改变时越过 leaderGUID 的另一侧的情况。

如果你的组长有一条如下所示的路径，他从点 5 移动到点 1 再返回，你应该在 memberGUID 上设置 point\_1 = 4 和 point\_2 = 8。如果 memberGUID 在前往点 5 时处于 90 度角，那么它在返程时会切换到 270 度角。这仅仅是为了让生物保持在正确的侧边。对于直接跟随在 leaderGUID 身后的生物，或任何沿环形路径移动的生物，这些值可以保持为 0。

```
	1     2     3     4    5

	-----<--------->------

       8    7      6
```
