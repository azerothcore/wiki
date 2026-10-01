# ChrRaces.dbc

[`返回:DBC`](dbc-index)

这个 DBC 包含所有可能的种族，其中一些种族未被使用且对玩家不可用。

**版本为：3.3.5a**

[如何将 DBC 数据导入我的数据库](how-to-import-dbc-data-in-db)

**表结构**

| 列 | 字段                   | 类型    | 备注                                                                                |
| ------ | ----------------------- | ------- | ------------------------------------------------------------------------------------ |
| 1      | ID                      | Integer |                                                                                      |
| 2      | [Flags](#flags)         | Integer |                                                                                      |
| 3      | FactionID               | iRefID  | 阵营模板 ID。创建界面中的顺序取决于此值。               |
| 4      | Exploration             | iRefID  | 用于探索区域时通过 SMSG_EXPLORATION_EXPERIENCE 播放。                          |
| 5      | MaleModel               | iRefID  | 仅用于角色创建/选择界面。服务器会在游戏内设置模型。 |
| 6      | FemaleModel             | iRefID  | 仅用于角色创建/选择界面。服务器会在游戏内设置模型。 |
| 7      | ClientPrefix            | String  | 名称的缩写形式。用于头盔模型。                                    |
| 8      | BaseLanguage            | Integer | 1 = 部落，7 = 联盟且不可玩。                                              |
| 9      | creatureType            | iRefID  | 始终为 7（人型生物）。                                                                 |
| 10     | ResSicknessSpellID      | Integer | 始终为 15007。                                                                        |
| 11     | SplashSoundID           | Integer | 矮人为 1090，其他种族为 1096。存储在 CGUnit 的 CGUnit::PostInit 中。  |
| 12     | clientFilestring        | String  | 与模型文件路径中使用的字符串相同。                                             |
| 13     | cinematicSequenceID     | iRefID  | 用于开场动画。                                                      |
| 14     | alliance                | Integer | 阵营（0 = 联盟，1 = 部落，2 = 不可用）                                 |
| 15-30  | RaceNameNeutral         | Loc     | 用于显示的名称。                                                                   |
| 31     | NameLangMask            | Integer | 字符串标志，未使用                                                                 |
| 32-47  | RaceNameFemale          | Loc     | 如果与基础大小写不同，否则未使用。对 zhCN 始终为 NULL。                 |
| 48     | NameFemaleLangMask      | Integer | 字符串标志，未使用                                                                 |
| 49-64  | RaceNameMale            | Loc     | 如果与基础大小写不同，否则未使用。对 zhCN 始终为 NULL。                 |
| 65     | NameMaleLangMask        | Integer | 字符串标志，未使用                                                                 |
| 66     | facialHairCustomization | String  | 面部特征的内部名称。                                              |
| 67     | facialHairCustomization | String  | 本地化版本在 luas 中。                                                      |
| 68     | hairCustomization       | String  | 发型自定义的内部名称。牛头人为角，其他种族为普通发型。 |
| 69     | required_expansion      | Integer | 0 = 经典旧世且不可玩，1 = 燃烧的远征                                      |

### 内容 {#content}

| ID  | 值   | 名称               |
| --- | ------- | ------------------ |
| 1   | 1       | 人类              |
| 2   | 2       | 兽人                |
| 3   | 4       | 矮人              |
| 4   | 8       | 暗夜精灵          |
| 5   | 16      | 亡灵             |
| 6   | 32      | 牛头人             |
| 7   | 64      | 侏儒              |
| 8   | 128     | 巨魔              |
| 9   | 256     | 地精             |
| 10  | 512     | 血精灵          |
| 11  | 1024    | 德莱尼            |
| 12  | 2048    | 邪能兽人            |
| 13  | 4096    | 娜迦               |
| 14  | 8192    | 破碎者             |
| 15  | 16384   | 骷髅           |
| 16  | 32768   | 维库人             |
| 17  | 65536   | 海象人            |
| 18  | 131072  | 森林巨魔       |
| 19  | 262144  | 牦牛人             |
| 20  | 524288  | 诺森德骷髅 |
| 21  | 1048576 | 冰霜巨魔          |

### 标志（Flags）

| 标志 | 描述  |
| ---- | ------------ |
| 1    | 不可玩 |
| 2    | 赤脚    |
| 4    | 可以骑乘    |
| 8    | 有秃头     |


### 阵营值（Faction values）

仅联盟 = 1101
仅部落 = 690
双阵营 = 1791（0 可能可行）


### 我如何获取这些值？

如果你想了解位运算的工作原理，可以阅读 [位与字节教程](bit-and-bytes-tutorial)。
