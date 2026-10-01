# creature\_summon\_groups

[<-返回：世界](database-world)

# 表：creature\_summon\_groups

该表保存关于临时召唤生物的数据。可以将召唤物分组，并创建 Boss 的波次小怪（adds）等。

## 结构

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [summonerId][1]   | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [summonerType][2] | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [groupId][3]      | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [entry][4]        | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [position_x][5]   | FLOAT        |            |     | NO   | 0       |       |         |
| [position_y][6]   | FLOAT        |            |     | NO   | 0       |       |         |
| [position_z][7]   | FLOAT        |            |     | NO   | 0       |       |         |
| [orientation][8]  | FLOAT        |            |     | NO   | 0       |       |         |
| [summonType][9]   | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [summonTime][10]  | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment][11]     | VARCHAR(255) |            |     | NO   | ''      |       |         |

[1]: #summonerid
[2]: #summonertype
[3]: #groupid
[4]: #entry
[5]: #positionx
[6]: #positiony
[7]: #positionz
[8]: #orientation
[9]: #summontype
[10]: #summontime
[11]: #comment

## **字段说明**

### summonerId

召唤者的 ID，取决于 [summonerType](#summonertype)

### summonerType

召唤者的类型：

| 值 | 类型                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

组标识符，所有具有相同 [groupId](#groupid) 的生物将同时被召唤

### entry

来自 [creature\_template.entry](creature_template#entry) 的被召唤生物条目

### position\_x

生物将刷新的位置 X 坐标

### position\_y

生物将刷新的位置 Y 坐标

### position\_z

生物将刷新的位置 Z 坐标

### orientation

被召唤生物刷新时获得的方向

### summonType

| 值 | 名称                                   | 注释                                                            |
| ----- | -------------------------------------- | ------------------------------------------------------------------- |
| 1     | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | 在指定时间后或当生物消失时消失     |
| 2     | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | 在指定时间后或当生物死亡时消失           |
| 3     | TEMPSUMMON_TIMED_DESPAWN               | 在指定时间后消失                                     |
| 4     | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | 在生物脱离战斗后的指定时间后消失 |
| 5     | TEMPSUMMON_CORPSE_DESPAWN              | 死亡后立即消失                                      |
| 6     | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | 死亡后的指定时间后消失                         |
| 7     | TEMPSUMMON_DEAD_DESPAWN                | 当生物消失时消失                               |
| 8     | TEMPSUMMON_MANUAL_DESPAWN              | 当调用 UnSummon() 时消失                                  |

### summonTime

与召唤类型相关联的计时器

### Comment

注释
