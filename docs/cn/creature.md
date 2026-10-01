# creature

[<-返回至:World](database-world)

**表结构**

包含游戏世界中每个生物的每次刷新的个体刷新数据。

| 字段                   | 类型     | 属性     | 键   | 空   | 默认值 | 额外          | 注释                                  |
| ---------------------- | -------- | -------- | ---- | ---- | ------ | ------------- | ------------------------------------- |
| [guid][1]              | INT      | UNSIGNED | PRI  | NO   | NULL   | Auto Increment | 全局唯一标识符                       |
| [id][2]                | INT      | UNSIGNED |      | NO   | 0      |               | 生物标识符                           |
| [map][5]               | SMALLINT | UNSIGNED |      | NO   | 0      |               | 地图标识符                           |
| [zoneId][6]            | SMALLINT | UNSIGNED |      | NO   | 0      |               | 区域（zone）标识符                   |
| [areaId][7]            | SMALLINT | UNSIGNED |      | NO   | 0      |               | 地区（area）标识符                   |
| [spawnMask][8]         | TINYINT  | UNSIGNED |      | NO   | 1      |               |                                      |
| [phaseMask][9]         | SMALLINT | UNSIGNED |      | NO   | 1      |               |                                      |
| [equipment_id][10]     | TINYINT  | UNSIGNED |      | NO   | 1      |               |                                      |
| [position_x][11]       | FLOAT    | SIGNED   |      | NO   | 0      |               |                                      |
| [position_y][12]       | FLOAT    | SIGNED   |      | NO   | 0      |               |                                      |
| [position_z][13]       | FLOAT    | SIGNED   |      | NO   | 0      |               |                                      |
| [orientation][14]      | FLOAT    | SIGNED   |      | NO   | 0      |               |                                      |
| [spawntimesecs][15]    | INT      | UNSIGNED |      | NO   | 120    |               |                                      |
| [wander_distance][16]  | FLOAT    | SIGNED   |      | NO   | 5      |               | 随机移动的码（yard）距离。           |
| [currentwaypoint][17]  | INT      | UNSIGNED |      | NO   | 0      |               | 由核心使用的存储。"始终设置为 0"     |
| [curhealth][18]        | INT      | UNSIGNED |      | NO   | 1      |               | 由核心使用的存储。"始终设置为 1"     |
| [curmana][19]          | INT      | UNSIGNED |      | NO   | 0      |               | 由核心使用的存储。"始终设置为 0"     |
| [MovementType][20]     | TINYINT  | UNSIGNED |      | NO   | 0      |               | 0 不移动，1 随机，2 路径              |
| [npcflag][21]          | INT      | UNSIGNED |      | NO   | 0      |               | 覆盖 creature_template                |
| [unit_flags][22]       | INT      | UNSIGNED |      | NO   | 0      |               | 覆盖 creature_template                |
| [dynamicflags][23]     | INT      | UNSIGNED |      | NO   | 0      |               | 覆盖 creature_template                |
| [ScriptName][24]       | CHAR     |           |      | YES  | NULL   |               |                                      |
| [VerifiedBuild][25]    | INT      | SIGNED   |      | YES  | NULL   |               | 核心不使用。                          |
| [CreateObject][26]     | TINYINT  | UNSIGNED |      | NO   | 0      |               | 核心不使用。                          |
| [Comment][27]          | TEXT     |           |      | YES  | NULL   |               | 核心不使用。                          |

[1]: #guid
[2]: #id
[5]: #map
[6]: #zoneId
[7]: #areaId
[8]: #spawnmask
[9]: #phasemask
[10]: #equipmentid
[11]: #positionx
[12]: #positiony
[13]: #positionz
[14]: #orientation
[15]: #spawntimesecs
[16]: #wanderdistance
[17]: #currentwaypoint
[18]: #curhealth
[19]: #curmana
[20]: #movementtype
[21]: #npcflag
[22]: #unitflags
[23]: #dynamicflags
[24]: #scriptname
[25]: #verifiedbuild
[26]: #createobject
[27]: #comment

**字段说明**

### guid

赋予每个生物的唯一标识符，用于将一个生物与另一个生物区分开来。两个生物不能拥有相同的 GUID。

### id

