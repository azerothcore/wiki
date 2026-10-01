# battleground\_deserters

[<-返回:Characters](database-characters)

**\`battleground\_deserters\` 表**

该表保存了战场（BattleGrounds）逃兵的相关数据。要启用此类信息的存储，请在 **worldserver.config** 文件中设置 **Battleground.TrackDeserters.Enable = 1**。

**表结构**

| Field         | Type     | Attributes | Key | Null | Default | Extra | Comment                   |
| ------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------- |
| [guid][1]     | INT      | UNSIGNED   |     | NO   |         |       | characters.guid           |
| [type][2]     | TINYINT  | UNSIGNED   |     | NO   |         |       | 逃兵的类型     |
| [datetime][3] | DATETIME | SIGNED     |     | NO   |         |       | 逃兵的时间 |

[1]: #guid
[2]: #type
[3]: #datetime

**字段说明**

### guid

关联到 [characters.guid](characters#guid)。

### type

| Value | Description                                             |
| ----- | ------------------------------------------------------- |
| 0     | 玩家离开战场                                    |
| 1     | 玩家因离线被移出战场                |
| 2     | 玩家被邀请加入但拒绝          |
| 3     | 玩家被邀请加入但无任何操作（超时） |
| 4     | 玩家被邀请加入但下线                  |

### datetime

事件发生的日期和时间。
