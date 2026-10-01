# achievement\_dbc

[<-返回至:World](database-world)

**`achievement\_dbc` 表**

存储 [Achievement.dbc](achievement) 中缺失的成就数据

**表结构**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment                                                                          |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------------------------------------- |
| [ID][1]              | INT  | UNSIGNED   | PRI | NO   |         |       |                                                                                  |
| [requiredFaction][2] | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [mapID][3]           | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [points][4]          | INT  | UNSIGNED   |     | NO   | 0       |       | 完成成就所奖励的成就点数，服务端不使用                                         |
| [flags][5]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [count][6]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [refAchievement][7]  | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |

[1]: #id
[2]: #requiredfaction
[3]: #mapid
[4]: #points
[5]: #flags
[6]: #count
[7]: #refachievement

**字段说明**

### ID

这是来自 [Achievement\_Criteria.dbc](achievement_criteria)（第 2 列）的成就 ID

### requiredFaction

| 条件   | 阵营    |
| ------ | ------- |
| 两者   | -1      |
| 部落   | 0       |
| 联盟   | 1       |

### mapID

条件：玩家必须位于该地图上，才允许更新成就条件（如果未设置则为 -1）

### points

完成成就所奖励的成就点数，服务端不使用

### flags

| 名称                              | 值          | 注释                                                                                                  |
| --------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| ACHIEVEMENT_FLAG_COUNTER          | 0x00000001  | 仅作统计计数（永不停止和完成）                                                                        |
| ACHIEVEMENT_FLAG_HIDDEN           | 0x00000002  | 不发送给客户端 - 仅供内部使用                                                                        |
| ACHIEVEMENT_FLAG_STORE_MAX_VALUE  | 0x00000004  | 仅存储最大值？仅用于"达到 XX 级"                                                                     |
| ACHIEVEMENT_FLAG_SUMM             | 0x00000008  | 使用所有要求的标准值之和（并计算最大值）                                                             |
| ACHIEVEMENT_FLAG_MAX_USED         | 0x00000010  | 显示最大标准（并计算最大值？？）                                                                     |
| ACHIEVEMENT_FLAG_REQ_COUNT        | 0x00000020  | 使用非零的要求数量（并计算最大值）                                                                   |
| ACHIEVEMENT_FLAG_AVERAGE          | 0x00000040  | 显示为平均值（值 / 天数），取决于其他标志（默认使用最后一个标准值）                                   |
| ACHIEVEMENT_FLAG_BAR              | 0x00000080  | 显示为进度条（值 / 最大值），取决于其他标志（默认使用最后一个标准值）                                 |
| ACHIEVEMENT_FLAG_REALM_FIRST_REACH | 0x00000100 |                                                                                                       |
| ACHIEVEMENT_FLAG_REALM_FIRST_KILL  | 0x00000200 |                                                                                                       |

### count

应该始终为 1。

### refAchievement

应该始终为 0。
