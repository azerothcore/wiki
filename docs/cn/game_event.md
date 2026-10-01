# game_event

[<-返回:World](database-world)

**\`game_event\` 表**

**表结构**

该表保存核心中由游戏事件系统（Game Event System）自动激活或停用的所有游戏事件的定义。

| 字段                          | 类型         | 属性     | 键 | 允许为空 | 默认值 | 额外   | 注释                                                                                                                                |
| ----------------------------- | ------------ | -------- | --- | -------- | ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| [eventEntry](#evententry)     | TINYINT      | UNSIGNED | PRI | NO       |        | Unique | 游戏事件的条目（Entry）                                                                                                             |
| [start_time](#starttime)      | TIMESTAMP    |          |     | YES      | NULL   |        | 绝对开始日期，事件绝不会在此之前开始                                                                                                |
| [end_time](#endtime)          | TIMESTAMP    |          |     | YES      | NULL   |        | 绝对结束日期，事件绝不会在此之后开始；如果为 NULL，则在每次服务器启动时将其隐式设置为未来 2 年                                                                 |
| [occurence](#occurence)       | BIGINT       | UNSIGNED |     | NO       |        |        | 事件两次发生之间的延迟（分钟）                                                                                                      |
| [length](#length)             | BIGINT       | UNSIGNED |     | NO       |        |        | 事件的持续时长（分钟）                                                                                                              |
| [holiday](#holiday)           | MEDIUMINT    | UNSIGNED |     | NO       |        |        | 客户端节日 ID（来自 dbc）                                                                                                           |
| holidayStage                  | TINYINT      | UNSIGNED |     | NO       |        |        |                                                                                                                                     |
| [description](#description)   | VARCHAR(255) | SIGNED   |     | YES      | NULL   |        | 在控制台显示的事件描述                                                                                                              |
| [world_event](#worldevent)    | TINYINT      | UNSIGNED |     | NO       |        |        | 0 表示普通事件，1 表示世界事件                                                                                                      |
| [announce](#announce)         | TINYINT      | UNSIGNED |     | YES      | 2      |        | 0 不公告，1 公告，2 使用配置中的值                                                                                                  |

**字段说明**

### eventEntry

事件的条目。请尽量保持其数值较低，并避免在列表中留下空档。最大 ID 越高，存储事件数据所使用的内存就越多。

### start_time

事件的绝对开始日期。只有当服务器的本地时间晚于此处设置的时间时，事件才会开始发生。

{% include note.html content="对于与具有动态日期计算的节日（复活节、农历新年、感恩节等）相关联的事件，start_time 会在服务器启动时自动计算，并覆盖数据库中设置的任何值。请参阅下面的动态节日系统章节。" %}

### end_time

事件的绝对结束日期。如果服务器的本地时间晚于此处设置的时间，事件将停止发生。

{% include note.html content="对于与具有动态日期计算的节日相关联的事件，end_time 会根据事件持续时长和 start_time 自动计算。" %}

### occurence

事件两次发生之间的分钟数。（2880 = 2 天，1440 = 1 天，以此类推）

{% include warning.html content="该值不能为 0，否则服务器将崩溃。" %}

### length

事件从本次发生开始后持续的分钟数。（2880 = 2 天，1440 = 1 天，以此类推）
该值必须小于 occurrence 的值，否则事件将永远不会停止。

### holiday

来自 [Holidays DBC 文件](holidays) 的节日 ID。该值会发送给客户端以更新日历。

### description

包含事件名称的字符串，每次事件开始或停止时会在控制台显示。

### world_event

这是一个布尔字段，用于确定该游戏事件是否为世界事件。0 = 普通事件，1 = 世界事件。要使世界事件生效，您至少需要填充 [game_event_condition](game_event_condition) 和 [game_event_quest_condition](game_event_quest_condition)。

### announce

| 值    | 描述                                              |
| ----- | ------------------------------------------------- |
| 0     | 不公告该事件                                      |
| 1     | 向世界公告该事件的描述                            |
| 2     | 使用配置中的 `event.announce` 设置                |

## 动态节日系统

某些节日发生在每年变化的日期。对于这些节日，服务器会在启动时使用天文算法和日历规则自动计算正确的日期。

### 动态计算的节日

| 节日 ID | 节日名称                       | 计算方法                                                         |
| ------- | ------------------------------ | ---------------------------------------------------------------- |
| 141     | 冬幕节（Feast of Winter Veil） | 冬至前 6 天（12 月 15-16 日）                                    |
| 181     | 复活节（Noblegarden）          | 复活节星期日的次日                                                |
| 201     | 儿童周（Children's Week）      | 4 月 25 日当天或之后的第一个星期一                                 |
| 283     | 收获节（Harvest Festival）     | 秋分前 2 天                                                       |
| 301     | 万圣节（Hallow's End）         | 固定为 10 月 18 日                                                |
| 321     | 农历新年（Lunar Festival）     | 中国农历新年的前一天（天文农历计算）                              |
| 324     | 仲夏火焰节（Midsummer Fire Festival） | 固定为 6 月 21 日                                           |
| 327     | 啤酒节（Brewfest）             | 9 月 15 日当天或之后的第一个星期六，再减去 7 天                   |
| 335     | 情人节（Love is in the Air）   | 2 月 3 日当天或之后的第一个星期一                                  |
| 341     | 亡灵节（Day of the Dead）      | 固定为 11 月 1 日                                                 |
| 372     | 丰收节（Pilgrim's Bounty）     | 11 月的第 4 个星期四减去 4 天                                     |
| 374     | 暗月马戏团（艾尔文森林）       | 3 月/6 月/9 月/12 月的第一个星期日减去 2 天                       |
| 375     | 暗月马戏团（莫高雷）           | 1 月/4 月/7 月/10 月的第一个星期日减去 2 天                       |
| 376     | 暗月马戏团（泰罗卡）           | 2 月/5 月/8 月/11 月的第一个星期日减去 2 天                       |

### 工作原理

1. 在服务器启动时，`GameEventMgr::LoadHolidayDates()` 会遍历所有节日规则
2. 为每个节日计算多年的日期（当前年份 ± 若干年）
3. 计算出的日期会写入 `Holidays.dbc` 的 Date[] 数组，用于日历显示
4. 相应的 game_event 的 `start_time` 和 `end_time` 会更新以匹配下一次发生的时间
5. 每次发生结束后，事件会自动重新排程

### 备注

- `holiday_dates` 数据库表已被**移除**——所有日期现在都动态计算
- 日历日期大约填充 4 年，以确保游戏内日历能正确显示
- 暗月马戏团每年多次发生，在莫高雷（1 月）、泰罗卡（2 月）、艾尔文森林（3 月）之间按月轮换并重复
