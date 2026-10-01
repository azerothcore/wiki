# gameobject\_template\_addon

此表保存游戏对象的附加信息。

## 结构

| 字段               | 类型     | 属性     | 键 | 空 | 默认值 | 额外 | 注释 |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)     | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [faction](#faction) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [flags](#flags)     | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [mingold](#mingold) | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [maxgold](#maxgold) | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [artkit0](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit1](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit2](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit3](#artkit)  | INT      |            |     |      | 0       |       |         |

## 字段说明

### entry

游戏对象的 ID，来自 [gameobject\_template.entry](gameobject_template#entry)。

### faction

对象的阵营（如有）。参见 [FactionTemplate](factiontemplate)

### flags

| 标志       | 位  | 名称                        | 注释                                                                                                                  |
| ---------- | ---- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 0x00000001 | 1    | GO\_FLAG\_IN\_USE           | 使用中的游戏对象 - 在动画播放期间禁止交互                                                            |
| 0x00000002 | 2    | GO\_FLAG\_LOCKED            | 使游戏对象处于锁定状态。需要钥匙、法术或事件才能打开。提示框中会显示"已锁定"                   |
| 0x00000004 | 4    | GO\_FLAG\_INTERACT\_COND    | 无法选中，无法交互（需要满足交互条件 - 需要在客户端启用 GO_DYNFLAG_LO_ACTIVATE 才能交互） |
| 0x00000008 | 8    | GO\_FLAG\_TRANSPORT         | 游戏对象可以运输（船、电梯、汽车）                                                                           |
| 0x00000010 | 16   | GO\_FLAG\_NOT\_SELECTABLE   | 不可选中（即使在 GM 模式下也无法选中）                                                                                     |
| 0x00000020 | 32   | GO\_FLAG\_NODESPAWN         | 永不消失。对于具有开/关状态的游戏对象很典型（例如门）                                            |
| 0x00000040 | 64   | GO\_FLAG\_TRIGGERED         | （GO_FLAG_AI_OBSTACLE）使客户端将对象注册到名为 AIObstacleMgr 的机制中，具体作用未知       |
| 0x00000080 | 128  | GO\_FLAG\_FREEZE\_ANIMATION | 从 AzerothCore 起未使用                                                                                                  |
| 0x00000200 | 512  | GO\_FLAG\_DAMAGED           | 游戏对象已被攻城伤害                                                                                        |
| 0x00000400 | 1024 | GO\_FLAG\_DESTROYED         | 游戏对象已被摧毁                                                                                            |

### mingold

游戏对象在被访问/使用时可以掉落的最低金钱数量，以铜币为单位。

### maxgold

游戏对象在被访问/使用时可以掉落的最高金钱数量，以铜币为单位。

### artkit

GameObjectArtKit.dbc ID

如果对象被 MiscValue 为 19 - 22 的 SPELL_EFFCT_ACTIVATE_OBJECT 激活，则会更新显示效果。