实例化此生物时使用的[模板](creature_template#entry)的 ID。

如果希望单个刷新点从多个模板中选择（旧版 `id1`/`id2`/`id3` 的行为），请在 [creature_multispawn](creature_multispawn) 中添加以该生物 `guid` 为键的额外条目。

### map

生物所刷新的[地图](map)的 ID。

### zoneId

生物所在的区域（zone）的 ID。（例如 贫瘠之地）

如果在 `Calculate.Creature.Zone.Area.Data` 设置启用的情况下，此列会在世界服务器启动时自动填充。它来源于 AreaTable.dbc。

### areaId

生物所在的地区（area）的 ID。你可以将地区理解为区域的"子区域"，例如贫瘠之地中的甜水绿洲（Lushwater Oasis）。

如果在 `Calculate.Creature.Zone.Area.Data` 设置启用的情况下，此列会在世界服务器启动时自动填充。它来源于 AreaTable.dbc。

### spawnMask

控制生物在哪些难度下刷新。该值是位掩码，因此你可以将两个或多个值相加来组合效果。

示例：

4 + 8 = 12

生物将只在该生物所在地图的 10 人和 25 人英雄版本中刷新。

| 值   | 注释                                                                                  |
| ----- | -------------------------------------------------------------------------------------- |
| 0     | 不刷新                                                                                 |
| 1     | 只在地图的 10 人普通版本中刷新（包括没有英雄模式的地图）                                |
| 2     | 只在地图的 25 人普通版本中刷新（或 3.2 之前的英雄模式）                                 |
| 4     | 只在地图的 10 人英雄版本中刷新                                                          |
| 8     | 只在地图的 25 人英雄版本中刷新                                                          |
| 15    | 在地图的所有版本中刷新                                                                  |

### phaseMask

这是一个位掩码字段，描述生物将出现的所有阶段（phase）。光环 261 决定你能看到的阶段。例如，如果你有这个光环 <http://www.wowhead.com/?spell=55782>，你就能看到阶段 2 中的生物。如果你希望生物在阶段 1 和阶段 2 中都可见，你可以将阶段掩码设置为 3。

### equipment_id

在 [creature_equip_template](creature_equip_template) 中定义的、与 [entry](creature_template) 相对应的 ID。该值本质上是定义装备：

-   **-1**：将从 [creature_equip_template](creature_equip_template) 中的装备集中随机选择一套装备。
-   **0**：未定义装备。
-   **1+**：creature_equip_template 中的具体 ID。

如果生物是通过 `.npc add` 刷新的，则该值会被自动设置（如果 creature_equip_template 中没有任何内容，则为 0）。

### position_x

生物刷新点的 X 坐标。

### position_y

生物刷新点的 Y 坐标。

### position_z

生物刷新点的 Z 坐标。

### orientation

生物刷新点的朝向。（北 = 0.0；南 = pi (3.14159)）

### spawntimesecs

生物的刷新时间（以秒为单位）。

### wander_distance

生物可以离开其刷新点的最大距离。如果生物的 [MovementType](#movementtype) = 1，它也控制生物可以离开其刷新点多远。

### currentwaypoint

生物当前所在的[路径点](waypoint_data#point)（如果有）。

### curhealth

生物刷新时所拥有的生命值。

### curmana

生物刷新时所拥有的法力值。

### MovementType

与生物关联的移动类型。通常与其 [MovementType](creature_template#movementtype) 相同，但也可能不同。

### npcflag

与 [creature_template.npcflag](creature_template#npcflag) 相同。

注意：creature.npcflag 记录会覆盖 [creature_template.npcflag](creature_template#npcflag) 记录。

### unit_flags

与 creature_template.unit_flags 相同。

注意：

creature.unit_flags 记录会覆盖 [creature_template.unit_flags](creature_template#unitflags) 记录。

### dynamicflags

与 creature_template.dynamicflags 相同。

注意：

creature.dynamicflags 记录会覆盖 [creature_template.dynamicflags](creature_template#dynamicflags) 记录。

### ScriptName

与 creature_template.scriptname 相同。

creature.scriptname 记录会覆盖 [creature_template.scriptname](creature_template#scriptname) 记录。

### VerifiedBuild

此字段用于确定此生物是否来自经过验证的嗅探（sniff）数据。

如果值为 0，则说明尚未被解析，或者是从旧数据库或其他核心继承而来。

如果值大于 0，则说明已使用来自该特定客户端构建版本的嗅探数据进行解析。

如果值为 -客户端构建版本，则说明是使用该特定客户端构建版本的 WDB 文件解析的，后来因某些特殊需求而手动编辑过。

### CreateObject

此字段是生物特有的，用于确定坐标是否完善。

一旦生物被嗅探，数据包可以是 CreateObject1 或 CreateObject2。
CO1 生物通常已经刷新、移动过，因此会偏离其真实的刷新位置。
CO2 生物是在其刷新时被嗅探的，因此在大多数情况下，这就是它真实的刷新位置。

还有第三个值用于特殊情况下，即那些不按常规刷新、而是由脚本刷新的生物。它在功能上与 CO2 相同，仅用于更好地区分这些特殊情况。

### comment

此字段用于为该生物提供额外的上下文，主要用于嗅探值或脚本注释的语境中。

例如，如果生物的位置需要修改，原始位置会保留在 comment 字段中。或者，如果涉及的生物是更大脚本的一部分，comment 用于提供上下文。
