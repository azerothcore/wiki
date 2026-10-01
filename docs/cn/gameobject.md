# gameobject

[<-返回:世界](database-world)

**\`gameobject\` 表**

该表保存着世界中每个已刷新游戏对象（game object）的单独对象数据。这些数据连同对象的模板数据一起被读取并用于在世界中实例化这些对象。

**表结构**

| 字段 (Field)           | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra)      | 注释 (Comment)                |
| ---------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ---------------- | ----------------------------- |
| [guid][1]              | INT         | UNSIGNED          | PRI      | NO        | NULL           | Auto increment   | 全局唯一标识符                |
| [id][2]                | INT         | UNSIGNED          |          | NO        | 0              |                  | 游戏对象标识符                |
| [map][3]               | SMALLINT    | UNSIGNED          |          | NO        | 0              |                  | 地图标识符                    |
| [zoneId][4]            | SMALLINT    | UNSIGNED          |          | NO        | 0              |                  | 区域标识符                    |
| [areaId][5]            | SMALLINT    | UNSIGNED          |          | NO        | 0              |                  | 子区域标识符                  |
| [spawnMask][6]         | TINYINT     | UNSIGNED          |          | NO        | 1              |                  |                               |
| [phaseMask][7]         | SMALLINT    | UNSIGNED          |          | NO        | 1              |                  |                               |
| [position_x][8]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [position_y][9]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [position_z][10]       | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [orientation][11]      | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [rotation0][12]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [rotation1][13]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [rotation2][14]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [rotation3][15]        | FLOAT       | SIGNED            |          | NO        | 0              |                  |                               |
| [spawntimesecs][16]    | INT         | SIGNED            |          | NO        | 0              |                  |                               |
| [animprogress][17]     | TINYINT     | UNSIGNED          |          | NO        | 0              |                  |                               |
| [state][18]            | TINYINT     | UNSIGNED          |          | NO        | 1              |                  |                               |
| [ScriptName][19]       | CHAR        |                   |          | YES       | ''              |                  |                               |
| [VerifiedBuild][20]    | INT         | SIGNED            |          | YES       | NULL            |                  | 核心（core）未使用。          |
| [Comment][21]          | TEXT        |                   |          | YES       | NULL            |                  |                               |

[1]: #guid
[2]: #id
[3]: #map
[4]: #zoneId
[5]: #areaId
[6]: #spawnmask
[7]: #phasemask
[8]: #positionx
[9]: #positiony
[10]: #positionz
[11]: #orientation
[12]: #rotation0
[13]: #rotation1
[14]: #rotation2
[15]: #rotation3
[16]: #spawntimesecs
[17]: #animprogress
[18]: #state
[19]: #scriptname
[20]: #verifiedbuild
[21]: #comment

**字段说明**

### guid

游戏对象的全局唯一标识符。该字段在所有游戏对象中必须是唯一的。

### id

游戏对象（gameobject）的模板 ID。参见 [gameobject_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### map

该对象被刷新所在的地图 ID。参见 Maps.dbc

### zoneId

该对象被刷新所在的区域（zone）的 ID。（例如 贫瘠之地）

如果启用了 `Calculate.Gameoject.Zone.Area.Data` 设置，该列会在 worldserver 启动时自动填入。它源自 AreaTable.dbc。

### areaId

该对象被刷新所在的子区域（area）的 ID。你可以把子区域理解为区域（zone）内的一个"子区"，例如 贫瘠之地 中的 甜水绿洲。

如果启用了 `Calculate.Gameoject.Zone.Area.Data` 设置，该列会在 worldserver 启动时自动填入。它源自 AreaTable.dbc。

### spawnMask

控制对象在哪些难度下刷新。

就像标志位一样，你可以按需叠加，因此 3 表示：在 10/25 人普通版本的地图中刷新（3.2 之前的所有地图）。

| 值 (Value) | 注释 (Comment)                                                              |
| ---------- | --------------------------------------------------------------------------- |
| 0          | 不刷新                                                                      |
| 1          | 仅在 10 人普通版本的地图中刷新（包括没有英雄模式的地图）                    |
| 2          | 仅在 25 人普通版本的地图中刷新（或 3.2 之前的英雄模式）                     |
| 4          | 仅在 10 人英雄版本的地图中刷新                                              |
| 8          | 仅在 25 人英雄版本的地图中刷新                                              |
| 15         | 在所有版本的地图中刷新                                                      |

### phaseMask

这是一个位掩码字段，描述该游戏对象将出现在所有相位（phase）中。光环（Aura）261 决定你能看到的相位。例如，如果你拥有这个光环 <http://www.wowhead.com/?spell=55782>，你就能看到相位 2 中的游戏对象。如果你希望游戏对象在相位 1 和相位 2 中都能被看到，你需要将 phaseMask 设为 3。

### position_x

X 坐标。

### position_y

Y 坐标。

### position_z

Z 坐标。

### orientation

朝向。（北 = 0，南 = 3.14159）

### rotation0

### rotation1

### rotation2

### rotation3

### spawntimesecs

该对象重新刷新所需的时间（秒）。

使用 0 将导致对象在使用后不会消失（despawn）。

使用负值将导致对象开始时处于"已消失"状态，直到某个脚本将其刷新出来。之后它会在此处指定的时间过后消失。

### animprogress

目前还不清楚这个字段的具体用途。不过，对于宝箱，请始终将其设置为 100。

### state

用于宝箱或门。

-   1 = 关闭
-   0 = 打开

### ScriptName

与 gameobject_template.scriptname 相同。

一条 gameobject.scriptname 记录会覆盖 [gameobject_template.scriptname](gameobject_template#scriptname) 记录。

### VerifiedBuild

该字段用于确定此游戏对象是否来自经过验证的抓包数据（sniffs）。

如果值为 0，则说明它尚未被解析，或者它继承自较旧的数据库或其他核心（Core）。

如果值大于 0，则说明它是使用该特定客户端版本的抓包数据解析得到的。

如果值为 -客户端版本号，则说明它是使用该特定客户端版本的 WDB 文件解析得到的，之后又出于某些特殊需要被手动编辑过。

### comment

该字段用于为此游戏对象添加额外的上下文信息，主要用于抓包值或脚本注释的语境。

例如，如果某个游戏对象的位置需要被修改，原始位置会保存在注释字段中。或者，如果相关游戏对象属于某个更大的脚本，该注释可用于提供上下文。
