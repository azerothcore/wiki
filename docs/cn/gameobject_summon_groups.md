# gameobject\_summon\_groups

[<-返回:World](database-world)

# 表：gameobject\_summon\_groups

此表保存关于以组的形式临时召唤的游戏对象（gameobject）的数据。它的工作方式与 [creature\_summon\_groups](creature_summon_groups) 类似，但针对的是游戏对象。

## 结构

| 字段               | 类型         | 属性     | 键 | 空 | 默认值 | 额外 | 注释 |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [summonerId](#summonerid)     | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [summonerType](#summonertype) | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [groupId](#groupid)           | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [entry](#entry)               | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [position\_x](#positionx)     | FLOAT        |            |     | NO   | 0       |       |         |
| [position\_y](#positiony)     | FLOAT        |            |     | NO   | 0       |       |         |
| [position\_z](#positionz)     | FLOAT        |            |     | NO   | 0       |       |         |
| [orientation](#orientation)   | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation0](#rotation0)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation1](#rotation1)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation2](#rotation2)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation3](#rotation3)       | FLOAT        |            |     | NO   | 1       |       |         |
| [respawnTime](#respawntime)   | INT          | UNSIGNED   |     | NO   | 120     |       |         |
| [Comment](#comment)           | VARCHAR(255) |            |     | NO   | ''      |       |         |

## 字段说明

### summonerId

触发召唤的对象的条目 ID，具体取决于 [summonerType](#summonertype)。

### summonerType

召唤对象的类型：

| 值 | 类型                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

组标识符。当该组被触发时，所有具有相同 `groupId` 和 `summonerId` 的游戏对象将同时被召唤。

### entry

要从 [gameobject\_template.entry](gameobject_template#entry) 中召唤的游戏对象的条目。

### position\_x

游戏对象将生成的 X 坐标。

### position\_y

游戏对象将生成的 Y 坐标。

### position\_z

游戏对象将生成的 Z 坐标。

### orientation

生成的游戏对象的朝向角度。为兼容性而保留；精确定位请使用四元数字段。

### rotation0

应用于所生成游戏对象的四元数旋转的 X 分量。默认值为 0。

### rotation1

四元数旋转的 Y 分量。默认值为 0。

### rotation2

四元数旋转的 Z 分量。默认值为 0。

### rotation3

四元数旋转的 W（标量）分量。默认值为 1，当其他分量都设置为 0 时，表示单位四元数（无旋转）。

### respawnTime

被召唤的游戏对象消失前的秒数。默认值为 120。使用 0 表示永久存在。

### Comment

此条目的可选的人类可读描述。
