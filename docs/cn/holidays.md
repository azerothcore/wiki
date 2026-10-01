---
redirect_from: "/cn/Holidays"
---

# 节日（Holidays）

## holidays.dbc

[`返回:DBC`](dbc-index)

[如何将 DBC 数据导入到我的数据库](how-to-import-dbc-data-in-db)  

## 结构

| Column | Field                         | Type    | Notes                                                                              | Extra info                                                                 |
| ------ | ----------------------------- | ------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 0      | [eventID][1]                  | Integer | 节日事件 ID                                                                        |                                                                            |
| 1      | [eventStage1Duration][2]      | Integer | 阶段1 事件时长（针对阶段1                                                          | 既可作为准备阶段，也可作为主事件。参见 eventSchedulerType 了解更多信息）    |
| 2      | [eventStage2Duration][3]      | Integer | 阶段2 事件时长（针对阶段2                                                          | 既可作为主事件，也可作为冷却阶段。参见 eventSchedulerType 了解更多信息）    |
| 11     | [eventDate][4]                | Integer | 打包的 blizzdate - Epochdate=01.01.2000-00:00 - 如果第 12 列为 0，则忽略年份         |                                                                            |
| 37     | [Region][5]                   | integer | ???（需要更多研究）                                                                  |                                                                            |
| 38     | [Looping][6]                  | integer | ???（需要更多研究 - 仅用于"号召参战"（Call To Arms）事件）                          | 283 - 号召参战：奥特兰克山谷                                          |
|        |                               |         |                                                                                    | 284 - 号召参战：战歌峡谷                                          |
|        |                               |         |                                                                                    | 285 - 号召参战：阿拉希盆地                                           |
|        |                               |         |                                                                                    | 353 - 号召参战：风暴之眼                                       |
|        |                               |         |                                                                                    | 400 - 号召参战：远古海滩                                  |
|        |                               |         |                                                                                    | 420 - 号召参战：征服之岛                                       |
| 39     | [calendarFlags][7]            | integer | ???（需要更多研究）                                                                  |                                                                            |
| 49     | [eventCalendarName][8]        | iRefID  | 引用 HolidayNames.dbc 中的 Loc                                                            |                                                                            |
| 50     | [eventCalendarDescription][9] | iRefID  | 引用 HolidayDescriptions.dbc 中的 Loc                                              |                                                                            |
| 51     | [eventCalendarOverlay][10]    | String  | 用于游戏内日历事件装饰的叠加贴图                                                         |                                                                            |
| 52     | [priority][11]                | Integer | ???（需要更多研究）                                                                  |                                                                            |
| 53     | [eventSchedulerType][12]      | Integer | 定义使用哪个计时器，参见下方 eventSchedulerType                                                | -1: 重复，每年                                                         |
|        |                               |         |                                                                                    | 0: 重复，每周                                                          |
|        |                               |         |                                                                                    | 1: 重复，使用定义的日期                                               |
|        |                               |         |                                                                                    | 2: 重复，每小时                                                          |
| 54     | [eventFlags][13]              | Integer | ???（需要更多研究）                                                                  |                                                                            |

[1]: #eventid
[2]: #eventstage1duration
[3]: #eventstage2duration
[4]: #eventdate
[5]: #region
[6]: #looping
[7]: #calendarflags
[8]: #eventcalendarname
[9]: #eventcalendardescription
[10]: #eventcalendaroverlay
[11]: #priority
[12]: #eventschedulertype
[13]: #eventflags

### eventID

### eventStage1Duration

### eventStage2Duration

### eventDate

### Region

### Looping

### calendarFlags

### eventCalendarName

### eventCalendarDescription

### eventCalendarOverlay

### priority

## eventSchedulerType
```
eventSchedulerType 定义事件何时停止、开始等使用何种计时器 —— 以及在其"准备"阶段是否使用不同的阶段（可用 2 个阶段）
-1: 事件根据第 11 列、第 12 列等日期每年重复 —— 时长和可能的事件阶段取自第 1 列和第 2 列中给出的信息（在 DBC 中调整以使其与**每年**的变化保持一致）—— 如果第 12 列为 0，则仅使用字段 11 中的日期
0: 事件每 7 天重复，持续 <eventStage1Duration> 小时（服务端根据 eventID 硬编码开始日期）
1: 事件根据第 11 列、第 12 列等值重复（参见 -1）—— 如果存在 <eventStage2Duration>，则将 <eventStage1Duration> 作为事件的准备阶段时长
2: 事件每 X 小时重复（<eventStage2Duration> 作为事件的暂停/等待计时器）
```

### eventFlags
